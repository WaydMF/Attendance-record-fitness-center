# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'authorization.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Authorization(object):
    def setupUi(self, Authorization):
        Authorization.setObjectName("Authorization")
        Authorization.resize(255, 201)
        self.labelLogin = QtWidgets.QLabel(Authorization)
        self.labelLogin.setGeometry(QtCore.QRect(40, 20, 47, 13))
        self.labelLogin.setObjectName("labelLogin")
        self.labelPassword = QtWidgets.QLabel(Authorization)
        self.labelPassword.setGeometry(QtCore.QRect(40, 70, 47, 13))
        self.labelPassword.setObjectName("labelPassword")
        self.lineEditLogin = QtWidgets.QLineEdit(Authorization)
        self.lineEditLogin.setGeometry(QtCore.QRect(40, 40, 181, 20))
        self.lineEditLogin.setObjectName("lineEditLogin")
        self.lineEditPassword = QtWidgets.QLineEdit(Authorization)
        self.lineEditPassword.setGeometry(QtCore.QRect(40, 100, 181, 20))
        self.lineEditPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEditPassword.setObjectName("lineEditPassword")
        self.pushButtonEnter = QtWidgets.QPushButton(Authorization)
        self.pushButtonEnter.setGeometry(QtCore.QRect(80, 140, 101, 41))
        self.pushButtonEnter.setObjectName("pushButtonEnter")

        self.retranslateUi(Authorization)
        QtCore.QMetaObject.connectSlotsByName(Authorization)

    def retranslateUi(self, Authorization):
        _translate = QtCore.QCoreApplication.translate
        Authorization.setWindowTitle(_translate("Authorization", "Авторизация"))
        self.labelLogin.setText(_translate("Authorization", "Имя"))
        self.labelPassword.setText(_translate("Authorization", "Пароль"))
        self.pushButtonEnter.setText(_translate("Authorization", "Вход"))

