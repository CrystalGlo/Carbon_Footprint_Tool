from PyQt5 import QtCore, QtGui, QtWidgets

from main_app.data import carbon
from main_app.src.footprintController import Utility
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
import math
from PIL import Image
from main_app.GUI.carbon_gui import Ui_GesWindow

class Ui_MainWindow(object):
    def __init__(self):
        self.utility = Utility()
        self.bank_statement = ""
        self.ges_statement = ""
        self.total_ges = ""
        self.year = ""

    def getBankStatement(self):
        return self.bank_statement

    def getGesStatement(self):
        return self.ges_statement

    def readFile(self):
        fileName = QtWidgets.QFileDialog.getOpenFileName()
        if fileName != '':
            self.bank_statement = self.utility.read_file(fileName)
            self.calculateCarbonEmission()

    def calculateCarbonEmission(self):
        bank_statement = self.getBankStatement()
        self.ges_statement = self.utility.calculate_carbon(bank_statement)
        self.total_ges = self.utility.calculate_total(self.ges_statement)
        self.year = self.utility.get_statement_year()
        self.btn_show.setEnabled(True)

    def openStatementsWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_GesWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        bank_statement = self.getBankStatement()
        ges_statement = self.getGesStatement()
        i = 0
        for val in bank_statement:
            self.ui.tableWidget_bank.setRowCount(i+1)
            self.ui.tableWidget_bank.setItem(i, 0, QtWidgets.QTableWidgetItem(str(val[0]).strip()))
            self.ui.tableWidget_bank.setItem(i, 1, QtWidgets.QTableWidgetItem(str(val[1]).strip() + ' $'))
            self.ui.tableWidget_bank.setItem(i, 2, QtWidgets.QTableWidgetItem(str(val[2]).strip()))
            i = i + 1
        j = 0
        for val in ges_statement:
            self.ui.tableWidget_carbon.setRowCount(j+1)
            self.ui.tableWidget_carbon.setItem(j, 0,QtWidgets.QTableWidgetItem(str(val[0]).strip()))
            self.ui.tableWidget_carbon.setItem(j, 1, QtWidgets.QTableWidgetItem(str(val[1])+ ' Kg CO2'))
            self.ui.tableWidget_carbon.setItem(j, 2, QtWidgets.QTableWidgetItem(str(val[2]).strip()))
            j = j + 1
        self.createGesGauge(self.total_ges)
        self.ui.label_gauge.setPixmap(QtGui.QPixmap("main_app/src/images/jauge.png"))
        self.ui.label_year.setText("Année: " + str(self.year))
        self.ui.label_totalGES.setText("Total GES: " + str(self.total_ges))

    def createGesGauge(self, totalGES):
        dial_colors = np.linspace(0, 1, 60)
        figname = 'jauge'
        arrow_index = totalGES / 2
        labels = [' '] * len(dial_colors) * 2
        labels[1] = '2000'
        labels[15] = '1500'
        labels[30] = '1000'
        labels[45] = '500'
        labels[59] = '0'
        fig, ax = plt.subplots()
        Ui_MainWindow.dial(dial_colors, arrow_index, labels, ax)
        ax.set_aspect('equal')
        plt.savefig('main_app/src/images/' + figname + '.png', bbox_inches='tight', transparent=True)
        im = Image.open('main_app/src/images/' + figname + '.png')
        width, height = im.size
        im = im.crop((0, 0, width, int(height / 2.0))).save('main_app/src/images/' + figname + '.png')

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 692)
        MainWindow.setStyleSheet("selection-background-color: rgb(144, 214, 106);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("font: 11pt \"Arial\";")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout_picture = QtWidgets.QGridLayout()
        self.gridLayout_picture.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout_picture.setObjectName("gridLayout_picture")
        self.label_picture = QtWidgets.QLabel(self.centralwidget)
        self.label_picture.setText("")
        self.label_picture.setPixmap(QtGui.QPixmap("../src/images/carbonFootprint.jpg"))
        self.label_picture.setObjectName("label_picture")
        self.gridLayout_picture.addWidget(self.label_picture, 0, 0, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_picture, 1, 2, 1, 1)
        self.gridLayout_table = QtWidgets.QGridLayout()
        self.gridLayout_table.setObjectName("gridLayout_table")
        self.frame_table = QtWidgets.QFrame(self.centralwidget)
        self.frame_table.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_table.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_table.setObjectName("frame_table")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_table)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tableWidget = QtWidgets.QTableWidget(self.frame_table)
        self.tableWidget.setMaximumSize(QtCore.QSize(2000, 2000))
        self.tableWidget.setAutoFillBackground(True)
        self.tableWidget.setStyleSheet("")
        self.tableWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tableWidget.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tableWidget.setLineWidth(1)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(QtCore.Qt.DashLine)
        self.tableWidget.setWordWrap(False)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(50)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget.verticalHeader().setDefaultSectionSize(30)
        self.horizontalLayout_2.addWidget(self.tableWidget)
        self.gridLayout_table.addWidget(self.frame_table, 0, 0, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_table, 1, 0, 1, 2)
        self.gridLayout_buttons = QtWidgets.QGridLayout()
        self.gridLayout_buttons.setObjectName("gridLayout_buttons")
        self.frame_buttons = QtWidgets.QFrame(self.centralwidget)
        self.frame_buttons.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.frame_buttons.setStyleSheet("font: 75 bold 8pt \"Arial\";\n"
"background-color: rgb(0, 147, 0);")
        self.frame_buttons.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_buttons.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_buttons.setObjectName("frame_buttons")
        self.btn_import = QtWidgets.QPushButton(self.frame_buttons)
        self.btn_import.setGeometry(QtCore.QRect(170, 0, 212, 31))
        self.btn_import.setStyleSheet("background-color: rgb(225, 225, 225);")
        self.btn_import.setObjectName("btn_import")
        self.btn_import.clicked.connect(self.readFile)
        self.btn_show = QtWidgets.QPushButton(self.frame_buttons)
        self.btn_show.setGeometry(QtCore.QRect(450, 0, 221, 31))
        self.btn_show.setStyleSheet("background-color: rgb(225, 225, 225);")
        self.btn_show.setObjectName("btn_show")
        self.btn_show.clicked.connect(self.openStatementsWindow)
        self.btn_show.setEnabled(False)
        self.gridLayout_buttons.addWidget(self.frame_buttons, 1, 0, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_buttons, 0, 2, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.frame_title = QtWidgets.QFrame(self.centralwidget)
        self.frame_title.setStyleSheet("background-color: rgb(0, 118, 0);\n"
"\n"
"")
        self.frame_title.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_title.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_title.setObjectName("frame_title")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_title)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_title = QtWidgets.QLabel(self.frame_title)
        self.label_title.setStyleSheet("font: 75 bold 12pt \"Arial\";\n"
"color: rgb(234, 234, 234);\n"
"")
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setObjectName("label_title")
        self.horizontalLayout.addWidget(self.label_title)
        self.gridLayout.addWidget(self.frame_title, 1, 0, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout, 0, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menu_bankStatement = QtWidgets.QMenu(self.menuFile)
        self.menu_bankStatement.setObjectName("menu_bankStatement")
        self.menu_gesStatement = QtWidgets.QMenu(self.menuFile)
        self.menu_gesStatement.setObjectName("menu_gesStatement")
        self.menu_help = QtWidgets.QMenu(self.menubar)
        self.menu_help.setObjectName("menu_help")
        self.menu_data = QtWidgets.QMenu(self.menubar)
        self.menu_data.setObjectName("menu_data")
        MainWindow.setMenuBar(self.menubar)
        self.menuBtn_showList = QtWidgets.QAction(MainWindow)
        self.menuBtn_showList.setObjectName("menuBtn_showList")
        self.menuBtn_save = QtWidgets.QAction(MainWindow)
        self.menuBtn_save.setObjectName("menuBtn_save")
        self.menuBtn_export = QtWidgets.QAction(MainWindow)
        self.menuBtn_export.setObjectName("menuBtn_export")
        self.menuBtn_save_2 = QtWidgets.QAction(MainWindow)
        self.menuBtn_save_2.setObjectName("menuBtn_save_2")
        self.menuBtn_print = QtWidgets.QAction(MainWindow)
        self.menuBtn_print.setObjectName("menuBtn_print")
        self.menuBtn_quit = QtWidgets.QAction(MainWindow)
        self.menuBtn_quit.setObjectName("menuBtn_quit")
        self.menuBtn_documentation = QtWidgets.QAction(MainWindow)
        self.menuBtn_documentation.setObjectName("menuBtn_documentation")
        self.menuBtn_about = QtWidgets.QAction(MainWindow)
        self.menuBtn_about.setObjectName("menuBtn_about")
        self.menuBtn_showPanorama = QtWidgets.QAction(MainWindow)
        self.menuBtn_showPanorama.setObjectName("menuBtn_showPanorama")
        self.menuBtn_savePanorama = QtWidgets.QAction(MainWindow)
        self.menuBtn_savePanorama.setObjectName("menuBtn_savePanorama")
        self.menu_bankStatement.addAction(self.menuBtn_save)
        self.menu_bankStatement.addSeparator()
        self.menu_bankStatement.addAction(self.menuBtn_showList)
        self.menu_gesStatement.addAction(self.menuBtn_export)
        self.menu_gesStatement.addSeparator()
        self.menu_gesStatement.addAction(self.menuBtn_save_2)
        self.menu_gesStatement.addSeparator()
        self.menu_gesStatement.addAction(self.menuBtn_print)
        self.menuFile.addAction(self.menu_bankStatement.menuAction())
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.menu_gesStatement.menuAction())
        self.menuFile.addSeparator()
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.menuBtn_quit)
        self.menu_help.addAction(self.menuBtn_documentation)
        self.menu_help.addSeparator()
        self.menu_help.addAction(self.menuBtn_about)
        self.menu_data.addAction(self.menuBtn_showPanorama)
        self.menu_data.addSeparator()
        self.menu_data.addAction(self.menuBtn_savePanorama)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menu_data.menuAction())
        self.menubar.addAction(self.menu_help.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Carbon Footprint Tool"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Catégorie"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Émission de GES (Kg)"))
        gesDict = carbon.get_carbon_value()
        i = 0
        for key, val in gesDict.items():
            self.tableWidget.setRowCount(i+1)
            self.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(key))
            self.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(str(val)))
            i = i+1

        self.btn_import.setText(_translate("MainWindow", "Importer relevé bancaire"))
        self.btn_show.setText(_translate("MainWindow", "Afficher relevé de GES"))
        self.label_title.setText(_translate("MainWindow", "Empreinte de l\'émission de GES"))
        self.menuFile.setTitle(_translate("MainWindow", "Fichier"))
        self.menu_bankStatement.setTitle(_translate("MainWindow", "Relevé bancaire"))
        self.menu_gesStatement.setTitle(_translate("MainWindow", "Relevé de l\'émission de GES"))
        self.menu_help.setTitle(_translate("MainWindow", "Aide"))
        self.menu_data.setTitle(_translate("MainWindow", "Données"))
        self.menuBtn_showList.setText(_translate("MainWindow", "Afficher la liste"))
        self.menuBtn_save.setText(_translate("MainWindow", "Enregistrer"))
        self.menuBtn_export.setText(_translate("MainWindow", "Exporter"))
        self.menuBtn_save_2.setText(_translate("MainWindow", "Enregistrer"))
        self.menuBtn_print.setText(_translate("MainWindow", "Imprimer"))
        self.menuBtn_quit.setText(_translate("MainWindow", "Quitter"))
        self.menuBtn_documentation.setText(_translate("MainWindow", "Documentation"))
        self.menuBtn_about.setText(_translate("MainWindow", "À propos du logiciel"))
        self.menuBtn_showPanorama.setText(_translate("MainWindow", "Panorama des données"))
        self.menuBtn_savePanorama.setText(_translate("MainWindow", "Enregistrer panorama"))

    def dial(color_array, arrow_index, labels, ax):
        size_of_groups = np.ones(len(color_array) * 2)
        white_half = np.ones(len(color_array)) * .5
        color_half = color_array
        color_pallet = np.concatenate([color_half, white_half])
        cs = cm.RdYlGn(color_pallet)
        pie_wedge_collection = ax.pie(size_of_groups, colors=cs, labels=labels)
        i = 0
        for pie_wedge in pie_wedge_collection[0]:
            pie_wedge.set_edgecolor(cm.RdYlGn(color_pallet[i]))
            i = i + 1
        my_circle = plt.Circle((0, 0), 0.3, color='white')
        ax.add_artist(my_circle)
        #When you reach max, dont go around
        if arrow_index > 1000:
            arrow_index = 1000
        arrow_angle = (arrow_index * 0.06 / float(len(color_array))) * math.pi
        arrow_x = math.cos(arrow_angle)
        arrow_y = math.sin(arrow_angle)
        ax.arrow(0, 0, -arrow_x, arrow_y, width=.02, head_width=.05, \
                 head_length=.1, fc='k', ec='k')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


