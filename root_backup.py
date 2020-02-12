
# Form implementation generated from reading ui file 'NT.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

import PyQt5
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QWidget, QMessageBox, QFileDialog, QApplication, QTableWidgetItem
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import webbrowser


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 577)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget_database = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_database.setGeometry(QtCore.QRect(10, 40, 691, 161))
        self.tableWidget_database.setLineWidth(1)
        self.tableWidget_database.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget_database.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget_database.setRowCount(10)
        self.tableWidget_database.setColumnCount(6)
        self.tableWidget_database.setObjectName("tableWidget_database")
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_database.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_database.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_database.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_database.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_database.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_database.setHorizontalHeaderItem(5, item)
        self.tableWidget_database.verticalHeader().setCascadingSectionResizes(False)
        self.label_database = QtWidgets.QLabel(self.centralwidget)
        self.label_database.setGeometry(QtCore.QRect(10, 0, 101, 31))
        self.label_database.setObjectName("label_database")
        self.tableWidget_entry = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_entry.setGeometry(QtCore.QRect(10, 310, 691, 171))
        self.tableWidget_entry.setRowCount(0)
        self.tableWidget_entry.setColumnCount(7)
        self.tableWidget_entry.setObjectName("tableWidget_entry")
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_entry.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_entry.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_entry.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_entry.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_entry.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_entry.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_entry.setHorizontalHeaderItem(6, item)
        self.pushButton_add = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_add.setGeometry(QtCore.QRect(310, 500, 81, 31))
        self.pushButton_add.setObjectName("pushButton_add")
        self.pushButton_entry_AddNewEntry = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_entry_AddNewEntry.setGeometry(QtCore.QRect(370, 270, 101, 31))
        self.pushButton_entry_AddNewEntry.setObjectName("pushButton_entry_AddNewEntry")
        self.pushButton_database_AddNewEntry = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_database_AddNewEntry.setGeometry(QtCore.QRect(40, 210, 91, 31))
        self.pushButton_database_AddNewEntry.setObjectName("pushButton_database_AddNewEntry")
        self.pushButton_database_Delete = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_database_Delete.setGeometry(QtCore.QRect(140, 210, 111, 31))
        self.pushButton_database_Delete.setObjectName("pushButton_database_Delete")
        self.comboBox_pickfood = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_pickfood.setGeometry(QtCore.QRect(20, 270, 111, 31))
        self.comboBox_pickfood.setObjectName("comboBox_pickfood")
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(260, 270, 110, 31))
        self.dateEdit.setObjectName("dateEdit")
        self.comboBox_meal = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_meal.setGeometry(QtCore.QRect(140, 270, 111, 31))
        self.comboBox_meal.setObjectName("comboBox_meal")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.tableWidget_database.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Food Name"))
        item = self.tableWidget_database.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Calories"))
        item = self.tableWidget_database.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Carbs"))
        item = self.tableWidget_database.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Fat"))
        item = self.tableWidget_database.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Protein"))
        item = self.tableWidget_database.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Fibre"))
        self.label_database.setText(_translate("MainWindow", "Database (Editable)"))
        item = self.tableWidget_entry.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Food Name"))
        item = self.tableWidget_entry.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Calories"))
        item = self.tableWidget_entry.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Carbs"))
        item = self.tableWidget_entry.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Fat"))
        item = self.tableWidget_entry.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Protein"))
        item = self.tableWidget_entry.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Fibre"))
        item = self.tableWidget_entry.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Date"))
        self.pushButton_add.setText(_translate("MainWindow", "Save "))
        self.pushButton_entry_AddNewEntry.setText(_translate("MainWindow", "Add New Entry"))
        self.pushButton_database_AddNewEntry.setText(_translate("MainWindow", "Add New Entry"))
        self.pushButton_database_Delete.setText(_translate("MainWindow", "Delete Selected Row"))




        self.printTOTable()
        self.tableWidget_database.cellChanged.connect(self.readTable)
        self.pushButton_entry_AddNewEntry.clicked.connect(self.NewItem)
        self.pushButton_database_AddNewEntry.clicked.connect(self.func_pushButton_database_AddNewEntry)
        str_meal = ['Breakfast' , 'Lunch' , 'Dinner' , 'Snacks']
        self.comboBox_pickfood.addItems(list(df['Food']))
        self.comboBox_meal.addItems(str_meal)
        self.pushButton_entry_AddNewEntry.clicked.connect(lambda: self.tableWidget_newentry(str(self.comboBox_pickfood.currentText()), str(self.comboBox_meal.currentText())))
        self.pushButton_database_Delete.clicked.connect(self.btn_pushButton_database_Delete)

    def btn_pushButton_database_Delete(self):
        try:
            indices = self.tableWidget_database.selectionModel().selectedRows()
            for index in sorted(indices, reverse=True):
                if index != 0:
                    self.tableWidget_database.removeRow(index.row())
                    self.readTable()
        except Exception as e:
            self.errMessage("Printing to Table:", str(e))

    def func_pushButton_database_AddNewEntry(self):
        self.tableWidget_database.setRowCount(self.tableWidget_database.rowCount()+1)
    def readTable(self):
        import pandas as pd
        try:
            global df
            tableDimensions = [int(self.tableWidget_database.rowCount()), int(self.tableWidget_database.columnCount())]
            df = pd.DataFrame({"Food": [],
                           "Calories": [],
                           "Carbs": [],
                           "Fat": [], "Protein": [], "Fibre": []})
            i = 0
            while i < tableDimensions[1]:
                j = 0
                while j < tableDimensions[0]:
                    a_item = self.tableWidget_database.item(j, i)
                    try:
                        a_name = str(a_item.text())
                    except:
                        a_name = str(np.single(0))
                    df.set_value(j,list(df)[i], a_name)
                    #df[i].loc[j] = a_name
                    j += 1
                i += 1
                self.comboBox_pickfood.clear()
                self.comboBox_pickfood.addItems(list(df['Food']))
                print(df)
        except Exception as e:
            self.errMessage("Reading Table:", str(e))

    def printTOTable(self):  # Prints data file to table
        import pandas as pd
        global df
        df = pd.DataFrame({"Food": ["Tea", "Egg", "Rotti"],
                           "Calories": [11, 212, 312],
                           "Carbs": [112, 2122, 3212],
                           "Fat": [11, 212, 321], "Protein": [11, 212, 321], "Fibre": [11, 212, 321]})
        try:
            i = 0
            for p in list(df):
                j = 0
                print(p)
                while j < df.shape[0]:
                    A = []
                    # ##print(data[j,i])
                    A = str(df[p].loc[j])
                    cellinfo = QTableWidgetItem(A)
                    self.tableWidget_database.setItem(j, i, cellinfo)
                    j += 1
                i += 1


        except Exception as e:
            self.errMessage("Printing to Table:", str(e))

    def onCellChanged(self):
        try:
            text = self.tableWidget_database.item(self.tableWidget_database.currentRow(), self.tableWidget_database.currentColumn()).text()
            text = str(text)
            df.set_value(self.tableWidget_database.currentRow(), list(df)[self.tableWidget_database.currentColumn()], text)
            print(df)
            self.comboBox_pickfood.clear()
            self.comboBox_pickfood.addItems(list(df['Food']))
        except Exception as e:
            self.errMessage("Printing to Table:", str(e))
    def NewItem(self):
        import pandas as pd
        df = pd.DataFrame({"Food": ["Tea", "Egg", "Rotti"],
                           "Calories": [11, 212, 312],
                           "Carbs": [112, 2122, 3212],
                           "Fat": [11, 212, 321], "Protein": [11, 212, 321], "Fibre": [11, 212, 321],
                           "Date": [11, 212, 321]})
    #    combo = QtWidgets.QComboBox()
     #   combo.addItems(list(df))
        # self.tableWidget.setItem(data.shape[1], data.shape[0], cellinfo)
     #   self.tableWidget_entry.setCellWidget(0, 0, combo)


    def tableWidget_newentry(self, food, meal):  # Prints data file to table
        temp_var = self.dateEdit.date()
        var_date = temp_var.toPyDate()
        self.tableWidget_entry.setRowCount(self.tableWidget_entry.rowCount()+1)
        A = str(var_date)
        cellinfo = QTableWidgetItem(A)
        self.tableWidget_entry.setItem(int(self.tableWidget_entry.rowCount() - 1), 6, cellinfo)
        try:
            j=0
            for p in list(df.loc[self.comboBox_pickfood.currentIndex()]):
          #      print(p)
                A = str(p)
                cellinfo = QTableWidgetItem(A)
                self.tableWidget_entry.setItem(int(self.tableWidget_entry.rowCount()-1), j, cellinfo)
                print(j)
                j += 1


        except Exception as e:
            self.errMessage("Printing to Table:", str(e))

    def errMessage(self, Text, InformativeText):
        msgBox = QMessageBox()
        msgBox.setWindowIcon(QtGui.QIcon('ico.ico'))
        msgBox.setWindowTitle("PhysPlot - Plot Window")
        msgBox.setIcon(QMessageBox.Critical)
        msgBox.setText(Text)
        msgBox.setInformativeText(InformativeText)
        msgBox.setWindowTitle("Warning")
        msgBox.exec_()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
