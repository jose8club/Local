#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import controller
import controller_local
import view_local_form
from PySide import QtGui, QtCore
from main2_ui import Ui_window




class Locales(QtGui.QMainWindow):

    first_time = True
    ciudad_actual = "*"
    s = "%"

    def __init__(self,parent=None):
        super(Locales, self).__init__(parent)
        self.ui = Ui_window()
	self.ui.setupUi(self)
	self.load_datos()
	self.setup_search_bar()
	self.setup_combo_ciudad()	
	self.set_signals()
	self.show()

   
    def set_signals(self):
		self.ui.filtro.textChanged.connect(self.textChanged)
		self.ui.crear_btn.clicked.connect(self.pressAdd)
		#self.ui.eliminar_btn.clicked.connect(self.pressDelete)
		#self.ui.edit_button.clicked.connect(self.pressEdit)
		self.ui.combo.activated[str].connect(self.activeCityBox)


    def activeCityBox(self, text):
		if text =="Todas":
			self.ciudad_actual = "*"
		else:
			self.ciudad_actual = str(text)
			self.load_datos()



    def setup_search_bar(self):
		#agrega la caracteristica de autocompletacion
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
		#filtra la tabla con la palabra ingresada en la barra de busqueda
		self.s = [string + '%']
		self.load_datos() #recarga tabla


    def setup_combo_ciudad(self):
		#Inicia el combo_box con las ciudades en la database.
		self.ui.combo.addItem("Todas")

		ciudad = controller_local.get_ciudades()
		for name in ciudad:
			self.ui.combo.addItem(name[1])


    def pressAdd(self):
		#Abre la ventana "Form"
		form = view_local_form.Form(self)
		form.setWindowTitle("Agregar un Local")

		#Enlaza el boton con el metodo agregar (add).
		form.ui.pushAceptar.clicked.connect(form.add)

		form.rejected.connect(self.load_datos)
		form.exec_()


    def load_datos(self):
        	
		if(self.first_time):
			locales = controller_local.get_locales()
			self.first_time = False
		else:
			locales = controller_local.search(self.s[0],self.ciudad_actual)

        	
        	self.model = QtGui.QStandardItemModel(len(locales), 5)
        	self.model.setHorizontalHeaderItem(0, QtGui.QStandardItem(u"id_local"))
        	self.model.setHorizontalHeaderItem(1, QtGui.QStandardItem(u"Nombre"))
        	self.model.setHorizontalHeaderItem(2, QtGui.QStandardItem(u"Direccion"))
        	self.model.setHorizontalHeaderItem(3, QtGui.QStandardItem(u"Empleados"))
		self.model.setHorizontalHeaderItem(4, QtGui.QStandardItem(u"Ciudad"))

        	r = 0
        	for row in locales:
            		index = self.model.index(r, 0, QtCore.QModelIndex()); 
            		self.model.setData(index, row['id_local'])
            		index = self.model.index(r, 1, QtCore.QModelIndex()); 
            		self.model.setData(index, row['nombre'])
            		index = self.model.index(r, 2, QtCore.QModelIndex()); 
            		self.model.setData(index, row['direccion'])
            		index = self.model.index(r, 3, QtCore.QModelIndex()); 
           		self.model.setData(index, row['empleados'])
			index = self.model.index(r, 4, QtCore.QModelIndex()); 
           		self.model.setData(index, row['fk_id_ciudad'])
           		r = r+1

                self.ui.table_win.setModel(self.model)

		self.ui.table_win.setColumnWidth(0, 120)
		self.ui.table_win.setColumnWidth(1, 120)
		self.ui.table_win.setColumnWidth(2, 120)
		self.ui.table_win.setColumnWidth(3, 120)
		self.ui.table_win.setColumnWidth(4, 120)
		self.ui.table_win.setColumnWidth(5, 120)


		
		self.update_search()

def run():
    app = QtGui.QApplication(sys.argv)
    main = Locales()
    sys.exit(app.exec_())

if __name__ == '__main__':
    	run()


