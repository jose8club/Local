#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PySide import QtGui, QtCore
import controller_local
#Importamos el constructor de la clase generada automáticamente
from local import Ui_Local
class Form(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.ui =  Ui_Local()
        self.ui.setupUi(self)
        self.show()
        #self.ui.btn_cancel.clicked.connect(self.cancel)
    

def add(self):
	if self.ui.id_local.text() == "":
		msgBox = QtGui.QMessageBox.warning(self,"Error","Ingrese el id del Local.")
	elif self.ui.lineNombre.text() == "":
		msgBox = QtGui.QMessageBox.warning(self,"Error","Ingrese el nombre Local.")
	elif self.ui.lineDireccion.text() == "":
		msgBox = QtGui.QMessageBox.warning(self,"Error","Ingrese direccion del Local.")
	elif self.ui.lineEmpleados.text() == "":
		msgBox = QtGui.QMessageBox.warning(self,"Error","Ingrese el numero de empleados inicial.")
	elif self.ui.lineCiudad.text() == "":
		msgBox = QtGui.QMessageBox.warning(self,"Error","Ingrese la ciudad.")
	
	else:
		res = controller_local.add_local(self.ui.id_local.text(),self.ui.lineNombre.text(),self.ui.lineDireccion.text(),self.ui.lineEmpleados.text(),self.ui.lineCiudad.text())
	if res:
		msgBox = QtGui.QMessageBox.information(self,"Exito","El registro fue agregado.")
		self.reject()
	else:
		msgBox = QtGui.QMessageBox.critical(self,"Error","No se pudo agregar el registro.")



def cancel(self):
	self.reject()

if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	main = Form()
	sys.exit(app.exec_())
