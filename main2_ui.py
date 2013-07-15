# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main2.ui'
#
# Created: Mon Jul 15 05:11:04 2013
#      by: pyside-uic 0.2.13 running on PySide 1.1.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_window(object):
    def setupUi(self, window):
        window.setObjectName("window")
        window.resize(945, 548)
        window.setWindowTitle("MainWindow")
        self.widget = QtGui.QWidget(window)
        self.widget.setObjectName("widget")
        self.combo = QtGui.QComboBox(self.widget)
        self.combo.setGeometry(QtCore.QRect(780, 40, 151, 27))
        self.combo.setObjectName("combo")
        self.local_label = QtGui.QLabel(self.widget)
        self.local_label.setGeometry(QtCore.QRect(600, 40, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.local_label.setFont(font)
        self.local_label.setObjectName("local_label")
        self.filtro = QtGui.QLineEdit(self.widget)
        self.filtro.setGeometry(QtCore.QRect(120, 40, 441, 27))
        self.filtro.setAccessibleName("")
        self.filtro.setAccessibleDescription("")
        self.filtro.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.filtro.setInputMask("")
        self.filtro.setText("")
        self.filtro.setObjectName("filtro")
        self.table_win = QtGui.QTableView(self.widget)
        self.table_win.setEnabled(True)
        self.table_win.setGeometry(QtCore.QRect(10, 80, 935, 361))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.table_win.sizePolicy().hasHeightForWidth())
        self.table_win.setSizePolicy(sizePolicy)
        self.table_win.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.table_win.setObjectName("table_win")
        self.crear_btn = QtGui.QPushButton(self.widget)
        self.crear_btn.setGeometry(QtCore.QRect(10, 460, 111, 27))
        self.crear_btn.setObjectName("crear_btn")
        self.eliminar_btn = QtGui.QPushButton(self.widget)
        self.eliminar_btn.setGeometry(QtCore.QRect(830, 460, 101, 27))
        self.eliminar_btn.setObjectName("eliminar_btn")
        self.edit_button = QtGui.QPushButton(self.widget)
        self.edit_button.setGeometry(QtCore.QRect(180, 460, 101, 27))
        self.edit_button.setObjectName("edit_button")
        self.label = QtGui.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(10, 45, 111, 17))
        self.label.setObjectName("label")
        window.setCentralWidget(self.widget)
        self.menubar = QtGui.QMenuBar(window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 945, 25))
        self.menubar.setObjectName("menubar")
        window.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(window)
        self.statusbar.setObjectName("statusbar")
        window.setStatusBar(self.statusbar)

        self.retranslateUi(window)
        QtCore.QMetaObject.connectSlotsByName(window)

    def retranslateUi(self, window):
        self.local_label.setText(QtGui.QApplication.translate("window", "Seleccione una Ciudad", None, QtGui.QApplication.UnicodeUTF8))
        self.filtro.setToolTip(QtGui.QApplication.translate("window", "<html><head/><body><p>Buscar...</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.filtro.setWhatsThis(QtGui.QApplication.translate("window", "<html><head/><body><p><br/></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.filtro.setPlaceholderText(QtGui.QApplication.translate("window", "Ingrese aquí el nombre del Local", None, QtGui.QApplication.UnicodeUTF8))
        self.crear_btn.setText(QtGui.QApplication.translate("window", "Agregar Local", None, QtGui.QApplication.UnicodeUTF8))
        self.eliminar_btn.setText(QtGui.QApplication.translate("window", "Eliminar", None, QtGui.QApplication.UnicodeUTF8))
        self.edit_button.setText(QtGui.QApplication.translate("window", "Editar", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("window", "Nombre Local", None, QtGui.QApplication.UnicodeUTF8))

