#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PySide import QtGui, QtCore
import controller as c

import empleados_form
#Importamos el constructor de la clase generada automáticamente
from empleados_ui import Ui_Dialog
class Form(QtGui.QDialog):
	def __init__(self, parent=None, id_local=None):
		QtGui.QDialog.__init__(self, parent)
		self.ui =  Ui_Dialog()
		self.ui.setupUi(self)
		self.ui.agregar.clicked.connect(self.conectar)
		self.ui.eliminar.clicked.connect(self.eliminar)
		self.datos(id_local)
		self.show()

	def conectar(self):
		form = empleados_form.Form(self)
		form.exec_()

	def datos(self, id_local):
		empleados = c.obtener_empleados_por_local(id_local)
		#print empleados
		#Creamos el modelo asociado a la tabla
		self.model = QtGui.QStandardItemModel(len(empleados), 6)
		self.model.setHorizontalHeaderItem(0, QtGui.QStandardItem(u"RUT"))
		self.model.setHorizontalHeaderItem(1, QtGui.QStandardItem(u"Nombre"))
		self.model.setHorizontalHeaderItem(2, QtGui.QStandardItem(u"Cargo"))
		self.model.setHorizontalHeaderItem(3, QtGui.QStandardItem(u"Genero"))
		self.model.setHorizontalHeaderItem(4, QtGui.QStandardItem(u"Sueldo"))
		self.model.setHorizontalHeaderItem(5, QtGui.QStandardItem(u"local"))

		r = 0
		for row in empleados:
			#print row
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
			index = self.model.index(r, 5, QtCore.QModelIndex())
			self.model.setData(index, row[5])
			r = r+1
		self.ui.tableView.setModel(self.model)

		self.ui.tableView.setColumnWidth(0, 120)
		self.ui.tableView.setColumnWidth(1, 120)
		self.ui.tableView.setColumnWidth(2, 120)
		self.ui.tableView.setColumnWidth(3, 120)
		self.ui.tableView.setColumnWidth(4, 120)
		self.ui.tableView.setColumnWidth(5, 120)


	def eliminar(self):
		model = self.ui.tableView.model()
		index = self.ui.tableView.currentIndex()
		if index.row() == -1: #No se ha seleccionado una fila
			self.ui.errorMessageDialog = QtGui.QErrorMessage(self)
			self.ui.errorMessageDialog.showMessage("Debe seleccionar una fila")
			return False
		else:
			rut = model.index(index.row(), 0, QtCore.QModelIndex()).data()
			id_local = model.index(index.row(), 5, QtCore.QModelIndex()).data()
			if (c.eliminar_empleado(rut)):
				self.datos(id_local)
				msgBox = QtGui.QMessageBox()
				msgBox.setText("EL empleado de este local fue eliminado.")
				msgBox.exec_()
				return True
			else:
				self.ui.errorMessageDialog = QtGui.QErrorMessage(self)
				self.ui.errorMessageDialog.showMessage("Error al eliminar el registro del empleado de este local")
				return False



if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	main = Form()
	sys.exit(app.exec_())

