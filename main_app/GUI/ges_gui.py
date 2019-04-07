# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ges_gui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_GesWindow(object):
    def setupUi(self, GesWindow):
        GesWindow.setObjectName("GesWindow")
        GesWindow.resize(755, 640)
        self.centralwidget = QtWidgets.QWidget(GesWindow)
        self.centralwidget.setStyleSheet("font: 9pt \"Arial\";")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_gauge = QtWidgets.QFrame(self.centralwidget)
        self.frame_gauge.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_gauge.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_gauge.setObjectName("frame_gauge")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_gauge)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_year = QtWidgets.QLabel(self.frame_gauge)
        self.label_year.setStyleSheet("font: 75 Bold 9pt \"MS Shell Dlg 2\";")
        self.label_year.setObjectName("label_year")
        self.gridLayout_3.addWidget(self.label_year, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_gauge = QtWidgets.QLabel(self.frame_gauge)
        self.label_gauge.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_gauge.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_gauge.setText("")
        self.label_gauge.setPixmap(QtGui.QPixmap("../src/images/jauge.png"))
        self.label_gauge.setObjectName("label_gauge")
        self.gridLayout_3.addWidget(self.label_gauge, 1, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_totalGES = QtWidgets.QLabel(self.frame_gauge)
        self.label_totalGES.setStyleSheet("font: 75 Bold 9pt \"MS Shell Dlg 2\";")
        self.label_totalGES.setObjectName("label_totalGES")
        self.gridLayout_3.addWidget(self.label_totalGES, 2, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.gridLayout.addWidget(self.frame_gauge, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_bank = QtWidgets.QFrame(self.centralwidget)
        self.frame_bank.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_bank.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_bank.setObjectName("frame_bank")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_bank)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.frame_bank)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("font: 75 Bold 10pt \"MS Shell Dlg 2\";\n"
"text-decoration: underline;")
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        #self.textBrowser_bank = QtWidgets.QTextBrowser(self.frame_bank)

        self.textBrowser_bank = QtWidgets.QTableWidget(self.frame_bank)
        self.textBrowser_bank.setColumnCount(3)
        self.textBrowser_bank.setRowCount(45)


        self.textBrowser_bank.setObjectName("textBrowser_bank")
        self.verticalLayout.addWidget(self.textBrowser_bank)
        self.horizontalLayout.addWidget(self.frame_bank)
        self.frame_ges = QtWidgets.QFrame(self.centralwidget)
        self.frame_ges.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_ges.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_ges.setObjectName("frame_ges")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_ges)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.frame_ges)
        self.label_2.setStyleSheet("font: 75 Bold 10pt \"MS Shell Dlg 2\";\n"
"text-decoration: underline;")
        self.label_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        #self.textBrowser_ges = QtWidgets.QTextBrowser(self.frame_ges)

        self.textBrowser_ges = QtWidgets.QTableWidget(self.frame_ges)
        self.textBrowser_ges.setColumnCount(4)
        self.textBrowser_ges.setRowCount(45)

        self.textBrowser_ges.setObjectName("textBrowser_ges")
        self.verticalLayout_2.addWidget(self.textBrowser_ges)
        self.horizontalLayout.addWidget(self.frame_ges)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        GesWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(GesWindow)
        QtCore.QMetaObject.connectSlotsByName(GesWindow)

    def retranslateUi(self, GesWindow):
        _translate = QtCore.QCoreApplication.translate
        GesWindow.setWindowTitle(_translate("GesWindow", "Relevé des émissions GES"))
        self.label_year.setText(_translate("GesWindow", "2018"))
        self.label_totalGES.setText(_translate("GesWindow", "1355"))
        self.label.setText(_translate("GesWindow", "Relevé bancaire"))
        self.label_2.setText(_translate("GesWindow", "Relevé des émissions en GES"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    GesWindow = QtWidgets.QMainWindow()
    ui = Ui_GesWindow()
    ui.setupUi(GesWindow)
    GesWindow.show()
    sys.exit(app.exec_())

