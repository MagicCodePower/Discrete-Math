# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lab1.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 764)
        MainWindow.setStyleSheet("font-size:16px;\n"
"font-family: \"Rockwell Condensed\"; ")
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(330, 10, 141, 31))
        self.label.setStyleSheet("font-size:26px;\n"
"font-family: \"Rockwell Condensed\"; ")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(510, 30, 231, 41))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(700, 65, 55, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(690, 90, 71, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(50, 120, 55, 21))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 140, 761, 221))
        self.label_6.setMaximumSize(QtCore.QSize(800, 16777215))
        self.label_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(40, 370, 121, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(400, 370, 121, 16))
        self.label_8.setObjectName("label_8")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(40, 390, 181, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(400, 390, 191, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(40, 420, 55, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(400, 420, 55, 16))
        self.label_10.setObjectName("label_10")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(70, 420, 81, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(430, 420, 81, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.menu = QtWidgets.QLabel(self.centralwidget)
        self.menu.setGeometry(QtCore.QRect(40, 480, 55, 16))
        self.menu.setObjectName("menu")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(30, 500, 201, 135))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.pushButton_4 = QtWidgets.QPushButton(self.formLayoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.formLayoutWidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(self.formLayoutWidget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.pushButton_6)
        self.pushButton_7 = QtWidgets.QPushButton(self.formLayoutWidget)
        self.pushButton_7.setObjectName("pushButton_7")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.pushButton_7)
        self.pushButton_3 = QtWidgets.QPushButton(self.formLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.pushButton_3)
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(230, 390, 21, 21))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(600, 390, 21, 21))
        self.pushButton_9.setObjectName("pushButton_9")
        self.a = QtWidgets.QLabel(self.centralwidget)
        self.a.setGeometry(QtCore.QRect(410, 480, 361, 151))
        self.a.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.a.setObjectName("a")
        self.b = QtWidgets.QLabel(self.centralwidget)
        self.b.setGeometry(QtCore.QRect(410, 570, 351, 131))
        self.b.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.b.setObjectName("b")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Courtrol work"))
        self.label_2.setText(_translate("MainWindow", "prepared by Elizabeth Savenko"))
        self.label_3.setText(_translate("MainWindow", "IO-з91"))
        self.label_4.setText(_translate("MainWindow", "Variant 9"))
        self.label_5.setText(_translate("MainWindow", "My Y: "))
        self.label_6.setText(_translate("MainWindow", "Y : { }"))
        self.label_7.setText(_translate("MainWindow", "Enter A(with \' \'):"))
        self.label_8.setText(_translate("MainWindow", "Enter B(with \' \'):"))
        self.label_9.setText(_translate("MainWindow", "or "))
        self.label_10.setText(_translate("MainWindow", "or "))
        self.pushButton.setText(_translate("MainWindow", "download"))
        self.pushButton_2.setText(_translate("MainWindow", "download"))
        self.menu.setText(_translate("MainWindow", "Menu"))
        self.pushButton_4.setText(_translate("MainWindow", "B"))
        self.pushButton_5.setText(_translate("MainWindow", "C"))
        self.pushButton_6.setText(_translate("MainWindow", "D"))
        self.pushButton_7.setText(_translate("MainWindow", "F"))
        self.pushButton_3.setText(_translate("MainWindow", "A"))
        self.pushButton_8.setText(_translate("MainWindow", "ok"))
        self.pushButton_9.setText(_translate("MainWindow", "ok"))
        self.a.setText(_translate("MainWindow", "A: {}"))
        self.b.setText(_translate("MainWindow", "B: {}"))
