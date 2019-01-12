# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'statusGr.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_StatusGroup(object):
    def setupUi(self, StatusGroup):
        StatusGroup.setObjectName("StatusGroup")
        StatusGroup.resize(446, 218)
        self.pushButtonBack = QtWidgets.QPushButton(StatusGroup)
        self.pushButtonBack.setGeometry(QtCore.QRect(280, 180, 151, 31))
        self.pushButtonBack.setObjectName("pushButtonBack")
        self.textEdit = QtWidgets.QTextEdit(StatusGroup)
        self.textEdit.setGeometry(QtCore.QRect(10, 10, 421, 161))
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(StatusGroup)
        QtCore.QMetaObject.connectSlotsByName(StatusGroup)

    def retranslateUi(self, StatusGroup):
        _translate = QtCore.QCoreApplication.translate
        StatusGroup.setWindowTitle(_translate("StatusGroup", "Состояние группы"))
        self.pushButtonBack.setText(_translate("StatusGroup", "&Назад"))

