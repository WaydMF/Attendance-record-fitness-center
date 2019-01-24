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
        Authorization.resize(275, 185)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Authorization)
        self.verticalLayout_3.setContentsMargins(-1, 17, -1, 23)
        self.verticalLayout_3.setSpacing(16)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.labelLogin = QtWidgets.QLabel(Authorization)
        self.labelLogin.setObjectName("labelLogin")
        self.verticalLayout_2.addWidget(self.labelLogin)
        self.lineEditLogin = QtWidgets.QLineEdit(Authorization)
        self.lineEditLogin.setObjectName("lineEditLogin")
        self.verticalLayout_2.addWidget(self.lineEditLogin)
        self.labelPassword = QtWidgets.QLabel(Authorization)
        self.labelPassword.setObjectName("labelPassword")
        self.verticalLayout_2.addWidget(self.labelPassword)
        self.lineEditPassword = QtWidgets.QLineEdit(Authorization)
        self.lineEditPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEditPassword.setObjectName("lineEditPassword")
        self.verticalLayout_2.addWidget(self.lineEditPassword)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButtonEnter = QtWidgets.QPushButton(Authorization)
        self.pushButtonEnter.setObjectName("pushButtonEnter")
        self.horizontalLayout.addWidget(self.pushButtonEnter)
        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.retranslateUi(Authorization)
        QtCore.QMetaObject.connectSlotsByName(Authorization)

    def retranslateUi(self, Authorization):
        _translate = QtCore.QCoreApplication.translate
        Authorization.setWindowTitle(_translate("Authorization", "Авторизация"))
        self.labelLogin.setText(_translate("Authorization", "Имя"))
        self.labelPassword.setText(_translate("Authorization", "Пароль"))
        self.pushButtonEnter.setText(_translate("Authorization", "Вход"))

