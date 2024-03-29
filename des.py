# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 400)
        MainWindow.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(108, 109, 109);\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: rgb(147, 149, 149);\n"
"}\n"
"\n"
"QLineEdit {\n"
"    border-radius: 10px;\n"
"    padding-left: 10px;\n"
"}\n"
"\n"
"QTextBrowser {\n"
"    border-radius: 15px;\n"
"    background-color: white;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 481, 381))
        self.tabWidget.setObjectName("tabWidget")
        self.chat = QtWidgets.QWidget()
        self.chat.setObjectName("chat")
        self.textBrowser = QtWidgets.QTextBrowser(self.chat)
        self.textBrowser.setGeometry(QtCore.QRect(10, 10, 451, 111))
        self.textBrowser.setStyleSheet("")
        self.textBrowser.setPlaceholderText("")
        self.textBrowser.setObjectName("textBrowser")
        self.lineEdit = QtWidgets.QLineEdit(self.chat)
        self.lineEdit.setGeometry(QtCore.QRect(20, 140, 431, 51))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.chat)
        self.pushButton.setGeometry(QtCore.QRect(20, 210, 431, 61))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.chat)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 280, 431, 61))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setObjectName("pushButton_2")
        self.tabWidget.addTab(self.chat, "")
        self.settings = QtWidgets.QWidget()
        self.settings.setObjectName("settings")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.settings)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 10, 451, 41))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.settings)
        self.lineEdit_3.setGeometry(QtCore.QRect(10, 60, 451, 41))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.settings)
        self.lineEdit_4.setGeometry(QtCore.QRect(10, 110, 451, 41))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton_3 = QtWidgets.QPushButton(self.settings)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 170, 451, 51))
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setObjectName("pushButton_3")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.settings)
        self.textBrowser_2.setGeometry(QtCore.QRect(10, 241, 451, 101))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.tabWidget.addTab(self.settings, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Подключитесь к серверу</p></body></html>"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Сообщение"))
        self.pushButton.setText(_translate("MainWindow", "Отправить"))
        self.pushButton_2.setText(_translate("MainWindow", "Очистить"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.chat), _translate("MainWindow", "Чат"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "IP"))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", "ПОРТ"))
        self.lineEdit_4.setPlaceholderText(_translate("MainWindow", "ИМЯ"))
        self.pushButton_3.setText(_translate("MainWindow", "Подключиться"))
        self.textBrowser_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Подключитесь к серверу</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.settings), _translate("MainWindow", "Настройки"))
