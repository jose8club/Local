#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PySide import QtGui, QtCore
import controller
#Importamos el constructor de la clase generada automáticamente
from form import Ui_Form
class Form(QtGui.QDialog):
    """clase que crea la ventana de ingreso de empleados"""
    def __init__(self, parent=None):
        """constructor que crea la ventana de ingreso de empleados"""
        QtGui.QDialog.__init__(self, parent)
        self.ui =  Ui_Form()
        self.ui.setupUi(self)
        self.show()
        #self.ui.cancel_btn.clicked.connect(self.cancel)
    

    def add(self):
        """función que crea el ingreso de empleados"""
        if self.ui.rut_bar.text() == "":
            msgBox = QtGui.QMessageBox.warning(self,"Error","Ingrese el rut del empleado.")
        elif self.ui.nombre_bar.text() == "":
            msgBox = QtGui.QMessageBox.warning(self,"Error","Ingrese un nombre del empleado.")
        elif self.ui.cargo_bar.text() == "":
            msgBox = QtGui.QMessageBox.warning(self,"Error","Ingrese el cargo.")
        elif self.ui.genero_bar.text() == "":
            msgBox = QtGui.QMessageBox.warning(self,"Error","Ingrese el genero F o M.")
        elif self.ui.sueldo_bar.text() == "":
            msgBox = QtGui.QMessageBox.warning(self,"Error","Ingrese el sueldo del empleado.")
        elif self.ui.local_bar.text() == "":
            msgBox = QtGui.QMessageBox.warning(self,"Error","Ingrese el codigo del local.")

        else:
            res = controller.agregar_empleado(self.ui.rut_bar.text(),self.ui.nombre_bar.text(),self.ui.cargo_bar.text(),
            self.ui.genero_bar.text(),self.ui.sueldo_bar.text(),self.ui.local_bar.text())
        if res:
            msgBox = QtGui.QMessageBox.information(self,"Exito","El registro fue agregado.")
            self.reject()
        else:
            msgBox = QtGui.QMessageBox.critical(self,"Error","No se pudo agregar el registro.")

    def cancel(self):
        """ventana que permite la cancelación de la ventana"""
        self.reject()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    main = Form()
    sys.exit(app.exec_())
