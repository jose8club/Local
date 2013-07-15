#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import controller_local
import view_local_form
import empleados_grid
from PySide import QtGui, QtCore
from main2_ui import Ui_window




class Locales(QtGui.QMainWindow):
    """Esta es la clase de la ventana principal que creará la grilla dond estan los locales"""

    first_time = True
    ciudad_actual = "*"
    s = "%"

    def __init__(self,parent=None):
        """constructor que crea la ventana"""
        super(Locales, self).__init__(parent)
        self.ui = Ui_window()
        self.ui.setupUi(self)
        self.load_datos()
        self.setup_search_bar()
        self.load_ciudades()
        self.set_signals()
        self.render_table()
        self.show()
             
    def render_table(self):
        """funcion que define las funciones de la tabla"""
        #Indica que el usuario al hacer click en la grilla seleccionará
        #una fila completa y no una celda
        self.ui.table_win.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        #Alterna el color de las filas de las grillas
        self.ui.table_win.setAlternatingRowColors(True)
        #Permite al usuario ordenar por columnas
        self.ui.table_win.setSortingEnabled(True)

    def conectar_tabla_empleados(self):
        """funcion que conecta la grilla principal con la tabla de empleados"""
        model = self.ui.table_win.model()
        index = self.ui.table_win.currentIndex()
        id_local = model.index(index.row(), 0, QtCore.QModelIndex()).data()
        form = empleados_grid.Form(self,id_local)
        form.setWindowTitle("Empleados por local")
        form.exec_()

   
    def set_signals(self):
        """función que establece las señales con los diferentes botones, el filtro de texto y el combobox"""
        self.ui.filtro.textChanged.connect(self.textChanged)
        self.ui.crear_btn.clicked.connect(self.pressAdd)
        self.ui.eliminar_btn.clicked.connect(self.pressDelete)
        self.ui.edit_button.clicked.connect(self.pressEdit)
        self.ui.combo.activated[str].connect(self.load_locales_por_ciudad)
        self.ui.table_win.doubleClicked.connect(self.conectar_tabla_empleados)
   

    def load_ciudades(self):
        """funcion que define el combobox"""
        ciudades = controller_local.get_ciudades()
        self.ui.combo.addItem("Todos", -1)
        for ciudad in ciudades:
            self.ui.combo.addItem(ciudad["nombre"], ciudad["id_ciudad"])


    def load_locales_por_ciudad(self, index):
        """función que carga los locales por ciudad al apretar el combobox"""
        id_ciudad = self.ui.combo.itemData(self.ui.combo.currentIndex())
        if id_ciudad == -1:
            ciudad = controller_local.get_locales()
        else:
            ciudad = controller_local.get_locales_by_ciudad(id_ciudad)
        self.load_datos(ciudad)

    def setup_search_bar(self):
        """función que agrega la caracteristica de autocompletacion"""
        wordList = controller_local.get_names()
        completer = QtGui.QCompleter(wordList, self)
        completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        self.ui.filtro.setCompleter(completer)
    
    
    #Completer para la barra de busqueda
    def update_search(self):
                wordList = controller_local.get_names()
                completer = QtGui.QCompleter(wordList, self)
                self.ui.filtro.setCompleter(completer)


    def textChanged(self,string):
        """función que filtra la tabla con la palabra ingresada en la barra de busqueda"""
        self.s = [string + '%']
        self.load_datos() #recarga tabla


    

    def pressAdd(self):
        """funcion que abre y hace funcionar la ventana de agregar locales mediante el boton PushAceptar"""
        #Abre la ventana "Form"
        form = view_local_form.Form(self)
        form.setWindowTitle("Agregar un Local")

        #Enlaza el boton con el metodo agregar (add).
        form.ui.PushAceptar.clicked.connect(form.add)

        form.rejected.connect(self.load_datos)
        form.exec_()


    def load_datos(self, locales=None):
        """función que carga todos los locales en la ventana principal"""   
                
        if locales is None:
                                    
            locales = controller_local.get_locales()
            
        self.model = QtGui.QStandardItemModel(len(locales), 3)
        #self.model.setHorizontalHeaderItem(0, QtGui.QStandardItem(u"id_local"))
        self.model.setHorizontalHeaderItem(0, QtGui.QStandardItem(u"Nombre"))
        self.model.setHorizontalHeaderItem(1, QtGui.QStandardItem(u"Direccion"))
        self.model.setHorizontalHeaderItem(2, QtGui.QStandardItem(u"Ciudad"))

        r = 0
        for row in locales:
                #index = self.model.index(r, 0, QtCore.QModelIndex()); 
                #self.model.setData(index, row['id_local'])
                index = self.model.index(r, 0, QtCore.QModelIndex()); 
                self.model.setData(index, row['nombre'])
                index = self.model.index(r, 1, QtCore.QModelIndex()); 
                self.model.setData(index, row['direccion'])
                index = self.model.index(r, 2, QtCore.QModelIndex()); 
                self.model.setData(index, row['ciudad'])
                r = r+1

        self.ui.table_win.setModel(self.model)
        self.ui.table_win.setColumnWidth(0, 200)
        self.ui.table_win.setColumnWidth(1, 345)
        self.ui.table_win.setColumnWidth(2, 199)
        #self.ui.table_win.setColumnWidth(3, 250)
        #self.ui.table_win.hideColumn(0)
        self.update_search()

  
    def pressDelete(self):
        """función que borra los locales"""
        model = self.ui.table_win.model()
        index = self.ui.table_win.currentIndex()
    
        if index.row() == -1: #No se ha seleccionado una fila
            self.errorMessageDialog = QtGui.QErrorMessage(self)
            self.errorMessageDialog.showMessage("Debe seleccionar una fila")
            return False
        else:
            #Obtenemos el id_local que es la primary key en la base de datos
            id_ciudad = model.index(index.row(), 2, QtCore.QModelIndex()).data()
            id_local = controller_local.get_locales_by_ciudad(id_ciudad)
            if (controller_local.delete_local(id_local)):
                self.load_datos()
                msgBox = QtGui.QMessageBox()
                msgBox.setText("EL registro fue eliminado.")
                msgBox.exec_()
                return True
            else:
                self.ui.errorMessageDialog = QtGui.QErrorMessage(self)
                self.ui.errorMessageDialog.showMessage("Error al eliminar")
                return False


    def pressEdit(self):
        """función que edita los locales"""
        model = self.ui.table_win.model()
        index = self.ui.table_win.currentIndex()
        if index.row() == -1: #No se ha seleccionado una fila
            #Notificacion si no se ha seleccionado una fila
            errorMessageBox = QtGui.QMessageBox.warning(self,"Error","Debe seleccionar una fila")
            return False
        else:
            #Abre la ventana "Form"
            form = view_local_form.Form(self)
            form.setWindowTitle("Editar un Local")

        #Obtiene los datos de la linea seleccionada
        nombre = model.index(index.row(), 0, QtCore.QModelIndex()).data()
        direccion = model.index(index.row(), 1, QtCore.QModelIndex()).data()
        ciudad = model.index(index.row(), 2, QtCore.QModelIndex()).data()
        
        #Enlaza el boton con el metodo editar (edit).
        form.ui.PushAceptar.clicked.connect(view_local_form.edit)
        form.ui.PushAceptar.setText("Editar")

        #Los inserta en los cuadros
        form.ui.nombre_label.setText(str(nombre))
        form.ui.direccion_label.setText(str(direccion))
        form.ui.ciudad_label.setText(int(ciudad))

        form.rejected.connect(self.load_datos)
        form.exec_()



def run():
    app = QtGui.QApplication(sys.argv)
    main = Locales()
    sys.exit(app.exec_())

if __name__ == '__main__':
        run()


