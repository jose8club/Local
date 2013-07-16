#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PySide import QtGui, QtCore
import controller
import controller as c
#Importamos el constructor de la clase generada automáticamente
from form import Ui_Form
class Form(QtGui.QDialog):
    """clase que crea la ventana de ingreso de empleados"""
    def __init__(self, parent=None, rut=None):
        """constructor que crea la ventana de ingreso de empleados"""
        QtGui.QDialog.__init__(self, parent)
        self.ui =  Ui_Form()
        self.ui.setupUi(self)
	if rut is None:
	    self.ui.comboBox.addItem("Masculino","Masculino")
	    self.ui.comboBox.addItem("Femenino","Femenino")
        else:
            datos_empleado = controller.obtener_empleado_por_rut(rut)
	    self.ui.rut_bar.setText(str(datos_empleado[0][0]))
	    self.ui.rut_bar.setReadOnly(True)
	    self.ui.nombre_bar.setText(datos_empleado[0][1])
            self.ui.cargo_bar.setText(datos_empleado[0][2])
            self.ui.sueldo_bar.setText(datos_empleado[0][4])
	    self.ui.local_bar.setText(str(datos_empleado[0][5]))
	    if(datos_empleado[0][3]=="Masculino"):
		self.ui.comboBox.addItem("Masculino","Masculino")
		self.ui.comboBox.addItem("Femenino","Femenino")
            else:
		self.ui.comboBox.addItem("Femenino","Femenino")
		self.ui.comboBox.addItem("Masculino","Masculino")		  

        self.ui.cancel_btn.clicked.connect(self.cancel)
	self.show()

    def add(self):
        """función que crea el ingreso de empleados"""
	genero = self.ui.comboBox.itemData(self.ui.comboBox.currentIndex())	
	if(self.ui.rut_bar.text()!="" and self.ui.nombre_bar.text()!="" and self.ui.cargo_bar.text()!=""
		and self.ui.sueldo_bar.text()!=""):        
	   	try:
			int(self.ui.rut_bar.text())
			res = controller.agregar_empleado(int(self.ui.rut_bar.text()),self.ui.nombre_bar.text(),self.ui.cargo_bar.text(),
            			genero,self.ui.sueldo_bar.text(),self.ui.local_bar.text())
			if res:
	   			self.reject()
            			msgBox = QtGui.QMessageBox.information(self,"Exito","El empleado fue agregado.")
			else:
           			msgBox = QtGui.QMessageBox.critical(self,"Error","No se pudo agregar el empleado.")

		except:
			msgBox = QtGui.QMessageBox.information(self,"Error","ingrese el rut sin puntos ni guion")
	else:
		msgBox = QtGui.QMessageBox.information(self,"Error","ingrese todos los campos de informacion")    	
	

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
        """ventana que permite la cancelación de la ventana"""
        self.reject()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    main = Form()
    sys.exit(app.exec_())
