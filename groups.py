# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'groups.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Groups(object):
    def setupUi(self, Groups):
        Groups.setObjectName("Groups")
        Groups.resize(302, 153)
        self.pushButtonBack = QtWidgets.QPushButton(Groups)
        self.pushButtonBack.setGeometry(QtCore.QRect(140, 100, 151, 31))
        self.pushButtonBack.setObjectName("pushButtonBack")
        self.lineEdit = QtWidgets.QLineEdit(Groups)
        self.lineEdit.setGeometry(QtCore.QRect(20, 30, 191, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(Groups)
        self.label.setGeometry(QtCore.QRect(20, 10, 121, 16))
        self.label.setObjectName("label")
        self.pushButtonAdd = QtWidgets.QPushButton(Groups)
        self.pushButtonAdd.setGeometry(QtCore.QRect(220, 30, 75, 23))
        self.pushButtonAdd.setObjectName("pushButtonAdd")
        self.pushButtonDelete = QtWidgets.QPushButton(Groups)
        self.pushButtonDelete.setGeometry(QtCore.QRect(220, 60, 75, 23))
        self.pushButtonDelete.setObjectName("pushButtonDelete")
        self.comboBoxGroups = QtWidgets.QComboBox(Groups)
        self.comboBoxGroups.setGeometry(QtCore.QRect(20, 60, 191, 22))
        self.comboBoxGroups.setObjectName("comboBoxGroups")

        self.retranslateUi(Groups)
        QtCore.QMetaObject.connectSlotsByName(Groups)

    def retranslateUi(self, Groups):
        _translate = QtCore.QCoreApplication.translate
        Groups.setWindowTitle(_translate("Groups", "Группы"))
        self.pushButtonBack.setText(_translate("Groups", "&Назад"))
        self.label.setText(_translate("Groups", "Название новой группы"))
        self.pushButtonAdd.setText(_translate("Groups", "Добавить"))
        self.pushButtonDelete.setText(_translate("Groups", "Удалить"))

