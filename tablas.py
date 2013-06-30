#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import controller
import view_form

from empleados import Ui_MainWindow
from PySide import QtGui, QtCore



class Main(QtGui.QWidget):
	def __init__(self):
		"""Documento de la clase main"""
		super(Main, self).__init__()
		self.resize(900, 600)
		self.layout = QtGui.QVBoxLayout(self)
		self.layouts()
		self.tables()
		#self.datos()
		#self.signals()
		self.show()

	def layouts(self):
		self.l = QtGui.QWidget(self)
		self.hl = QtGui.QHBoxLayout()
		self.hl.setAlignment(QtCore.Qt.AlignRight)
		self.l.setLayout(self.hl)
		##botones y combobox y filtro
		self.label = QtGui.QLabel(u"Ciudad")
		self.filtro = QtGui.QLineEdit()
		self.combo = QtGui.QComboBox(self)
		#self.combo.activated[int].connect(self.onActivated)
		self.b1 = QtGui.QPushButton(u"&Buscar")
		self.b3 = QtGui.QPushButton(u"&Eliminar local")
		self.hl.addWidget(self.label)
		self.hl.addWidget(self.filtro)
		self.hl.addWidget(self.combo)
		self.hl.addWidget(self.b1)
		
		self.hl.addWidget(self.b3)
		##agreagar este layout al vertical
		self.layout.addWidget(self.l)

	def tables(self):
		self.table = QtGui.QTableWidget(self)
		
		self.table.setFixedWidth(890)
		self.table.setFixedHeight(480)
		self.table.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
		self.table.setAlternatingRowColors(True)
		self.table.setSortingEnabled(True)

		self.layout.addWidget(self.table)

	def signals(self):
		self.b1.clicked.connect(self.create)
		self.b3.clicked.connect(self.borrar)

	def borrar(self):
		modelo = self.table.model()
		index = self.table.currentIndex()
		if index.row() == -1: #No se ha seleccionado una fila
			self.errorMessageDialog = QtGui.QErrorMessage(self)
			self.errorMessageDialog.showMessage("Debe seleccionar una fila")
			return False
	
	# Metodo para agregar empleado en la ventana de Locales, este debe ir en la clase "Locales" asumo yo.
	def Add_Empleado(self): 
		#Abre la ventana "Form" del empleado
		form = view_form.Form(self)
        	form.rejected.connect(self.datos)
        	form.exec_()

		#Enlaza el boton con el metodo agregar (add).
		form.ui.add_btn.clicked.connect(form.add)

		form.rejected.connect(self.datos)
		form.exec_()
        
         # Este boton deberia abrir la ventana Locales
	 # def create(self): 
	




def run():
	app = QtGui.QApplication(sys.argv)
	main = Main()
	sys.exit(app.exec_())

if __name__ == '__main__':
	run()



