
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QWidget, QMessageBox, QFileDialog, QApplication, QTableWidgetItem

import numpy as np
class Ui_Dialog_Config(object):
    def setupUi(self, Dialog_Config):
        Dialog_Config.setObjectName("Dialog_Config")
        Dialog_Config.resize(357, 258)
        self.gridLayout = QtWidgets.QGridLayout(Dialog_Config)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(Dialog_Config)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(Dialog_Config)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.label_7 = QtWidgets.QLabel(Dialog_Config)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_2.addWidget(self.label_7)
        self.label_3 = QtWidgets.QLabel(Dialog_Config)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(Dialog_Config)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(Dialog_Config)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(Dialog_Config)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit_Name = QtWidgets.QLineEdit(Dialog_Config)
        self.lineEdit_Name.setObjectName("lineEdit_Name")
        self.verticalLayout.addWidget(self.lineEdit_Name)
        self.comboBox_Activity_2 = QtWidgets.QComboBox(Dialog_Config)
        self.comboBox_Activity_2.setObjectName("comboBox_Activity_2")
        self.comboBox_Activity_2.addItem("")
        self.comboBox_Activity_2.addItem("")
        self.verticalLayout.addWidget(self.comboBox_Activity_2)
        self.lineEdit_Age = QtWidgets.QLineEdit(Dialog_Config)
        self.lineEdit_Age.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)
        self.lineEdit_Age.setObjectName("lineEdit_Age")
        self.verticalLayout.addWidget(self.lineEdit_Age)
        self.lineEdit_Height = QtWidgets.QLineEdit(Dialog_Config)
        self.lineEdit_Height.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)
        self.lineEdit_Height.setObjectName("lineEdit_Height")
        self.verticalLayout.addWidget(self.lineEdit_Height)
        self.lineEdit_Mass = QtWidgets.QLineEdit(Dialog_Config)
        self.lineEdit_Mass.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)
        self.lineEdit_Mass.setObjectName("lineEdit_Mass")
        self.verticalLayout.addWidget(self.lineEdit_Mass)
        self.comboBox_Activity = QtWidgets.QComboBox(Dialog_Config)
        self.comboBox_Activity.setObjectName("comboBox_Activity")
        self.comboBox_Activity.addItem("")
        self.comboBox_Activity.addItem("")
        self.comboBox_Activity.addItem("")
        self.comboBox_Activity.addItem("")
        self.comboBox_Activity.addItem("")
        self.verticalLayout.addWidget(self.comboBox_Activity)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.pushButton_OK = QtWidgets.QPushButton(Dialog_Config)
        self.pushButton_OK.setObjectName("pushButton_OK")
        self.gridLayout.addWidget(self.pushButton_OK, 2, 0, 1, 1)

        self.retranslateUi(Dialog_Config)
        QtCore.QMetaObject.connectSlotsByName(Dialog_Config)

    def retranslateUi(self, Dialog_Config):
        _translate = QtCore.QCoreApplication.translate
        Dialog_Config.setWindowTitle(_translate("Dialog_Config", "Dialog"))
        self.label.setText(_translate("Dialog_Config", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Welcome to Calorie Counter</span></p></body></html>"))
        self.label_2.setText(_translate("Dialog_Config", "Name:"))
        self.label_7.setText(_translate("Dialog_Config", "Gender"))
        self.label_3.setText(_translate("Dialog_Config", "Age:"))
        self.label_4.setText(_translate("Dialog_Config", "Height:"))
        self.label_5.setText(_translate("Dialog_Config", "Initial Mass:"))
        self.label_6.setText(_translate("Dialog_Config", "Activity Level:"))
        self.comboBox_Activity_2.setItemText(0, _translate("Dialog_Config", "Male"))
        self.comboBox_Activity_2.setItemText(1, _translate("Dialog_Config", "Female"))
        self.comboBox_Activity.setItemText(0, _translate("Dialog_Config", "Sedentary (Little or No Exercise)"))
        self.comboBox_Activity.setItemText(1, _translate("Dialog_Config", "Lightly Active (Light Exercise/Sports 1-3 Days/Week)"))
        self.comboBox_Activity.setItemText(2, _translate("Dialog_Config", "Moderately Active (Moderate Exercise/Sports 3-5 Days/Week)"))
        self.comboBox_Activity.setItemText(3, _translate("Dialog_Config", "Very Active (Hard Exercise/Sports 6-7 Days a Week)"))
        self.comboBox_Activity.setItemText(4, _translate("Dialog_Config", "Extra Active (Very Hard Exercise/Sports & Physical Job or 2x training)"))
        self.pushButton_OK.setText(_translate("Dialog_Config", "OK"))



        self.pushButton_OK.clicked.connect(lambda: self.BMR(self.comboBox_Activity_2.currentText(), self.lineEdit_Name.text(), float(self.lineEdit_Age.text()), float(self.lineEdit_Height.text()),float(self.lineEdit_Mass.text()),self.comboBox_Activity.currentText()))
    def BMR(self,Gender, Name, Age, Height, Mass, Activity):
        try:
            global BMR
            if Gender == "Male":
                BMR = 66 + (6.3 * Mass) + (12.9 * Height) - (6.8 * Age)
            if Gender == "Female":
                BMR = 65.5 + (4.3 * Mass) + (4.7 * Height) - (4.7 * Age)
            self.CalorieCalculation()
            self.NewProfileWrite(Gender, Name, Age, Height, Mass, Activity,ReqCalorie)
        except Exception as e:
            self.errMessage("Reading Table:", str(e))
    def NewProfileWrite(self,Gender1, Name1, Age1, Height1, Mass1, Activity1,ReqCalorie1):
        outF = open("Config", "w")
        outF.write(str(Gender1) + "\n")
        outF.write(str(Name1) + "\n")
        outF.write(str(Age1) + "\n")
        outF.write(str(Height1) + "\n")
        outF.write(str(Mass1) + "\n")
        outF.write(str(Activity1) + "\n")
        outF.write(str(ReqCalorie1) + "\n")
        outF.close()
    def CalorieCalculation(self):
        global ReqCalorie
        if self.comboBox_Activity.currentIndex()==0:
            ReqCalorie = BMR * 1.2
        if self.comboBox_Activity.currentIndex() == 1:
            ReqCalorie = BMR * 1.375
        if self.comboBox_Activity.currentIndex() == 2:
            ReqCalorie = BMR * 1.55
        if self.comboBox_Activity.currentIndex() == 3:
            ReqCalorie = BMR * 1.725
        if self.comboBox_Activity.currentIndex() == 4:
            ReqCalorie = BMR * 1.9
        return ReqCalorie


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(562, 644)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_profile = QtWidgets.QLabel(self.centralwidget)
        self.label_profile.setObjectName("label_profile")
        self.gridLayout_2.addWidget(self.label_profile, 0, 1, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_TrackMeal = QtWidgets.QWidget()
        self.tab_TrackMeal.setObjectName("tab_TrackMeal")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tab_TrackMeal)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.groupBox = QtWidgets.QGroupBox(self.tab_TrackMeal)
        self.groupBox.setMinimumSize(QtCore.QSize(262, 192))
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_12 = QtWidgets.QLabel(self.groupBox)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_5.addWidget(self.label_12)
        self.lineEdit_Goal_3 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_Goal_3.setObjectName("lineEdit_Goal_3")
        self.horizontalLayout_5.addWidget(self.lineEdit_Goal_3)
        self.gridLayout.addLayout(self.horizontalLayout_5, 0, 0, 1, 2)
        self.line_2 = QtWidgets.QFrame(self.groupBox)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 1, 0, 1, 2)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_PickFood = QtWidgets.QLabel(self.groupBox)
        self.label_PickFood.setObjectName("label_PickFood")
        self.horizontalLayout.addWidget(self.label_PickFood)
        self.comboBox_pickfood = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_pickfood.setMinimumSize(QtCore.QSize(79, 0))
        self.comboBox_pickfood.setObjectName("comboBox_pickfood")
        self.horizontalLayout.addWidget(self.comboBox_pickfood)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.dateEdit = QtWidgets.QDateEdit(self.groupBox)
        self.dateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2020, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName("dateEdit")
        self.horizontalLayout_4.addWidget(self.dateEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_8.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.line = QtWidgets.QFrame(self.groupBox)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_3.addWidget(self.line)
        self.label_MealCategory = QtWidgets.QLabel(self.groupBox)
        self.label_MealCategory.setObjectName("label_MealCategory")
        self.horizontalLayout_3.addWidget(self.label_MealCategory)
        self.comboBox_meal = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_meal.setMinimumSize(QtCore.QSize(59, 0))
        self.comboBox_meal.setObjectName("comboBox_meal")
        self.horizontalLayout_3.addWidget(self.comboBox_meal)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.pushButton_entry_AddNewEntry = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_entry_AddNewEntry.setObjectName("pushButton_entry_AddNewEntry")
        self.verticalLayout_3.addWidget(self.pushButton_entry_AddNewEntry)
        self.horizontalLayout_8.addLayout(self.verticalLayout_3)
        self.gridLayout.addLayout(self.horizontalLayout_8, 2, 0, 1, 2)
        self.line_3 = QtWidgets.QFrame(self.groupBox)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout.addWidget(self.line_3, 3, 0, 1, 2)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_13 = QtWidgets.QLabel(self.groupBox)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_10.addWidget(self.label_13)
        self.lineEdit_TotalIntake = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_TotalIntake.setMinimumSize(QtCore.QSize(9, 0))
        self.lineEdit_TotalIntake.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)
        self.lineEdit_TotalIntake.setReadOnly(True)
        self.lineEdit_TotalIntake.setObjectName("lineEdit_TotalIntake")
        self.horizontalLayout_10.addWidget(self.lineEdit_TotalIntake)
        self.verticalLayout_4.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_15 = QtWidgets.QLabel(self.groupBox)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_12.addWidget(self.label_15)
        self.lineEdit_NetCalories = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_NetCalories.setMinimumSize(QtCore.QSize(19, 0))
        self.lineEdit_NetCalories.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)
        self.lineEdit_NetCalories.setReadOnly(True)
        self.lineEdit_NetCalories.setObjectName("lineEdit_NetCalories")
        self.horizontalLayout_12.addWidget(self.lineEdit_NetCalories)
        self.verticalLayout_4.addLayout(self.horizontalLayout_12)
        self.gridLayout.addLayout(self.verticalLayout_4, 4, 0, 1, 1)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_14 = QtWidgets.QLabel(self.groupBox)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_11.addWidget(self.label_14)
        self.lineEdit_Exercise = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_Exercise.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)
        self.lineEdit_Exercise.setObjectName("lineEdit_Exercise")
        self.horizontalLayout_11.addWidget(self.lineEdit_Exercise)
        self.verticalLayout_5.addLayout(self.horizontalLayout_11)
        self.pushButton_Save = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_Save.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.pushButton_Save.setObjectName("pushButton_Save")
        self.verticalLayout_5.addWidget(self.pushButton_Save)
        self.gridLayout.addLayout(self.verticalLayout_5, 4, 1, 1, 1)
        self.gridLayout_6.addWidget(self.groupBox, 0, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.MplWidget = MplWidget(self.tab_TrackMeal)
        self.MplWidget.setMinimumSize(QtCore.QSize(250, 230))
        self.MplWidget.setObjectName("MplWidget")
        self.verticalLayout.addWidget(self.MplWidget)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.radioButton_Breakfast = QtWidgets.QRadioButton(self.tab_TrackMeal)
        self.radioButton_Breakfast.setMaximumSize(QtCore.QSize(16777215, 17))
        self.radioButton_Breakfast.setObjectName("radioButton_Breakfast")
        self.horizontalLayout_2.addWidget(self.radioButton_Breakfast)
        self.radioButton_Lunch = QtWidgets.QRadioButton(self.tab_TrackMeal)
        self.radioButton_Lunch.setObjectName("radioButton_Lunch")
        self.horizontalLayout_2.addWidget(self.radioButton_Lunch)
        self.radioButton_Dinner = QtWidgets.QRadioButton(self.tab_TrackMeal)
        self.radioButton_Dinner.setObjectName("radioButton_Dinner")
        self.horizontalLayout_2.addWidget(self.radioButton_Dinner)
        self.radioButton_Snacks = QtWidgets.QRadioButton(self.tab_TrackMeal)
        self.radioButton_Snacks.setObjectName("radioButton_Snacks")
        self.horizontalLayout_2.addWidget(self.radioButton_Snacks)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.gridLayout_6.addLayout(self.verticalLayout, 0, 1, 2, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_TrackMeal)
        self.groupBox_3.setMaximumSize(QtCore.QSize(262, 86))
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_6.addWidget(self.label_2)
        self.lineEdit_Mass = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_Mass.setObjectName("lineEdit_Mass")
        self.horizontalLayout_6.addWidget(self.lineEdit_Mass)
        self.horizontalLayout_14.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_13.addWidget(self.label_3)
        self.dateEdit_Mass = QtWidgets.QDateEdit(self.groupBox_3)
        self.dateEdit_Mass.setDateTime(QtCore.QDateTime(QtCore.QDate(2020, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateEdit_Mass.setCalendarPopup(True)
        self.dateEdit_Mass.setObjectName("dateEdit_Mass")
        self.horizontalLayout_13.addWidget(self.dateEdit_Mass)
        self.horizontalLayout_14.addLayout(self.horizontalLayout_13)
        self.gridLayout_5.addLayout(self.horizontalLayout_14, 0, 0, 1, 1)
        self.pushButton_page = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_page.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.pushButton_page.setObjectName("pushButton_page")
        self.gridLayout_5.addWidget(self.pushButton_page, 1, 0, 1, 1)
        self.gridLayout_6.addWidget(self.groupBox_3, 1, 0, 1, 1)
        self.tableWidget_entry = QtWidgets.QTableWidget(self.tab_TrackMeal)
        self.tableWidget_entry.setMinimumSize(QtCore.QSize(520, 218))
        font = QtGui.QFont()
        font.setKerning(False)
        self.tableWidget_entry.setFont(font)
        self.tableWidget_entry.setRowCount(0)
        self.tableWidget_entry.setColumnCount(8)
        self.tableWidget_entry.setObjectName("tableWidget_entry")
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(9)
        item.setFont(font)
        self.tableWidget_entry.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(9)
        item.setFont(font)
        self.tableWidget_entry.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(9)
        item.setFont(font)
        self.tableWidget_entry.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(9)
        item.setFont(font)
        self.tableWidget_entry.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(9)
        item.setFont(font)
        self.tableWidget_entry.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(9)
        item.setFont(font)
        self.tableWidget_entry.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_entry.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_entry.setHorizontalHeaderItem(7, item)
        self.tableWidget_entry.horizontalHeader().setDefaultSectionSize(60)
        self.tableWidget_entry.verticalHeader().setDefaultSectionSize(23)
        self.gridLayout_6.addWidget(self.tableWidget_entry, 2, 0, 1, 2)
        self.tabWidget.addTab(self.tab_TrackMeal, "")
        self.tab_Analytics = QtWidgets.QWidget()
        self.tab_Analytics.setObjectName("tab_Analytics")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_Analytics)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.MplWidget1 = MplWidget1(self.tab_Analytics)
        self.MplWidget1.setObjectName("MplWidget1")
        self.gridLayout_3.addWidget(self.MplWidget1, 0, 0, 1, 1)
        self.MplWidget2 = MplWidget2(self.tab_Analytics)
        self.MplWidget2.setObjectName("MplWidget2")
        self.gridLayout_3.addWidget(self.MplWidget2, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab_Analytics, "")
        self.Database = QtWidgets.QWidget()
        self.Database.setObjectName("Database")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.Database)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_database = QtWidgets.QLabel(self.Database)
        self.label_database.setObjectName("label_database")
        self.gridLayout_4.addWidget(self.label_database, 0, 0, 1, 1)
        self.tableWidget_database = QtWidgets.QTableWidget(self.Database)
        self.tableWidget_database.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.tableWidget_database.setAutoFillBackground(False)
        self.tableWidget_database.setLineWidth(1)
        self.tableWidget_database.setAutoScroll(False)
        self.tableWidget_database.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget_database.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget_database.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget_database.setRowCount(10)
        self.tableWidget_database.setColumnCount(6)
        self.tableWidget_database.setObjectName("tableWidget_database")
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(9)
        item.setFont(font)
        item.setBackground(QtGui.QColor(255, 255, 255))
        self.tableWidget_database.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(9)
        item.setFont(font)
        self.tableWidget_database.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(9)
        item.setFont(font)
        self.tableWidget_database.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(9)
        item.setFont(font)
        self.tableWidget_database.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(9)
        item.setFont(font)
        self.tableWidget_database.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(9)
        item.setFont(font)
        self.tableWidget_database.setHorizontalHeaderItem(5, item)
        self.tableWidget_database.horizontalHeader().setDefaultSectionSize(60)
        self.tableWidget_database.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_database.verticalHeader().setDefaultSectionSize(23)
        self.gridLayout_4.addWidget(self.tableWidget_database, 1, 0, 1, 2)
        self.pushButton_database_AddNewEntry = QtWidgets.QPushButton(self.Database)
        self.pushButton_database_AddNewEntry.setObjectName("pushButton_database_AddNewEntry")
        self.gridLayout_4.addWidget(self.pushButton_database_AddNewEntry, 2, 0, 1, 1)
        self.pushButton_database_Delete = QtWidgets.QPushButton(self.Database)
        self.pushButton_database_Delete.setObjectName("pushButton_database_Delete")
        self.gridLayout_4.addWidget(self.pushButton_database_Delete, 2, 1, 1, 1)
        self.tabWidget.addTab(self.Database, "")
        self.gridLayout_2.addWidget(self.tabWidget, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 562, 21))
        self.menubar.setObjectName("menubar")
        self.menuconfiguration = QtWidgets.QMenu(self.menubar)
        self.menuconfiguration.setObjectName("menuconfiguration")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuconfiguration.menuAction())
        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_profile.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.groupBox.setTitle(_translate("MainWindow", "Meal Entry"))
        self.label_12.setText(_translate("MainWindow", "Goal Calories:"))
        self.label_PickFood.setText(_translate("MainWindow", "Food"))
        self.label.setText(_translate("MainWindow", "Date"))
        self.label_MealCategory.setText(_translate("MainWindow", "Category"))
        self.pushButton_entry_AddNewEntry.setText(_translate("MainWindow", "Add New Entry"))
        self.label_13.setText(_translate("MainWindow", "Total Intake:"))
        self.label_15.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Net Calories:</span></p></body></html>"))
        self.label_14.setText(_translate("MainWindow", "Exercise:"))
        self.lineEdit_Exercise.setText(_translate("MainWindow", "0"))
        self.pushButton_Save.setText(_translate("MainWindow", "Save"))
        self.radioButton_Breakfast.setText(_translate("MainWindow", "Breakfast"))
        self.radioButton_Lunch.setText(_translate("MainWindow", "Lunch"))
        self.radioButton_Dinner.setText(_translate("MainWindow", "Dinner"))
        self.radioButton_Snacks.setText(_translate("MainWindow", "Snacks"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Weekly Mass"))
        self.label_2.setText(_translate("MainWindow", "Mass:"))
        self.label_3.setText(_translate("MainWindow", "Date:"))
        self.pushButton_page.setText(_translate("MainWindow", "Enter"))
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
        item.setText(_translate("MainWindow", "Category"))
        item = self.tableWidget_entry.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Date"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_TrackMeal), _translate("MainWindow", "Track Meal"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Analytics), _translate("MainWindow", "Analytics"))
        self.label_database.setText(_translate("MainWindow", "Database (Editable)"))
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
        self.pushButton_database_AddNewEntry.setText(_translate("MainWindow", "Add New Entry"))
        self.pushButton_database_Delete.setText(_translate("MainWindow", "Delete Selected Row"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Database), _translate("MainWindow", "Database"))
        self.menuconfiguration.setTitle(_translate("MainWindow", "Configuration"))
        self.ProfileOpen()
        self.lineEdit_Goal_3.setText(str(ReqCalorie))
        self.lineEdit_Exercise.setText("0")
        self.pushButton_Save.clicked.connect(self.CaloriesSave)
        global CalorieAnalytics
        import pandas as pd
        if os.path.exists('CalorieAnalytics.csv') == False:
            CalorieAnalytics = pd.DataFrame({"Calories": [],
                                      "Date": []})
            CalorieAnalytics.Date = pd.to_datetime(CalorieAnalytics.Date)
            CalorieAnalytics["Calories"] = CalorieAnalytics["Calories"].astype(str)
        if os.path.exists('CalorieAnalytics.csv') == True:
            import pandas as pd
            CalorieAnalytics = pd.read_csv("CalorieAnalytics.csv")
            CalorieAnalytics.Date = pd.to_datetime(CalorieAnalytics.Date)
            CalorieAnalytics["Calories"] = CalorieAnalytics["Calories"].astype(str)
            self.gen_chart_calories(CalorieAnalytics.Calories, CalorieAnalytics.Date)
        global MassAnalytics
        import pandas as pd
        if os.path.exists('MassAnalytics.csv') == False:
            MassAnalytics = pd.DataFrame({"Mass": [],
                                      "Date": []})
            MassAnalytics.Date = pd.to_datetime(MassAnalytics.Date)
            MassAnalytics["Mass"] = MassAnalytics["Mass"].astype(str)
        if os.path.exists('MassAnalytics.csv') == True:
            MassAnalytics = pd.read_csv("MassAnalytics.csv")
            MassAnalytics.Date = pd.to_datetime(MassAnalytics.Date)
            MassAnalytics["Mass"] = MassAnalytics["Mass"].astype(str)
            print(MassAnalytics)
        try:
            self.tableWidget_newentry_load()
        except:
            pass
        self.dateEdit.setDate(QDate.currentDate())
        self.dateEdit_Mass.setDate(QDate.currentDate())
        self.printTOTable()
        self.tableWidget_database.cellChanged.connect(self.readTable)
        self.tableWidget_database.setColumnWidth(0,70)
        self.tableWidget_entry.setColumnWidth(0, 70)
        self.tableWidget_entry.setColumnWidth(7, 80)
        self.pushButton_entry_AddNewEntry.clicked.connect(self.NewItem)
        self.pushButton_database_AddNewEntry.clicked.connect(self.func_pushButton_database_AddNewEntry)
        str_meal = ['Breakfast' , 'Lunch' , 'Dinner' , 'Snacks']
        self.comboBox_pickfood.addItems(list(df['Food']))
        self.comboBox_meal.addItems(str_meal)
        self.pushButton_entry_AddNewEntry.clicked.connect(lambda: self.tableWidget_newentry(str(self.comboBox_pickfood.currentText()), str(self.comboBox_meal.currentText())))
        self.pushButton_database_Delete.clicked.connect(self.btn_pushButton_database_Delete)
        self.radioButton_Breakfast.clicked.connect(lambda: self.gen_chart("Breakfast"))
        self.radioButton_Lunch.clicked.connect(lambda: self.gen_chart("Lunch"))
        self.radioButton_Dinner.clicked.connect(lambda: self.gen_chart("Dinner"))
        self.radioButton_Snacks.clicked.connect(lambda: self.gen_chart("Snacks"))
        self.pushButton_page.clicked.connect(self.gen_chart_mass)
        _translate = QtCore.QCoreApplication.translate
        self.label_profile.setText(_translate("MainWindow","Name: "+Name+ ",   Gender: "+Gender+",   Age: "+ str(Age) + ",   Required Calories: "+str(ReqCalorie)))
        try:
            self.gen_chart_mass()
        except:
            pass
        try:
            self.gen_chart_calories()
        except:
            pass
    def CaloriesSave(self):
        import  pandas as pd
        TotalIntake = [sum(dfe.Calories), sum(dfe.Carbs), sum(dfe.Fat), sum(dfe.Protein), sum(dfe.Fibre)]
        TotalIntake = sum(TotalIntake)
        NetCalories = float(TotalIntake) - float(self.lineEdit_Exercise.text())
        self.lineEdit_TotalIntake.setText(str(TotalIntake))
        self.lineEdit_NetCalories.setText(str(NetCalories))

        dfe.to_csv('dfe.csv', index=False)
        try:
            global CalorieAnalytics
            temp_var = self.dateEdit.date()
            var_date = temp_var.toPyDate()
            CalorieLoad = pd.DataFrame({"Calories": [str(NetCalories)], "Date": [var_date]})
            CalorieLoad.Date = pd.to_datetime(CalorieLoad.Date)
            CalorieAnalytics = CalorieAnalytics.append(CalorieLoad,  ignore_index = True)
            self.gen_chart_calories(CalorieAnalytics.Calories, CalorieAnalytics.Date)
            CalorieAnalytics.to_csv('CalorieAnalytics.csv', index=False)
        except Exception as e:
            print(str(e))
    def ProfileOpen(self):
        Profile = [line.rstrip() for line in open('Config')]
        global Gender
        global Name
        global Age
        global Height
        global Mass
        global Activity
        global ReqCalorie
        Gender = Profile[0]
        Name = Profile[1]
        Age = float(Profile[2])
        Height = float(Profile[3])
        Mass = float(Profile[4])
        Activity = Profile[5]
        ReqCalorie = float(Profile[6])
    def home_entry(self,Mass,Date):
        import pandas as pd
        global dfhome
        dfhome = pd.DataFrame({"Mass": [],
                           "Goal": [],
                           "Intake": [],"Exercise": [], "NetCalories": [], "Date": []})
        dfhome["Date"] = dfhome["Date"].astype(str)

    def gen_chart(self, Meal):
        try:
            labels = 'Calories', 'Carbs', 'Fat', 'Protein', 'Fibre'
            temp_var = self.dateEdit.date()
            var_date = temp_var.toPyDate()
            dfeChart = dfe[dfe.Date == str(var_date)]
            print(dfeChart)
            sizes = [sum(dfeChart[dfeChart.Category==Meal].Calories), sum(dfeChart[dfeChart.Category==Meal].Carbs), sum(dfeChart.Fat), sum(dfeChart[dfeChart.Category==Meal].Protein), sum(dfeChart[dfeChart.Category==Meal].Fibre)]
            self.MplWidget.canvas.axes.clear()
            self.MplWidget.canvas.axes.pie(sizes,labels=labels, radius=1.2,autopct='%1.1f%%',
                                 shadow=True, startangle=90,textprops={'fontsize': 7})
            self.MplWidget.canvas.axes.set_title(Meal+' Calories Breakdown')
            self.MplWidget.canvas.draw()
        except Exception as e:
            self.errMessage("Reading Table:", str(e))
    def gen_chart_mass(self):
        try:
            global MassAnalytics
            import pandas as pd
            temp_var = self.dateEdit_Mass.date()
            var_date = temp_var.toPyDate()
            if str(self.lineEdit_Mass.text()) != '':
                MassLoad = pd.DataFrame({"Mass": [str(self.lineEdit_Mass.text())], "Date": [var_date]})
                MassLoad.Date = pd.to_datetime(MassLoad.Date)
                MassAnalytics = MassAnalytics.append(MassLoad,  ignore_index = True)
                MassAnalytics.to_csv('MassAnalytics.csv', index=False)
            self.MplWidget1.canvas.axes.clear()
            self.MplWidget1.canvas.axes.plot(MassAnalytics.Date, MassAnalytics.Mass)
            self.MplWidget1.canvas.axes.set_title('Mass Plot')
            self.MplWidget1.canvas.draw()
            print(MassAnalytics)


        except Exception as e:
            self.errMessage("Reading Table:", str(e))
    def gen_chart_calories(self,CaloriesSum, CaloriesDate):
        try:
            self.MplWidget2.canvas.axes.clear()
            self.MplWidget2.canvas.axes.plot(CaloriesDate, CaloriesSum)
            self.MplWidget2.canvas.axes.set_title('Calories Plot')
            self.MplWidget2.canvas.draw()
        except Exception as e:
            self.errMessage("Reading Table:", str(e))
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
                df.to_csv('df.csv',index=False)
        except Exception as e:
            self.errMessage("Reading Table:", str(e))

    def pltConfigWindow(self):
        self.Dialog_Config = QtWidgets.QDialog()
        self.ui = Ui_Dialog_Config()
        self.ui.setupUi(self.Dialog_Config)

        self.Dialog_Config.show()



    def readTable_tableWidget_entry(self):

   #     app_conf = QtWidgets.QApplication(sys.argv)

   #     sys.exit(app_conf.exec_())
        import pandas as pd
        global dfe
        tableDimensions = [int(self.tableWidget_entry.rowCount()), int(self.tableWidget_entry.columnCount())]
        dfe = pd.DataFrame({"Food": [],
                           "Calories": [],
                           "Carbs": [],"Fat": [], "Protein": [], "Fibre": [], "Category": [], "Date": []})
        dfe["Category"] = dfe["Category"].astype(str)
        dfe["Date"] = dfe["Date"].astype(str)
        i = 0
        try:
            while i < tableDimensions[1]:
                j = 0
                while j < tableDimensions[0]:
                    a_item = self.tableWidget_entry.item(j, i)
                    a_name = str(a_item.text())
                    if j == tableDimensions[0]:
                        a_name = pd.to_datetime(a_item.text())
                        ##print(a_name)

                    dfe.set_value(j,list(dfe)[i], a_name)
                    #df[i].loc[j] = a_name
                    j += 1
                i += 1
                ##print(dfe)
            self.gen_chart(self.comboBox_meal.currentText())
            from datetime import date
            import pandas as pd
            Date = str(pd.to_datetime(pd.Timestamp(date.today())).date())
            sizes = [sum(dfe[dfe.Date == Date].Calories), sum(dfe[dfe.Date == Date].Carbs),
                     sum(dfe[dfe.Date == Date].Fat),
                     sum(dfe[dfe.Date == Date].Protein), sum(dfe[dfe.Date == Date].Fibre)]
            ##print(sizes)
        except Exception as e:
            self.errMessage("Printing to Table:", str(e))
    def printTOTable(self):  # Prints data file to table
        import pandas as pd
        global df
        import os
        if os.path.exists('df.csv') == True:
            df = pd.read_csv("df.csv")
        if os.path.exists('df.csv') == False:
            df = pd.DataFrame({"Food": ["Tea", "Egg", "Rotti"],
                           "Calories": [11, 212, 312],
                           "Carbs": [112, 2122, 3212],
                           "Fat": [11, 212, 321], "Protein": [11, 212, 321], "Fibre": [11, 212, 321]})
        try:
            i = 0
            for p in list(df):
                j = 0
                ##print(p)
                while j < df.shape[0]:
                    A = []
                    # ###print(data[j,i])
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
            ##print(df)
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
    def tableWidget_newentry_load(self):  # Prints data file to table
        import pandas as pd
        global dfe
        dfe = pd.read_csv("dfe.csv")
        self.tableWidget_entry.setRowCount(dfe.shape[0])
        #print(dfe)
        try:
            i = 0
            for p in list(dfe):
                j = 0
                ##print(p)
                while j < dfe.shape[0]:
                    A = []
                    # ###print(data[j,i])
                    A = str(dfe[p].loc[j])
                    cellinfo = QTableWidgetItem(A)
                    self.tableWidget_entry.setItem(j, i, cellinfo)
                    j += 1
                i += 1

        except Exception as e:
            self.errMessage("Printing to Table:", str(e))


    def tableWidget_newentry(self, food, meal):  # Prints data file to table
        temp_var = self.dateEdit.date()
        var_date = temp_var.toPyDate()
        self.tableWidget_entry.setRowCount(self.tableWidget_entry.rowCount()+1)
        A = str(var_date)
        cellinfo = QTableWidgetItem(A)
        self.tableWidget_entry.setItem(int(self.tableWidget_entry.rowCount() - 1), 7, cellinfo)
        A = str(self.comboBox_meal.currentText())
        cellinfo = QTableWidgetItem(A)
        self.tableWidget_entry.setItem(int(self.tableWidget_entry.rowCount() - 1), 6, cellinfo)

        try:
            j=0
            for p in list(df.loc[self.comboBox_pickfood.currentIndex()]):
          #      #print(p)
                A = str(p)
                cellinfo = QTableWidgetItem(A)
                self.tableWidget_entry.setItem(int(self.tableWidget_entry.rowCount()-1), j, cellinfo)
                j += 1
            self.readTable_tableWidget_entry()
            TotalIntake = [sum(dfe[dfe.Date==str(var_date)].Calories), sum(dfe[dfe.Date==str(var_date)].Carbs), sum(dfe[dfe.Date==str(var_date)].Fat), sum(dfe[dfe.Date==str(var_date)].Protein), sum(dfe[dfe.Date==str(var_date)].Fibre)]
            TotalIntake = sum(TotalIntake)
            NetCalories= float(TotalIntake) - float(self.lineEdit_Exercise.text())
            self.lineEdit_TotalIntake.setText(str(TotalIntake))
            self.lineEdit_NetCalories.setText(str(NetCalories))
            if str(self.comboBox_meal.currentText())=="Breakfast":
                self.radioButton_Breakfast.setChecked(True)
            if str(self.comboBox_meal.currentText()) == "Lunch":
                self.radioButton_Lunch.setChecked(True)
            if str(self.comboBox_meal.currentText()) == "Dinner":
                self.radioButton_Dinner.setChecked(True)
            if str(self.comboBox_meal.currentText()) == "Snacks":
                self.radioButton_Snacks.setChecked(True)


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




from MplWidget import MplWidget
from MplWidget1 import MplWidget1
from MplWidget2 import MplWidget2

if __name__ == "__main__":
    import os
    if os.path.exists('Config') == False:
        import sys
        app = QtWidgets.QApplication(sys.argv)
        Dialog_Config = QtWidgets.QDialog()
        ui = Ui_Dialog_Config()
        ui.setupUi(Dialog_Config)
        Dialog_Config.show()
        sys.exit(app.exec_())
    if os.path.exists('Config') == True:
        import sys
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())
