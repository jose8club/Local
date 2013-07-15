# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created: Mon Jul 15 05:43:46 2013
#      by: pyside-uic 0.2.13 running on PySide 1.1.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(313, 300)
        self.rut_bar = QtGui.QLineEdit(Form)
        self.rut_bar.setGeometry(QtCore.QRect(100, 20, 191, 27))
        self.rut_bar.setObjectName("rut_bar")
        self.codigo_label = QtGui.QLabel(Form)
        self.codigo_label.setGeometry(QtCore.QRect(10, 20, 71, 21))
        self.codigo_label.setObjectName("codigo_label")
        self.nombre_bar = QtGui.QLineEdit(Form)
        self.nombre_bar.setGeometry(QtCore.QRect(100, 60, 191, 27))
        self.nombre_bar.setObjectName("nombre_bar")
        self.nombre_label = QtGui.QLabel(Form)
        self.nombre_label.setGeometry(QtCore.QRect(10, 60, 71, 21))
        self.nombre_label.setObjectName("nombre_label")
        self.cargo_bar = QtGui.QLineEdit(Form)
        self.cargo_bar.setGeometry(QtCore.QRect(100, 100, 191, 27))
        self.cargo_bar.setObjectName("cargo_bar")
        self.cargo_label = QtGui.QLabel(Form)
        self.cargo_label.setGeometry(QtCore.QRect(10, 100, 81, 21))
        self.cargo_label.setObjectName("cargo_label")
        self.genero_label = QtGui.QLabel(Form)
        self.genero_label.setGeometry(QtCore.QRect(10, 140, 71, 21))
        self.genero_label.setObjectName("genero_label")
        self.sueldo_bar = QtGui.QLineEdit(Form)
        self.sueldo_bar.setGeometry(QtCore.QRect(100, 180, 191, 27))
        self.sueldo_bar.setObjectName("sueldo_bar")
        self.sueldo_label = QtGui.QLabel(Form)
        self.sueldo_label.setGeometry(QtCore.QRect(10, 180, 71, 21))
        self.sueldo_label.setObjectName("sueldo_label")
        self.add_btn = QtGui.QPushButton(Form)
        self.add_btn.setGeometry(QtCore.QRect(40, 260, 111, 27))
        self.add_btn.setObjectName("add_btn")
        self.cancel_btn = QtGui.QPushButton(Form)
        self.cancel_btn.setGeometry(QtCore.QRect(160, 260, 111, 27))
        self.cancel_btn.setObjectName("cancel_btn")
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 220, 66, 17))
        self.label.setObjectName("label")
        self.local_bar = QtGui.QLineEdit(Form)
        self.local_bar.setEnabled(False)
        self.local_bar.setGeometry(QtCore.QRect(100, 220, 191, 27))
        self.local_bar.setObjectName("local_bar")
        self.comboBox = QtGui.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(100, 140, 131, 27))
        self.comboBox.setObjectName("comboBox")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.codigo_label.setText(QtGui.QApplication.translate("Form", "Rut", None, QtGui.QApplication.UnicodeUTF8))
        self.nombre_label.setText(QtGui.QApplication.translate("Form", "Nombre:", None, QtGui.QApplication.UnicodeUTF8))
        self.cargo_label.setText(QtGui.QApplication.translate("Form", "Cargo", None, QtGui.QApplication.UnicodeUTF8))
        self.genero_label.setText(QtGui.QApplication.translate("Form", "Genero", None, QtGui.QApplication.UnicodeUTF8))
        self.sueldo_label.setText(QtGui.QApplication.translate("Form", "Sueldo", None, QtGui.QApplication.UnicodeUTF8))
        self.add_btn.setText(QtGui.QApplication.translate("Form", "Agregar", None, QtGui.QApplication.UnicodeUTF8))
        self.cancel_btn.setText(QtGui.QApplication.translate("Form", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Local", None, QtGui.QApplication.UnicodeUTF8))

