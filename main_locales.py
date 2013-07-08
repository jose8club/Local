# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'nuevo_tabla.ui'
#
# Created: Sun Jul  7 19:11:49 2013
#      by: pyside-uic 0.2.13 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.filtro = QtGui.QLineEdit(self.centralwidget)
        self.filtro.setGeometry(QtCore.QRect(80, 30, 351, 27))
        self.filtro.setObjectName("filtro")
        self.combo = QtGui.QComboBox(self.centralwidget)
        self.combo.setGeometry(QtCore.QRect(450, 30, 78, 27))
        self.combo.setObjectName("combo")
        self.buscar_btn = QtGui.QPushButton(self.centralwidget)
        self.buscar_btn.setGeometry(QtCore.QRect(540, 30, 98, 27))
        self.buscar_btn.setObjectName("buscar_btn")
        self.eliminar_btn = QtGui.QPushButton(self.centralwidget)
        self.eliminar_btn.setGeometry(QtCore.QRect(780, 30, 101, 27))
        self.eliminar_btn.setObjectName("eliminar_btn")
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 30, 66, 17))
        self.label.setObjectName("label")
        self.pushSalir = QtGui.QPushButton(self.centralwidget)
        self.pushSalir.setGeometry(QtCore.QRect(697, 520, 181, 27))
        self.pushSalir.setObjectName("pushSalir")
        self.table = QtGui.QListView(self.centralwidget)
        self.table.setGeometry(QtCore.QRect(9, 80, 880, 430))
        self.table.setObjectName("table")
        self.crear_btn = QtGui.QPushButton(self.centralwidget)
        self.crear_btn.setGeometry(QtCore.QRect(660, 30, 98, 27))
        self.crear_btn.setObjectName("crear_btn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.buscar_btn.setText(QtGui.QApplication.translate("MainWindow", "Buscar", None, QtGui.QApplication.UnicodeUTF8))
        self.eliminar_btn.setText(QtGui.QApplication.translate("MainWindow", "Eliminar Local", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Ciudad", None, QtGui.QApplication.UnicodeUTF8))
        self.pushSalir.setText(QtGui.QApplication.translate("MainWindow", "Salir", None, QtGui.QApplication.UnicodeUTF8))
        self.crear_btn.setText(QtGui.QApplication.translate("MainWindow", "Crear Local", None, QtGui.QApplication.UnicodeUTF8))

