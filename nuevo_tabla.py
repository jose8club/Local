# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'nuevo_tabla.ui'
#
# Created: Thu Jul  4 12:17:38 2013
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(900, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.filtro = QtGui.QLineEdit(self.centralwidget)
        self.filtro.setGeometry(QtCore.QRect(80, 30, 471, 27))
        self.filtro.setObjectName(_fromUtf8("filtro"))
        self.combo = QtGui.QComboBox(self.centralwidget)
        self.combo.setGeometry(QtCore.QRect(570, 30, 78, 27))
        self.combo.setObjectName(_fromUtf8("combo"))
        self.b1 = QtGui.QPushButton(self.centralwidget)
        self.b1.setGeometry(QtCore.QRect(680, 30, 98, 27))
        self.b1.setObjectName(_fromUtf8("b1"))
        self.b3 = QtGui.QPushButton(self.centralwidget)
        self.b3.setGeometry(QtCore.QRect(790, 30, 101, 27))
        self.b3.setObjectName(_fromUtf8("b3"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 30, 66, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.pushSalir = QtGui.QPushButton(self.centralwidget)
        self.pushSalir.setGeometry(QtCore.QRect(697, 520, 181, 27))
        self.pushSalir.setObjectName(_fromUtf8("pushSalir"))
        self.table = QtGui.QListView(self.centralwidget)
        self.table.setGeometry(QtCore.QRect(9, 80, 880, 430))
        self.table.setObjectName(_fromUtf8("table"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.b1.setText(QtGui.QApplication.translate("MainWindow", "Buscar", None, QtGui.QApplication.UnicodeUTF8))
        self.b3.setText(QtGui.QApplication.translate("MainWindow", "Eliminar Local", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Ciudad", None, QtGui.QApplication.UnicodeUTF8))
        self.pushSalir.setText(QtGui.QApplication.translate("MainWindow", "Salir", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

