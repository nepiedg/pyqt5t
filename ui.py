# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(850, 817)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.translate = QtWidgets.QPushButton(self.centralwidget)
        self.translate.setGeometry(QtCore.QRect(380, 112, 81, 31))
        self.translate.setObjectName("translate")
        self.openfile = QtWidgets.QPushButton(self.centralwidget)
        self.openfile.setGeometry(QtCore.QRect(380, 160, 81, 31))
        self.openfile.setObjectName("openfile")
        self.clicktxt = QtWidgets.QPushButton(self.centralwidget)
        self.clicktxt.setGeometry(QtCore.QRect(380, 210, 81, 31))
        self.clicktxt.setObjectName("clicktxt")
        self.savefile = QtWidgets.QPushButton(self.centralwidget)
        self.savefile.setGeometry(QtCore.QRect(380, 260, 81, 31))
        self.savefile.setObjectName("savefile")
        self.putcontent = QtWidgets.QTextEdit(self.centralwidget)
        self.putcontent.setGeometry(QtCore.QRect(21, 11, 351, 751))
        self.putcontent.setObjectName("putcontent")
        self.outcontent = QtWidgets.QTextEdit(self.centralwidget)
        self.outcontent.setGeometry(QtCore.QRect(464, 11, 371, 761))
        self.outcontent.setObjectName("outcontent")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 850, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "伪原创"))
        self.translate.setText(_translate("MainWindow", "原创"))
        self.openfile.setText(_translate("MainWindow", "选择文件"))
        self.clicktxt.setText(_translate("MainWindow", "清除"))
        self.savefile.setText(_translate("MainWindow", "存储"))

