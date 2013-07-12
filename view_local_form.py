#!/usr/bin/python
# -*- coding: utf-8 -*-


from PySide import QtGui, QtCore
import controller_local
#Importamos el constructor de la clase generada automáticamente
from local2_ui import Ui_Form

class Form(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.ui =  Ui_Form()
        self.ui.setupUi(self)
        self.show()
        self.ui.PushSalir.clicked.connect(self.cancel)
    

    def add(self):
        if self.ui.lineNombre.text() == "":
            msgBox = QtGui.QMessageBox.warning(self,"Error","Ingrese el nombre Local.")
        elif self.ui.lineDireccion.text() == "":
            msgBox = QtGui.QMessageBox.warning(self,"Error","Ingrese direccion del Local.")
        elif self.ui.lineCiudad.text() == "":
            msgBox = QtGui.QMessageBox.warning(self,"Error","Ingrese la ciudad.")
    
        else:
            res = controller_local.add_local(self.ui.lineNombre.text(),self.ui.lineDireccion.text(),self.ui.lineCiudad.text())
        if res:
            msgBox = QtGui.QMessageBox.information(self,"Exito","El registro fue agregado.")
            self.reject()
        else:
            msgBox = QtGui.QMessageBox.critical(self,"Error","No se pudo agregar el registro.")



    def cancel(self):
        self.reject()

