# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Config.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_Config(object):
    def setupUi(self, Dialog_Config):
        Dialog_Config.setObjectName("Dialog_Config")
        Dialog_Config.resize(458, 258)
        Dialog_Config.setFocusPolicy(QtCore.Qt.StrongFocus)
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
        self.lineEdit_Age.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhFormattedNumbersOnly)
        self.lineEdit_Age.setObjectName("lineEdit_Age")
        self.verticalLayout.addWidget(self.lineEdit_Age)
        self.lineEdit_Height = QtWidgets.QLineEdit(Dialog_Config)
        self.lineEdit_Height.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhFormattedNumbersOnly)
        self.lineEdit_Height.setObjectName("lineEdit_Height")
        self.verticalLayout.addWidget(self.lineEdit_Height)
        self.lineEdit_Mass = QtWidgets.QLineEdit(Dialog_Config)
        self.lineEdit_Mass.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhFormattedNumbersOnly)
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




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_Config = QtWidgets.QDialog()
    ui = Ui_Dialog_Config()
    ui.setupUi(Dialog_Config)
    Dialog_Config.show()
    sys.exit(app.exec_())
