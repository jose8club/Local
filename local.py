# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'local.ui'
#
# Created: Sun Jul  7 22:55:29 2013
#      by: pyside-uic 0.2.13 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Local(object):
    def setupUi(self, Local):
        Local.setObjectName("Local")
        Local.resize(369, 312)
        Local.setMinimumSize(QtCore.QSize(369, 312))
        Local.setMaximumSize(QtCore.QSize(369, 312))
        self.centralwidget = QtGui.QWidget(Local)
        self.centralwidget.setObjectName("centralwidget")
        self.lineNombre = QtGui.QLineEdit(self.centralwidget)
        self.lineNombre.setGeometry(QtCore.QRect(190, 50, 113, 27))
        self.lineNombre.setObjectName("lineNombre")
        self.lineDireccion = QtGui.QLineEdit(self.centralwidget)
        self.lineDireccion.setGeometry(QtCore.QRect(190, 90, 113, 27))
        self.lineDireccion.setObjectName("lineDireccion")
        self.nombre_label = QtGui.QLabel(self.centralwidget)
        self.nombre_label.setGeometry(QtCore.QRect(60, 50, 66, 17))
        self.nombre_label.setObjectName("nombre_label")
        self.direccion_label = QtGui.QLabel(self.centralwidget)
        self.direccion_label.setGeometry(QtCore.QRect(60, 90, 66, 17))
        self.direccion_label.setObjectName("direccion_label")
        self.lineCiudad = QtGui.QLineEdit(self.centralwidget)
        self.lineCiudad.setGeometry(QtCore.QRect(190, 170, 113, 27))
        self.lineCiudad.setObjectName("lineCiudad")
        self.pushAceptar = QtGui.QPushButton(self.centralwidget)
        self.pushAceptar.setGeometry(QtCore.QRect(50, 220, 98, 27))
        self.pushAceptar.setObjectName("pushAceptar")
        self.pushSalir = QtGui.QPushButton(self.centralwidget)
        self.pushSalir.setGeometry(QtCore.QRect(220, 220, 98, 27))
        self.pushSalir.setObjectName("pushSalir")
        self.ciudad_label = QtGui.QLabel(self.centralwidget)
        self.ciudad_label.setGeometry(QtCore.QRect(60, 170, 66, 17))
        self.ciudad_label.setObjectName("ciudad_label")
        self.empleados_label = QtGui.QLabel(self.centralwidget)
        self.empleados_label.setGeometry(QtCore.QRect(60, 130, 81, 17))
        self.empleados_label.setObjectName("empleados_label")
        self.lineEmpleados = QtGui.QLineEdit(self.centralwidget)
        self.lineEmpleados.setGeometry(QtCore.QRect(190, 130, 113, 27))
        self.lineEmpleados.setObjectName("lineEmpleados")
        self.id_label = QtGui.QLabel(self.centralwidget)
        self.id_label.setGeometry(QtCore.QRect(60, 10, 66, 17))
        self.id_label.setObjectName("id_label")
        self.id_local = QtGui.QLineEdit(self.centralwidget)
        self.id_local.setGeometry(QtCore.QRect(190, 10, 113, 27))
        self.id_local.setObjectName("id_local")
        Local.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Local)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 369, 25))
        self.menubar.setObjectName("menubar")
        Local.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Local)
        self.statusbar.setObjectName("statusbar")
        Local.setStatusBar(self.statusbar)

        self.retranslateUi(Local)
        QtCore.QMetaObject.connectSlotsByName(Local)

    def retranslateUi(self, Local):
        Local.setWindowTitle(QtGui.QApplication.translate("Local", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.nombre_label.setText(QtGui.QApplication.translate("Local", "Nombre", None, QtGui.QApplication.UnicodeUTF8))
        self.direccion_label.setText(QtGui.QApplication.translate("Local", "Direccion", None, QtGui.QApplication.UnicodeUTF8))
        self.pushAceptar.setText(QtGui.QApplication.translate("Local", "Aceptar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushSalir.setText(QtGui.QApplication.translate("Local", "Salir", None, QtGui.QApplication.UnicodeUTF8))
        self.ciudad_label.setText(QtGui.QApplication.translate("Local", "Ciudad", None, QtGui.QApplication.UnicodeUTF8))
        self.empleados_label.setText(QtGui.QApplication.translate("Local", "Empleados", None, QtGui.QApplication.UnicodeUTF8))
        self.id_label.setText(QtGui.QApplication.translate("Local", "Id_local", None, QtGui.QApplication.UnicodeUTF8))

