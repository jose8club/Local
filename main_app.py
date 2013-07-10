#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PySide import QtGui, QtCore

from form import Ui_Form

import empleados_grid
import controller_locales as c

class Main(QtGui.QWidget):
	def __init__(self):
		"""Documento de la clase main"""
		super(Main, self).__init__()
		self.resize(900, 600)
		self.layout = QtGui.QVBoxLayout(self)
		self.layouts()
		self.tables()
		#self.datos()
		self.signals()
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
		box = c.obtener_ciudades()
		for element in box:
			self.combo.addItem(element["nombre"])
		self.combo.activated[int].connect(self.Activado)
		self.b2 = QtGui.QPushButton(u"&Crear local")
		self.b1 = QtGui.QPushButton(u"&Buscar")
		self.b3 = QtGui.QPushButton(u"&Eliminar local")
		self.hl.addWidget(self.label)
		self.hl.addWidget(self.filtro)
		self.hl.addWidget(self.combo)
		self.hl.addWidget(self.b1)
		self.hl.addWidget(self.b2)
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
	def create(self): 
		#Abre la ventana "Form" del empleado
		form = empleados_grid.Form(self)
		form.exec_()
		
		#self.datos()
		 # Este boton deberia abrir la ventana Locales
	def Activado(self, index):
		
		
		id_ciudad = self.combo.itemData(index)
		nombre_empleados = self.combo.itemText(index)
		empleados = c.obtener_locales_por_ciudad(id_ciudad)

		self.model = QtGui.QStandardItemModel(len(empleados), 6)
		self.model.setHorizontalHeaderItem(0, QtGui.QStandardItem(u"id_local"))
		self.model.setHorizontalHeaderItem(1, QtGui.QStandardItem(u"Nombre"))
		self.model.setHorizontalHeaderItem(2, QtGui.QStandardItem(u"direccion"))
		self.model.setHorizontalHeaderItem(3, QtGui.QStandardItem(u"empleados"))
		self.model.setHorizontalHeaderItem(4, QtGui.QStandardItem(u"fk_id_ciudad"))
		



		r = 0
		for row in empleados:
			print row
			index = self.model.index(r, 0, QtCore.QModelIndex()) 
			self.model.setData(index, row[0])
			index = self.model.index(r, 1, QtCore.QModelIndex()) 
			self.model.setData(index, row[1])
			index = self.model.index(r, 2, QtCore.QModelIndex()) 
			self.model.setData(index, row[2])
			index = self.model.index(r, 3, QtCore.QModelIndex())
			self.model.setData(index, row[3])
			index = self.model.index(r, 4, QtCore.QModelIndex())
			self.model.setData(index, row[4])
			
			r = r+1
		self.table.setModel(self.model)

		self.table.setColumnWidth(0, 120)
		self.table.setColumnWidth(1, 120)
		self.table.setColumnWidth(2, 120)
		self.table.setColumnWidth(3, 120)
		self.table.setColumnWidth(4, 120)
		self.table.setColumnWidth(5, 120)

def run():
	app = QtGui.QApplication(sys.argv)
	main = Main()
	sys.exit(app.exec_())

if __name__ == '__main__':
	run()



