# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'local2.ui'
#
# Created: Wed Jul 10 18:47:01 2013
#      by: pyside-uic 0.2.13 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(368, 312)
        self.id_local = QtGui.QLineEdit(Form)
        self.id_local.setGeometry(QtCore.QRect(120, 20, 191, 27))
        self.id_local.setObjectName("id_local")
        self.codigo_label = QtGui.QLabel(Form)
        self.codigo_label.setGeometry(QtCore.QRect(10, 20, 71, 21))
        self.codigo_label.setObjectName("codigo_label")
        self.lineNombre = QtGui.QLineEdit(Form)
        self.lineNombre.setGeometry(QtCore.QRect(120, 60, 191, 27))
        self.lineNombre.setObjectName("lineNombre")
        self.nombre_label = QtGui.QLabel(Form)
        self.nombre_label.setGeometry(QtCore.QRect(10, 60, 71, 21))
        self.nombre_label.setObjectName("nombre_label")
        self.lineDireccion = QtGui.QLineEdit(Form)
        self.lineDireccion.setGeometry(QtCore.QRect(120, 100, 191, 27))
        self.lineDireccion.setObjectName("lineDireccion")
        self.direccion_label = QtGui.QLabel(Form)
        self.direccion_label.setGeometry(QtCore.QRect(10, 100, 81, 21))
        self.direccion_label.setObjectName("direccion_label")
        self.lineEmpleados = QtGui.QLineEdit(Form)
        self.lineEmpleados.setGeometry(QtCore.QRect(120, 140, 191, 27))
        self.lineEmpleados.setObjectName("lineEmpleados")
        self.empleados_label = QtGui.QLabel(Form)
        self.empleados_label.setGeometry(QtCore.QRect(10, 140, 81, 21))
        self.empleados_label.setObjectName("empleados_label")
        self.lineCiudad = QtGui.QLineEdit(Form)
        self.lineCiudad.setGeometry(QtCore.QRect(120, 180, 191, 27))
        self.lineCiudad.setObjectName("lineCiudad")
        self.ciudad_label = QtGui.QLabel(Form)
        self.ciudad_label.setGeometry(QtCore.QRect(10, 180, 71, 21))
        self.ciudad_label.setObjectName("ciudad_label")
        self.PushAceptar = QtGui.QPushButton(Form)
        self.PushAceptar.setGeometry(QtCore.QRect(60, 240, 111, 27))
        self.PushAceptar.setObjectName("PushAceptar")
        self.PushSalir = QtGui.QPushButton(Form)
        self.PushSalir.setGeometry(QtCore.QRect(180, 240, 111, 27))
        self.PushSalir.setObjectName("PushSalir")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.codigo_label.setText(QtGui.QApplication.translate("Form", "Id_local", None, QtGui.QApplication.UnicodeUTF8))
        self.nombre_label.setText(QtGui.QApplication.translate("Form", "Nombre:", None, QtGui.QApplication.UnicodeUTF8))
        self.direccion_label.setText(QtGui.QApplication.translate("Form", "Direccion", None, QtGui.QApplication.UnicodeUTF8))
        self.empleados_label.setText(QtGui.QApplication.translate("Form", "Empleados", None, QtGui.QApplication.UnicodeUTF8))
        self.ciudad_label.setText(QtGui.QApplication.translate("Form", "Ciudad", None, QtGui.QApplication.UnicodeUTF8))
        self.PushAceptar.setText(QtGui.QApplication.translate("Form", "Agregar", None, QtGui.QApplication.UnicodeUTF8))
        self.PushSalir.setText(QtGui.QApplication.translate("Form", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))

