# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'visitors.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Visitors(object):
    def setupUi(self, Visitors):
        Visitors.setObjectName("Visitors")
        Visitors.resize(418, 313)
        self.pushButtonBack = QtWidgets.QPushButton(Visitors)
        self.pushButtonBack.setGeometry(QtCore.QRect(260, 270, 151, 31))
        self.pushButtonBack.setObjectName("pushButtonBack")
        self.radioButton_2 = QtWidgets.QRadioButton(Visitors)
        self.radioButton_2.setGeometry(QtCore.QRect(330, 40, 31, 17))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton = QtWidgets.QRadioButton(Visitors)
        self.radioButton.setGeometry(QtCore.QRect(280, 40, 31, 17))
        self.radioButton.setObjectName("radioButton")
        self.comboBoxGroups = QtWidgets.QComboBox(Visitors)
        self.comboBoxGroups.setGeometry(QtCore.QRect(10, 90, 251, 24))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.comboBoxGroups.setFont(font)
        self.comboBoxGroups.setEditable(False)
        self.comboBoxGroups.setCurrentText("")
        self.comboBoxGroups.setObjectName("comboBoxGroups")
        self.label = QtWidgets.QLabel(Visitors)
        self.label.setGeometry(QtCore.QRect(10, 70, 121, 16))
        self.label.setObjectName("label")
        self.comboBoxVisitors = QtWidgets.QComboBox(Visitors)
        self.comboBoxVisitors.setGeometry(QtCore.QRect(10, 10, 251, 22))
        self.comboBoxVisitors.setObjectName("comboBoxVisitors")
        self.lineEdit = QtWidgets.QLineEdit(Visitors)
        self.lineEdit.setGeometry(QtCore.QRect(10, 40, 251, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButtonAdd = QtWidgets.QPushButton(Visitors)
        self.pushButtonAdd.setGeometry(QtCore.QRect(280, 90, 111, 31))
        self.pushButtonAdd.setObjectName("pushButtonAdd")
        self.pushButtonLeaveGroup = QtWidgets.QPushButton(Visitors)
        self.pushButtonLeaveGroup.setGeometry(QtCore.QRect(280, 180, 111, 31))
        self.pushButtonLeaveGroup.setObjectName("pushButtonLeaveGroup")
        self.pushButtonDeleteVisitor = QtWidgets.QPushButton(Visitors)
        self.pushButtonDeleteVisitor.setGeometry(QtCore.QRect(280, 220, 111, 31))
        self.pushButtonDeleteVisitor.setObjectName("pushButtonDeleteVisitor")
        self.comboBoxGroups_2 = QtWidgets.QComboBox(Visitors)
        self.comboBoxGroups_2.setGeometry(QtCore.QRect(10, 180, 251, 24))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.comboBoxGroups_2.setFont(font)
        self.comboBoxGroups_2.setEditable(False)
        self.comboBoxGroups_2.setCurrentText("")
        self.comboBoxGroups_2.setObjectName("comboBoxGroups_2")
        self.comboBoxVisitors_2 = QtWidgets.QComboBox(Visitors)
        self.comboBoxVisitors_2.setGeometry(QtCore.QRect(10, 220, 251, 22))
        self.comboBoxVisitors_2.setObjectName("comboBoxVisitors_2")

        self.retranslateUi(Visitors)
        QtCore.QMetaObject.connectSlotsByName(Visitors)

    def retranslateUi(self, Visitors):
        _translate = QtCore.QCoreApplication.translate
        Visitors.setWindowTitle(_translate("Visitors", "Посетители"))
        self.pushButtonBack.setText(_translate("Visitors", "&Назад"))
        self.radioButton_2.setText(_translate("Visitors", "16"))
        self.radioButton.setText(_translate("Visitors", "8"))
        self.label.setText(_translate("Visitors", "Незаполенные группы"))
        self.pushButtonAdd.setText(_translate("Visitors", "Добавить"))
        self.pushButtonLeaveGroup.setText(_translate("Visitors", "Покинуть группу"))
        self.pushButtonDeleteVisitor.setText(_translate("Visitors", "Закрыть абонемент"))

