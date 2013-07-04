#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PySide import QtGui, QtCore
import controller

import view_form
#Importamos el constructor de la clase generada automáticamente
from empleados import Ui_Dialog
class Form(QtGui.QDialog):
	def __init__(self, parent=None):
		QtGui.QDialog.__init__(self, parent)
		self.ui =  Ui_Dialog()
		self.ui.setupUi(self)
		self.ui.agregar.clicked.connect(self.conectar)
		self.show()

	def conectar(self):
		form = view_form.Form(self)
		form.exec_()

if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	main = Form()
	sys.exit(app.exec_())