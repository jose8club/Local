# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'agregar.ui'
#
# Created: Mon Jun 24 23:17:54 2013
#      by: pyside-uic 0.2.13 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.verticalLayoutWidget = QtGui.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 351, 261))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.rutlabel = QtGui.QLabel(self.verticalLayoutWidget)
        self.rutlabel.setObjectName("rutlabel")
        self.horizontalLayout.addWidget(self.rutlabel)
        self.rut = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.rut.setObjectName("rut")
        self.horizontalLayout.addWidget(self.rut)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.nombrelabel = QtGui.QLabel(self.verticalLayoutWidget)
        self.nombrelabel.setObjectName("nombrelabel")
        self.horizontalLayout_2.addWidget(self.nombrelabel)
        self.nombre = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.nombre.setObjectName("nombre")
        self.horizontalLayout_2.addWidget(self.nombre)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.cargolabel = QtGui.QLabel(self.verticalLayoutWidget)
        self.cargolabel.setObjectName("cargolabel")
        self.horizontalLayout_3.addWidget(self.cargolabel)
        self.cargo = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.cargo.setObjectName("cargo")
        self.horizontalLayout_3.addWidget(self.cargo)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.sueldolabel = QtGui.QLabel(self.verticalLayoutWidget)
        self.sueldolabel.setObjectName("sueldolabel")
        self.horizontalLayout_4.addWidget(self.sueldolabel)
        self.sueldo = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.sueldo.setObjectName("sueldo")
        self.horizontalLayout_4.addWidget(self.sueldo)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.generolabel = QtGui.QLabel(self.verticalLayoutWidget)
        self.generolabel.setObjectName("generolabel")
        self.horizontalLayout_5.addWidget(self.generolabel)
        self.genero = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.genero.setObjectName("genero")
        self.horizontalLayout_5.addWidget(self.genero)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.pushButton = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_6.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.rutlabel.setText(QtGui.QApplication.translate("Dialog", "RUT", None, QtGui.QApplication.UnicodeUTF8))
        self.nombrelabel.setText(QtGui.QApplication.translate("Dialog", "Nombre", None, QtGui.QApplication.UnicodeUTF8))
        self.cargolabel.setText(QtGui.QApplication.translate("Dialog", "Cargo", None, QtGui.QApplication.UnicodeUTF8))
        self.sueldolabel.setText(QtGui.QApplication.translate("Dialog", "Sueldo", None, QtGui.QApplication.UnicodeUTF8))
        self.generolabel.setText(QtGui.QApplication.translate("Dialog", "Genero", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Dialog", "Aceptar", None, QtGui.QApplication.UnicodeUTF8))

