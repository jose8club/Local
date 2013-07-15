#!/usr/bin/python
# -*- coding: utf-8 -*-


from PySide import QtGui, QtCore
import controller_local
import controller as c
#Importamos el constructor de la clase generada automáticamente
from local2_ui import Ui_Form

class Form(QtGui.QDialog):
    """clase que crea la ventana de agregar locales"""
    def __init__(self, parent=None):
        """constructor de la ventana de agregar locales"""
        QtGui.QDialog.__init__(self, parent)
        self.ui =  Ui_Form()
        self.ui.setupUi(self)
	self.ui.PushSalir.clicked.connect(self.cancel)
	self.ui.PushAceptar.clicked.connect(self.edit)
        self.show()
        
    def add(self):
        """función que se llama para agregar locales"""
	if(self.ui.lineNombre.text()!="" and self.ui.lineDireccion.text()!="" and 
		self.ui.lineCiudad.text()!=""):
		id_ciudad = c.obtener_id_ciudad(self.ui.lineCiudad.text())
		if(id_ciudad!="null"):
			res = c.agregar_local(self.ui.lineNombre.text(),self.ui.lineDireccion.text(),id_ciudad) 
			if res:
			    msgBox = QtGui.QMessageBox.information(self,"Exito","El registro fue agregado.")
			    self.reject()
	       		else:
		    	    msgBox = QtGui.QMessageBox.critical(self,"Error","No se pudo agregar el registro.")
		else:
			msgBox = QtGui.QMessageBox.critical(self,"Error","Ingrese una ciudad valida")
	else:
		msgBox = QtGui.QMessageBox.critical(self,"Error","Ingrese todos los campos de informacion")

    def edit(self):
        """función que se llama para editar locales"""
	if(self.ui.lineNombre.text()!="" and self.ui.lineDireccion.text()!="" and 
		self.ui.lineCiudad.text()!=""):
		id_ciudad = c.obtener_id_ciudad(self.ui.lineCiudad.text())
		if(id_ciudad!="null"):
			res = c.editar_local(self.ui.idlocal.text(),self.ui.lineNombre.text(),self.ui.lineDireccion.text(),id_ciudad) 
			if res:
			    msgBox = QtGui.QMessageBox.information(self,"Exito","El registro fue agregado.")
			    self.reject()
	       		else:
		    	    msgBox = QtGui.QMessageBox.critical(self,"Error","No se pudo editar el registro.")
		else:
			msgBox = QtGui.QMessageBox.critical(self,"Error","Ingrese una ciudad valida")
	else:
		msgBox = QtGui.QMessageBox.critical(self,"Error","Ingrese todos los campos de informacion")

    def cancel(self):
        """función para cancelar el agregar un local nuevo"""
        self.reject()

