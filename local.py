# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'local.ui'
#
# Created: Thu Jul  4 11:49:19 2013
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Local(object):
    def setupUi(self, Local):
        Local.setObjectName(_fromUtf8("Local"))
        Local.resize(369, 312)
        Local.setMinimumSize(QtCore.QSize(369, 312))
        Local.setMaximumSize(QtCore.QSize(369, 312))
        self.centralwidget = QtGui.QWidget(Local)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.lineNombre = QtGui.QLineEdit(self.centralwidget)
        self.lineNombre.setGeometry(QtCore.QRect(190, 40, 113, 27))
        self.lineNombre.setObjectName(_fromUtf8("lineNombre"))
        self.lineDireccion = QtGui.QLineEdit(self.centralwidget)
        self.lineDireccion.setGeometry(QtCore.QRect(190, 90, 113, 27))
        self.lineDireccion.setObjectName(_fromUtf8("lineDireccion"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 40, 66, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 90, 66, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.lineCiudad = QtGui.QLineEdit(self.centralwidget)
        self.lineCiudad.setGeometry(QtCore.QRect(190, 140, 113, 27))
        self.lineCiudad.setObjectName(_fromUtf8("lineCiudad"))
        self.pushAceptar = QtGui.QPushButton(self.centralwidget)
        self.pushAceptar.setGeometry(QtCore.QRect(50, 220, 98, 27))
        self.pushAceptar.setObjectName(_fromUtf8("pushAceptar"))
        self.pushSalir = QtGui.QPushButton(self.centralwidget)
        self.pushSalir.setGeometry(QtCore.QRect(220, 220, 98, 27))
        self.pushSalir.setObjectName(_fromUtf8("pushSalir"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 150, 66, 17))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        Local.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Local)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 369, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        Local.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Local)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Local.setStatusBar(self.statusbar)

        self.retranslateUi(Local)
        QtCore.QMetaObject.connectSlotsByName(Local)

    def retranslateUi(self, Local):
        Local.setWindowTitle(QtGui.QApplication.translate("Local", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Local", "Nombre", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Local", "Direccion", None, QtGui.QApplication.UnicodeUTF8))
        self.pushAceptar.setText(QtGui.QApplication.translate("Local", "Aceptar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushSalir.setText(QtGui.QApplication.translate("Local", "Salir", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Local", "Ciudad", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Local = QtGui.QMainWindow()
    ui = Ui_Local()
    ui.setupUi(Local)
    Local.show()
    sys.exit(app.exec_())

