#!/usr/bin/env python
import asyncio
import sys
from PyQt5 import QtWidgets, QtGui
from main_app.GUI.main_gui import Ui_MainWindow

class MainWindow(Ui_MainWindow):
    def __init__(self, dialog):
        Ui_MainWindow.__init__(self)
        self.setupUi(dialog)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.label_picture.setPixmap(QtGui.QPixmap("main_app/src/images/carbonFootprint.jpg"))
    MainWindow.show()
    sys.exit(app.exec_())
