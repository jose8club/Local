# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'local2.ui'
#
# Created: Mon Jul 15 18:29:28 2013
#      by: pyside-uic 0.2.13 running on PySide 1.1.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(378, 214)
        self.lineNombre = QtGui.QLineEdit(Form)
        self.lineNombre.setGeometry(QtCore.QRect(110, 30, 241, 27))
        self.lineNombre.setObjectName("lineNombre")
        self.nombre_label = QtGui.QLabel(Form)
        self.nombre_label.setGeometry(QtCore.QRect(20, 30, 71, 21))
        self.nombre_label.setObjectName("nombre_label")
        self.lineDireccion = QtGui.QLineEdit(Form)
        self.lineDireccion.setGeometry(QtCore.QRect(110, 70, 241, 27))
        self.lineDireccion.setObjectName("lineDireccion")
        self.direccion_label = QtGui.QLabel(Form)
        self.direccion_label.setGeometry(QtCore.QRect(20, 70, 81, 21))
        self.direccion_label.setObjectName("direccion_label")
        self.lineCiudad = QtGui.QLineEdit(Form)
        self.lineCiudad.setGeometry(QtCore.QRect(110, 110, 241, 27))
        self.lineCiudad.setObjectName("lineCiudad")
        self.ciudad_label = QtGui.QLabel(Form)
        self.ciudad_label.setGeometry(QtCore.QRect(20, 110, 71, 21))
        self.ciudad_label.setObjectName("ciudad_label")
        self.PushAceptar = QtGui.QPushButton(Form)
        self.PushAceptar.setGeometry(QtCore.QRect(110, 160, 111, 27))
        self.PushAceptar.setObjectName("PushAceptar")
        self.PushSalir = QtGui.QPushButton(Form)
        self.PushSalir.setGeometry(QtCore.QRect(230, 160, 111, 27))
        self.PushSalir.setObjectName("PushSalir")
        self.idlocal = QtGui.QLabel(Form)
        self.idlocal.setEnabled(False)
        self.idlocal.setGeometry(QtCore.QRect(331, 10, 20, 20))
        self.idlocal.setText("")
        self.idlocal.setObjectName("idlocal")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.nombre_label.setText(QtGui.QApplication.translate("Form", "Nombre:", None, QtGui.QApplication.UnicodeUTF8))
        self.direccion_label.setText(QtGui.QApplication.translate("Form", "Direccion", None, QtGui.QApplication.UnicodeUTF8))
        self.ciudad_label.setText(QtGui.QApplication.translate("Form", "Ciudad", None, QtGui.QApplication.UnicodeUTF8))
        self.PushAceptar.setText(QtGui.QApplication.translate("Form", "Aceptar", None, QtGui.QApplication.UnicodeUTF8))
        self.PushSalir.setText(QtGui.QApplication.translate("Form", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))

