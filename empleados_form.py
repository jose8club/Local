#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PySide import QtGui, QtCore
import controller
#Importamos el constructor de la clase generada automáticamente
from form import Ui_Form
class Form(QtGui.QDialog):
<<<<<<< HEAD
    """clase que crea la ventana de ingreso de empleados"""
    def __init__(self, parent=None, rut=None):
        """constructor que crea la ventana de ingreso de empleados"""
=======
    
    def __init__(self, parent=None):
>>>>>>> cfeae8411eaab071f8161139976f70fe9df76134
        QtGui.QDialog.__init__(self, parent)
        self.ui =  Ui_Form()
        self.ui.setupUi(self)
	if rut is None:
            self.ui.add_btn.clicked.connect(self.add)
	    self.ui.comboBox.addItem("Masculino","M")
	    self.ui.comboBox.addItem("Femenino","F")
        else:
            datos_empleado = controller.obtener_empleado_por_rut(rut)
	    self.ui.rut_bar.setText(str(datos_empleado[0][0]))
	    self.ui.rut_bar.setReadOnly(True)
	    self.ui.nombre_bar.setText(datos_empleado[0][1])
            self.ui.cargo_bar.setText(datos_empleado[0][2])
            self.ui.sueldo_bar.setText(datos_empleado[0][4])
	    self.ui.local_bar.setText(str(datos_empleado[0][5]))
	    if(datos_empleado[0][3]=="M"):
		self.ui.comboBox.addItem("Masculino","M")
		self.ui.comboBox.addItem("Femenino","F")
            else:
		self.ui.comboBox.addItem("Femenino","F")
		self.ui.comboBox.addItem("Masculino","M")		
            self.ui.add_btn.clicked.connect(self.edit)	  

        self.ui.cancel_btn.clicked.connect(self.cancel)
	self.show()

    def add(self):
<<<<<<< HEAD
        """función que crea el ingreso de empleados"""
	genero = self.ui.comboBox.itemData(self.ui.comboBox.currentIndex())	
=======
>>>>>>> cfeae8411eaab071f8161139976f70fe9df76134
        if self.ui.rut_bar.text() == "":
            msgBox = QtGui.QMessageBox.warning(self,"Error","Ingrese el rut del empleado.")
        elif self.ui.nombre_bar.text() == "":
            msgBox = QtGui.QMessageBox.warning(self,"Error","Ingrese un nombre del empleado.")
        elif self.ui.cargo_bar.text() == "":
            msgBox = QtGui.QMessageBox.warning(self,"Error","Ingrese el cargo.")
        elif self.ui.sueldo_bar.text() == "":
            msgBox = QtGui.QMessageBox.warning(self,"Error","Ingrese el sueldo del empleado.")      
	else:
	    res = controller.agregar_empleado(self.ui.rut_bar.text(),self.ui.nombre_bar.text(),self.ui.cargo_bar.text(),
            	genero,self.ui.sueldo_bar.text(),self.ui.local_bar.text())
        if res:
	    self.reject()
            msgBox = QtGui.QMessageBox.information(self,"Exito","El registro fue agregado.")
	else:
            msgBox = QtGui.QMessageBox.critical(self,"Error","No se pudo agregar el registro.")


    def edit(self):
        rut = self.ui.rut_bar.text()
	nombre = self.ui.nombre_bar.text()
        cargo = self.ui.cargo_bar.text()
        genero = self.ui.comboBox.itemData(self.ui.comboBox.currentIndex())
        sueldo = self.ui.sueldo_bar.text()
        result = controller.editar_empleado(rut,nombre, cargo, genero, sueldo)
        if result:
            self.reject() #Cerramos y esto cargara nuevamente la grilla
        else:
            self.ui.mensajes.setText("Hubo un problema al intentar editar el alumno")

  
    def cancel(self):
        self.reject()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    main = Form()
    sys.exit(app.exec_())
