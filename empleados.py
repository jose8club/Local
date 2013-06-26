# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'empleados.ui'
#
# Created: Mon Jun 24 22:55:00 2013
#      by: pyside-uic 0.2.13 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 20, 731, 521))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.agregar = QtGui.QPushButton(self.verticalLayoutWidget)
        self.agregar.setObjectName("agregar")
        self.horizontalLayout.addWidget(self.agregar)
        self.eliminar = QtGui.QPushButton(self.verticalLayoutWidget)
        self.eliminar.setObjectName("eliminar")
        self.horizontalLayout.addWidget(self.eliminar)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.tableView = QtGui.QTableView(self.verticalLayoutWidget)
        self.tableView.setObjectName("tableView")
        self.horizontalLayout_3.addWidget(self.tableView)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.aceptar = QtGui.QPushButton(self.verticalLayoutWidget)
        self.aceptar.setObjectName("aceptar")
        self.horizontalLayout_2.addWidget(self.aceptar)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.agregar.setText(QtGui.QApplication.translate("MainWindow", "Agregar empleado", None, QtGui.QApplication.UnicodeUTF8))
        self.eliminar.setText(QtGui.QApplication.translate("MainWindow", "Eliminar empleado", None, QtGui.QApplication.UnicodeUTF8))
        self.aceptar.setText(QtGui.QApplication.translate("MainWindow", "Aceptar", None, QtGui.QApplication.UnicodeUTF8))

