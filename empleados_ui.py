# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'empleados.ui'
#
# Created: Wed Jul  3 18:31:18 2013
#      by: pyside-uic 0.2.13 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(803, 581)
        self.verticalLayoutWidget = QtGui.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 20, 731, 521))
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

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.agregar.setText(QtGui.QApplication.translate("Dialog", "Agregar empleado", None, QtGui.QApplication.UnicodeUTF8))
        self.eliminar.setText(QtGui.QApplication.translate("Dialog", "Eliminar empleado", None, QtGui.QApplication.UnicodeUTF8))
        self.aceptar.setText(QtGui.QApplication.translate("Dialog", "Aceptar", None, QtGui.QApplication.UnicodeUTF8))

