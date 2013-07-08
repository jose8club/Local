#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

from PySide import QtGui, QtCore
import controller
import controller_local
from main_locales import Ui_MainWindow
from local import Ui_Local
import view_productos_form


class Locales(QtGui.QWidget):

    first_time = True
    marca_actual = "*"
    s = "%"

    def __init__(self):
        super(Locales, self).__init__()
        self.ui = Ui_MainWindow()
	self.ui.setupUi(self)
	self.load_productos()
	self.setup_search_bar()
	self.setup_combo_marcas()	
	#self.load_marcas()
	self.set_listeners()
	self.show()
