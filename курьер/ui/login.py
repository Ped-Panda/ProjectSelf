# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(270, 110, 261, 61))
        font = QtGui.QFont()
        font.setPointSize(32)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(310, 200, 171, 61))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.btn_admin = QtWidgets.QPushButton(self.centralwidget)
        self.btn_admin.setGeometry(QtCore.QRect(200, 290, 171, 71))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.btn_admin.setFont(font)
        self.btn_admin.setObjectName("btn_admin")
        self.btn_kurer = QtWidgets.QPushButton(self.centralwidget)
        self.btn_kurer.setGeometry(QtCore.QRect(420, 290, 171, 71))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.btn_kurer.setFont(font)
        self.btn_kurer.setObjectName("btn_kurer")
        self.btn_user = QtWidgets.QPushButton(self.centralwidget)
        self.btn_user.setGeometry(QtCore.QRect(250, 380, 291, 71))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.btn_user.setFont(font)
        self.btn_user.setObjectName("btn_user")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Авторизация"))
        self.label_2.setText(_translate("MainWindow", "Войти как"))
        self.btn_admin.setText(_translate("MainWindow", "Админ"))
        self.btn_kurer.setText(_translate("MainWindow", "Курьер"))
        self.btn_user.setText(_translate("MainWindow", "Пользователь"))
