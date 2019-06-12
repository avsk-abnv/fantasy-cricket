# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fantasy_cric.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3,json,random,math
from new_match import play_thematch,create_scoretext
from calculatepoints import calculate_points
from dialogs import newTeam_dialog,show_evteam,save_team,error_dialog,openteam,myscore_board
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(755, 564)
        MainWindow.setMinimumSize(QtCore.QSize(755, 564))
        MainWindow.setMaximumSize(QtCore.QSize(755, 564))
        MainWindow.setStyleSheet("color: yellow;\n"
"background-color: rgb(93, 95, 82);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(93, 95, 82);\n"
"QPushButton::hover\n"
"{\n"
"    background-color:transparent;\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalWidget.setGeometry(QtCore.QRect(10, 20, 731, 81))
        self.verticalWidget.setStyleSheet("background-color: rgb(74, 74, 69);\n"
"padding-top:5px;\n"
"padding-left:5px;\n"
"border-radius:10px;")
        self.verticalWidget.setObjectName("verticalWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_5 = QtWidgets.QLabel(self.verticalWidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.horizontalWidget = QtWidgets.QWidget(self.verticalWidget)
        self.horizontalWidget.setStyleSheet("")
        self.horizontalWidget.setObjectName("horizontalWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_4 = QtWidgets.QLabel(self.horizontalWidget)
        self.label_4.setMaximumSize(QtCore.QSize(97, 16777215))
        self.label_4.setStyleSheet("color:white;")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.label_6 = QtWidgets.QLabel(self.horizontalWidget)
        self.label_6.setMaximumSize(QtCore.QSize(30, 16777215))
        self.label_6.setStyleSheet("color:lime;")
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6, 0, QtCore.Qt.AlignLeft)
        self.label = QtWidgets.QLabel(self.horizontalWidget)
        self.label.setStyleSheet("color:white;")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.label_7 = QtWidgets.QLabel(self.horizontalWidget)
        self.label_7.setStyleSheet("color:lime;")
        self.label_7.setObjectName("label_7")
        self.horizontalLayout.addWidget(self.label_7, 0, QtCore.Qt.AlignLeft)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout.addItem(spacerItem)
        self.label_2 = QtWidgets.QLabel(self.horizontalWidget)
        self.label_2.setStyleSheet("color:white;")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.label_8 = QtWidgets.QLabel(self.horizontalWidget)
        self.label_8.setStyleSheet("color:lime;")
        self.label_8.setObjectName("label_8")
        self.horizontalLayout.addWidget(self.label_8, 0, QtCore.Qt.AlignLeft)
        self.label_3 = QtWidgets.QLabel(self.horizontalWidget)
        self.label_3.setStyleSheet("color:white;")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.label_9 = QtWidgets.QLabel(self.horizontalWidget)
        self.label_9.setStyleSheet("color:lime;")
        self.label_9.setObjectName("label_9")
        self.horizontalLayout.addWidget(self.label_9, 0, QtCore.Qt.AlignLeft)
        self.verticalLayout.addWidget(self.horizontalWidget)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(30, 180, 281, 331))
        self.widget.setStyleSheet("background-color: black;\n"
"border-radius: 5px;\n"
"border: 1px solid yellow;")
        self.widget.setObjectName("widget")
        self.horizontalGroupBox = QtWidgets.QGroupBox(self.widget)
        self.horizontalGroupBox.setGeometry(QtCore.QRect(0, 0, 281, 31))
        self.horizontalGroupBox.setStyleSheet("background-color: rgb(68, 68, 58);")
        self.horizontalGroupBox.setObjectName("horizontalGroupBox")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalGroupBox)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.radioButton_2 = QtWidgets.QRadioButton(self.horizontalGroupBox)
        self.radioButton_2.setStyleSheet("background-color: transparent;\n"
"border:none;")
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout_2.addWidget(self.radioButton_2)
        self.radioButton_3 = QtWidgets.QRadioButton(self.horizontalGroupBox)
        self.radioButton_3.setStyleSheet("background-color: transparent;\n"
"border:none;")
        self.radioButton_3.setObjectName("radioButton_3")
        self.horizontalLayout_2.addWidget(self.radioButton_3)
        self.radioButton = QtWidgets.QRadioButton(self.horizontalGroupBox)
        self.radioButton.setStyleSheet("background-color: transparent;\n"
"border:none;")
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout_2.addWidget(self.radioButton)
        self.radioButton_4 = QtWidgets.QRadioButton(self.horizontalGroupBox)
        self.radioButton_4.setStyleSheet("background-color: transparent;\n"
"border:none;")
        self.radioButton_4.setObjectName("radioButton_4")
        self.horizontalLayout_2.addWidget(self.radioButton_4)
        self.listWidget = QtWidgets.QListWidget(self.widget)
        self.listWidget.setGeometry(QtCore.QRect(10, 40, 261, 281))
        self.listWidget.setStyleSheet("#listWidget{\n"
"background-color:black;\n"
"color:yellow;\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"padding:5px;\n"
"padding-left:10px;\nborder:none;"
"}\n"
"#listWidget::item:selected{\n"
"background-color:yellow;\nborder:none;\n"
"color:black;\n"
"}")
        self.listWidget.setObjectName("listWidget")
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(440, 180, 281, 331))
        self.widget_2.setStyleSheet("background-color: black;\n"
"border-radius: 5px;\n"
"border: 1px solid yellow;")
        self.widget_2.setObjectName("widget_2")
        self.horizontalWidget1 = QtWidgets.QWidget(self.widget_2)
        self.horizontalWidget1.setGeometry(QtCore.QRect(0, 0, 281, 31))
        self.horizontalWidget1.setStyleSheet("background-color: rgb(68, 68, 58);\n"
"border-bottom:none;")
        self.horizontalWidget1.setObjectName("horizontalWidget1")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalWidget1)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_12 = QtWidgets.QLabel(self.horizontalWidget1)
        self.label_12.setStyleSheet("background-color:transparent;\n"
"border:none;")
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_4.addWidget(self.label_12, 0, QtCore.Qt.AlignRight)
        self.label_11 = QtWidgets.QLabel(self.horizontalWidget1)
        self.label_11.setStyleSheet("background-color:transparent;\n"
"border:none;\n"
"color:lime;")
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_4.addWidget(self.label_11)
        self.listWidget_2 = QtWidgets.QListWidget(self.widget_2)
        self.listWidget_2.setGeometry(QtCore.QRect(10, 40, 261, 281))
        self.listWidget_2.setStyleSheet("#listWidget_2{\n"
"background-color:black;\n"
"color:yellow;\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"padding:5px;\n"
"padding-left:10px;\nborder:none;"
"}\n"
"#listWidget_2::item:selected{\n"
"background-color:yellow;\nborder:none;\n"
"color:black;\n"
"}")
        self.listWidget_2.setObjectName("listWidget_2")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(360, 340, 47, 13))
        self.label_10.setStyleSheet("font: 15pt \"Consolas\";\n"
"color: lime;")
        self.label_10.setObjectName("label_10")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 130, 825, 33))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_14 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_5.addWidget(self.label_14)
        self.label_15 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_15.setMinimumSize(QtCore.QSize(150, 0))
        self.label_15.setStyleSheet("color:lime;\n"
"font: 57 12pt \"Yu Gothic Medium\";")
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_5.addWidget(self.label_15, 0, QtCore.Qt.AlignLeft)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.label_16 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_16.setMinimumSize(QtCore.QSize(60, 0))
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_5.addWidget(self.label_16, 0, QtCore.Qt.AlignLeft)
        self.label_13 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_13.setMinimumSize(QtCore.QSize(50, 0))
        self.label_13.setStyleSheet("color:lime;\n"
"font: 57 12pt \"Yu Gothic Medium\";")
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_5.addWidget(self.label_13, 0, QtCore.Qt.AlignLeft)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        self.widget_3.setGeometry(QtCore.QRect(210, 150, 321, 201))
        self.widget_3.setStyleSheet("border:2px solid gray;\n"
"border-top:20px solid gray;\n"
"background-color: rgb(245, 245, 200);")
        self.widget_3.setObjectName("widget_3")
        self.horizontalWidget_2 = QtWidgets.QWidget(self.widget_3)
        self.horizontalWidget_2.setGeometry(QtCore.QRect(10, 50, 301, 40))
        self.horizontalWidget_2.setMinimumSize(QtCore.QSize(0, 40))
        self.horizontalWidget_2.setMaximumSize(QtCore.QSize(16777215, 31))
        self.horizontalWidget_2.setStyleSheet("border:none;")
        self.horizontalWidget_2.setObjectName("horizontalWidget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalWidget_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_17 = QtWidgets.QLabel(self.horizontalWidget_2)
        self.label_17.setStyleSheet("color:black;\n"
"border:none;")
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_3.addWidget(self.label_17)
        self.lineEdit = QtWidgets.QLineEdit(self.horizontalWidget_2)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit.setStyleSheet("background-color:white;\n"
"border-radius:5px;\n"
"border:1px solid orange;\n"
"font: 11pt \"MS Shell Dlg 2\";\n"
"color:black;")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_3.addWidget(self.lineEdit)
        self.horizontalWidget_3 = QtWidgets.QWidget(self.widget_3)
        self.horizontalWidget_3.setGeometry(QtCore.QRect(10, 140, 301, 51))
        self.horizontalWidget_3.setStyleSheet("border:none;")
        self.horizontalWidget_3.setObjectName("horizontalWidget_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalWidget_3)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalWidget_3)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 35))
        self.pushButton_2.setStyleSheet("#pushButton_2{\n"
"background-color: rgb(222, 236, 218);\n"
"color:black;\n"
"border-radius:5px;\n"
"border:1px solid blue;\n"
"}\n"
"#pushButton_2:hover{\n"
"    background-color:transparent;\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_6.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.horizontalWidget_3)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 35))
        self.pushButton.setStyleSheet("#pushButton{\n"
"color:black;\n"
"background-color: rgb(255, 227, 160);\n"
"border:1px solid red;\n"
"border-radius:5px;\n"
"}\n"
"#pushButton:hover{\n"
"    background-color:transparent;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_6.addWidget(self.pushButton)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_3.setGeometry(QtCore.QRect(300, 0, 15, 15))
        self.pushButton_3.setStyleSheet("#pushButton_3{\n"
"background-color: rgb(255, 85, 0);\n"
"border:2px solid gray;\n"
"border-radius:7px;\n"
"}\n"
"#pushButton_3:hover{\n"
"    background-color:orange;\n"
"}")
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_4.setGeometry(QtCore.QRect(280, 0, 15, 15))
        self.pushButton_4.setStyleSheet("background-color: lime;\n"
"border:2px solid gray;\n"
"border-radius:7px;")
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.widget_4 = QtWidgets.QWidget(self.centralwidget)
        self.widget_4.setGeometry(QtCore.QRect(110, 20, 531, 491))
        self.widget_4.setStyleSheet("background-color: rgb(80, 70, 60);\n"
"border:2px solid gray;\n"
"border-top:25px solid gray;\n"
"QPushButton#pushButton:hover {\n"
"background-color: rgb(224, 255, 0);\n"
"border-style: inset;\n"
"}")
        self.widget_4.setObjectName("widget_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.widget_4)
        self.pushButton_5.setGeometry(QtCore.QRect(510, 0, 15, 15))
        self.pushButton_5.setStyleSheet("#pushButton_5{\n"
"background-color:red;\n"
"border:1px solid gray;\n"
"border-radius: 7px;\n"
"}\n"
"#pushButton_5:hover{\n"
"    background-color:orange;\n"
"}")
        self.pushButton_5.setText("")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.widget_4)
        self.pushButton_6.setGeometry(QtCore.QRect(480, 0, 15, 15))
        self.pushButton_6.setStyleSheet("background-color: lime;\n"
"border:1px solid gray;\n"
"border-radius: 7px;")
        self.pushButton_6.setText("")
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalWidget_21 = QtWidgets.QWidget(self.widget_4)
        self.horizontalWidget_21.setGeometry(QtCore.QRect(20, 79, 491, 41))
        self.horizontalWidget_21.setStyleSheet("border:none;")
        self.horizontalWidget_21.setObjectName("horizontalWidget_21")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.horizontalWidget_21)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem3)
        self.comboBox_2 = QtWidgets.QComboBox(self.horizontalWidget_21)
        self.comboBox_2.setMinimumSize(QtCore.QSize(150, 30))
        self.comboBox_2.setStyleSheet("border:1px solid yellow;\n"
"background-color:black;\n"
"padding-left:10px;")
        self.comboBox_2.setObjectName("comboBox_2")
        self.horizontalLayout_7.addWidget(self.comboBox_2)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem4)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem5)
        self.comboBox = QtWidgets.QComboBox(self.horizontalWidget_21)
        self.comboBox.setMinimumSize(QtCore.QSize(150, 30))
        self.comboBox.setStyleSheet("#comboBox{\n"
"border:1px solid yellow;\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"background-color:black;\n"
"padding-left:10px;\n"
"color:white;\n"
"}")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_7.addWidget(self.comboBox)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.playTheMatch = QtWidgets.QPushButton(self.horizontalWidget_21)
        self.playTheMatch.setMinimumSize(QtCore.QSize(50, 28))
        self.playTheMatch.setStyleSheet("#playTheMatch{\n"
"    background-color:lime;\n"
"    color:black;\n"
"    height:22px;\n"
"    margin-top:3px;\n"
"    margin-bottom:3px;\n"
"    border:1px solid black;\n"
"}\n"
"#playTheMatch:hover{\n"
"    background-color:transparent;\n"
"    border:1px solid lime;\n"
"    color:lime;\n"
"}")
        self.playTheMatch.setObjectName("playTheMatch")
        self.horizontalLayout_7.addWidget(self.playTheMatch)
        self.horizontalLayout_7.addItem(spacerItem6)
        self.line = QtWidgets.QFrame(self.widget_4)
        self.line.setGeometry(QtCore.QRect(20, 130, 501, 2))
        self.line.setStyleSheet("background-color:yellow;\n"
"border-top:none;\n"
"border-bottom:1px solid orange;")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.listWidget_3 = QtWidgets.QListWidget(self.widget_4)
        self.listWidget_3.setGeometry(QtCore.QRect(30, 210, 221, 221))
        self.listWidget_3.setStyleSheet("#listWidget_3{\n"
"border:1px solid yellow;\n"
"background-color:black;\n"
"color:white;\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"padding:10px;\n"
"padding-left:20px;\n"
"}\n"
"#listWidget_3::item:selected{\n"
"background-color:yellow;\nborder:none;\n"
"color:black;\n"
"}")
        self.listWidget_3.setObjectName("listWidget_3")
        self.listWidget_4 = QtWidgets.QListWidget(self.widget_4)
        self.listWidget_4.setGeometry(QtCore.QRect(290, 210, 221, 221))
        self.listWidget_4.setStyleSheet("#listWidget_4{\n"
"border:1px solid yellow;\n"
"background-color:black;\n"
"color:blue;\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"padding:10px;\n"
"padding-left:20px;\n"
"}\n"
"#listWidget_4::item:selected{\n"
"background-color:yellow;\nborder:none;\n"
"color:black;\n"
"}")
        self.listWidget_4.setObjectName("listWidget_4")
        self.pushButton_7 = QtWidgets.QPushButton(self.widget_4)
        self.pushButton_7.setGeometry(QtCore.QRect(210, 450, 121, 31))
        self.pushButton_7.setStyleSheet("#pushButton_7{\n"
"border:1px solid lime;\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(59, 78, 95);\n"
"}\n"
"#pushButton_7:hover{\n"
"    background-color:transparent;\n"
"    border-style:inset;\n"
"}")
        self.pushButton_7.setObjectName("pushButton_7")
        self.label_18 = QtWidgets.QLabel(self.widget_4)
        self.label_18.setGeometry(QtCore.QRect(110, 40, 321, 16))
        self.label_18.setStyleSheet("border:none;\n"
"color:orange;\n"
"font: 75 11pt \"MS Shell Dlg 2\";")
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.widget_4)
        self.label_19.setGeometry(QtCore.QRect(30, 180, 71, 16))
        self.label_19.setStyleSheet("border:none;\n"
"color:lime;\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.widget_4)
        self.label_20.setGeometry(QtCore.QRect(290, 180, 47, 13))
        self.label_20.setStyleSheet("border:none;\n"
"color:lime;\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.widget_4)
        self.label_21.setGeometry(QtCore.QRect(340, 180, 61, 14))
        self.label_21.setStyleSheet("color:red;\n"
"border:none;\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.label_21.setObjectName("label_21")
        self.cancelButton = QtWidgets.QPushButton(self.centralwidget)
        self.cancelButton.setGeometry(QtCore.QRect(450, 185, 21, 21))
        self.cancelButton.setMaximumSize(QtCore.QSize(121, 27))
        self.cancelButton.setStyleSheet("#cancelButton{\n"
"background-color:red;\n"
"color:white;\n"
"font: 9pt \"MS Shell Dlg 2\";\n"
"border-radius:13px;\n"
"border-right:1px solid maroon;\n"
"border-bottom:1px solid maroon;\n"
"}\n"
"#cancelButton:hover{\n"
"border:none;\n"
"border-left:1px solid maroon;\n"
"border-top:1px solid maroon;\n"
"}")
        self.cancelButton.setObjectName("cancelButton")
        self.widget_5 = QtWidgets.QWidget(self.centralwidget)
        self.widget_5.setGeometry(QtCore.QRect(219, 160, 321, 171))
        self.widget_5.setStyleSheet("border:2px solid lime;\n"
"border-top:15px solid lime;")
        self.widget_5.setObjectName("widget_5")
        self.label_22 = QtWidgets.QLabel(self.widget_5)
        self.label_22.setGeometry(QtCore.QRect(20, 40, 279, 20))
        self.label_22.setStyleSheet("font: 75 11pt \"MS Shell Dlg 2\";\n"
"border:none;")
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.widget_5)
        self.label_23.setGeometry(QtCore.QRect(120, 80, 61, 51))
        self.label_23.setStyleSheet("font: 57 50pt \"Marlett\";\n"
"color:black;\n"
"background-color:lime;\n"
"border:none;\n"
"border-radius:25px;")
        self.label_23.setObjectName("label_23")
        self.pushButton_8 = QtWidgets.QPushButton(self.widget_5)
        self.pushButton_8.setGeometry(QtCore.QRect(110, 140, 81, 23))
        self.pushButton_8.setStyleSheet("#pushButton_8{\n"
"border:1px solid black;\n"
"color:black;\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"background-color:yellow;\n"
"border-radius:10px;\n"
"}\n"
"#pushButton_8:hover{\n"
"    background-color:transparent;\n"
"    border-style:inset;\n"
"    color:yellow;\n"
"    border:1px solid yellow;\n"
"}")
        self.pushButton_8.setObjectName("pushButton_8")
        self.widget_6 = QtWidgets.QWidget(self.centralwidget)
        self.widget_6.setGeometry(QtCore.QRect(220, 160, 321, 171))
        self.widget_6.setStyleSheet("border:2px solid red;\n"
"border-top:15px solid red;")
        self.widget_6.setObjectName("widget_6")
        self.label_24 = QtWidgets.QLabel(self.widget_6)
        self.label_24.setGeometry(QtCore.QRect(10, 40, 305, 20))
        self.label_24.setStyleSheet("font: 75 11pt \"MS Shell Dlg 2\";\n"
"border:none;")
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.widget_6)
        self.label_25.setGeometry(QtCore.QRect(120, 80, 61, 51))
        self.label_25.setStyleSheet("color:black;\n"
"font: 40pt \"MS Shell Dlg 2\";\n"
"background-color:red;\n"
"border:none;\n"
"border-radius:25px;\n"
"padding-bottom:10px;\n"
"padding-left:5px;")
        self.label_25.setObjectName("label_25")
        self.pushButton_9 = QtWidgets.QPushButton(self.widget_6)
        self.pushButton_9.setGeometry(QtCore.QRect(110, 140, 81, 23))
        self.pushButton_9.setStyleSheet("#pushButton_9{\n"
"border:1px solid black;\n"
"color:black;\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"background-color:orange;\n"
"border-radius:10px;\n"
"}\n"
"#pushButton_9:hover{\n"
"    background-color:transparent;\n"
"    border-style:inset;\n"
"    color:orange;\n"
"    border:1px solid orange;\n"
"}")
        self.pushButton_9.setObjectName("pushButton_9")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 755, 21))
        self.menubar.setStyleSheet("QMenu#menuManage_Teams{background-color:gray;} QMenuBar::item{background-color:black;} QMenuBar::item:selected{background-color:gray;} QMenu::item:selected{background-color:black;}")
        self.menubar.setObjectName("menubar")
        self.menuManage_Teams = QtWidgets.QMenu(self.menubar)
        self.menuManage_Teams.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.menuManage_Teams.setStyleSheet("")
        self.menuManage_Teams.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.menuManage_Teams.setObjectName("menuManage_Teams")
        self.widget_7 = QtWidgets.QWidget(self.centralwidget)
        self.widget_7.setGeometry(QtCore.QRect(180, 159, 391, 231))
        self.widget_7.setStyleSheet("background-color: transparent;")
        self.widget_7.setObjectName("widget_7")
        self.widget_69 = QtWidgets.QWidget(self.widget_7)
        self.widget_69.setGeometry(QtCore.QRect(20, 19, 351, 191))
        self.widget_69.setStyleSheet("background-color:gray;\n"
"border:2px solid lime;")
        self.widget_69.setObjectName("widget_69")
        self.comboBox_3 = QtWidgets.QComboBox(self.widget_69)
        self.comboBox_3.setGeometry(QtCore.QRect(190, 30, 150, 30))
        self.comboBox_3.setMinimumSize(QtCore.QSize(0, 30))
        self.comboBox_3.setStyleSheet("#comboBox_3{\n"
"background-color: black;\n"
"border:1px solid brown;\n"
"padding-left:10px;\n"
"    font: 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"#comboBox_3::item{\n"
"    height:30px;\n"
"    background-color: black;\n"
"    border:none;\n"
"}")
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.label_26 = QtWidgets.QLabel(self.widget_69)
        self.label_26.setGeometry(QtCore.QRect(30, 35, 100, 20))
        self.label_26.setStyleSheet("background-color:transparent;\n"
"border:none;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color:lime;")
        self.label_26.setObjectName("label_26")
        self.line_A = QtWidgets.QFrame(self.widget_7)
        self.line_A.setGeometry(QtCore.QRect(0, 0, 391, 5))
        self.line_A.setStyleSheet("background-color:lime;")
        self.line_A.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_A.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_A.setObjectName("line_A")
        self.line_B = QtWidgets.QFrame(self.widget_7)
        self.line_B.setGeometry(QtCore.QRect(0, 225, 391, 5))
        self.line_B.setStyleSheet("background-color:lime;")
        self.line_B.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_B.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_B.setObjectName("line_B")
        self.line_C = QtWidgets.QFrame(self.widget_7)
        self.line_C.setGeometry(QtCore.QRect(0, 0, 5, 231))
        self.line_C.setStyleSheet("background-color:lime;")
        self.line_C.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_C.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_C.setObjectName("line_C")
        self.line_D = QtWidgets.QFrame(self.widget_7)
        self.line_D.setGeometry(QtCore.QRect(385, 0, 5, 231))
        self.line_D.setStyleSheet("background-color:lime;")
        self.line_D.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_D.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_D.setObjectName("line_D")
        self.pushButton_12 = QtWidgets.QPushButton(self.widget_7)
        self.pushButton_12.setGeometry(QtCore.QRect(150, 200, 90, 30))
        self.pushButton_12.setStyleSheet("#pushButton_12{\n"
"    background-color:yellow;\n"
"    color:black;\n"
"    font: 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"#pushButton_12:hover{\n"
"        background-color:gray;\n"
"        border:1px solid yellow;\n"
"        color:yellow;\n"
"}")
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_10 = QtWidgets.QPushButton(self.widget_7)
        self.pushButton_10.setGeometry(QtCore.QRect(348, 0, 42, 21))
        self.pushButton_10.setStyleSheet("background-color:red;\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.pushButton_10.setObjectName("pushButton_10")
        self.widget_8 = QtWidgets.QWidget(self.centralwidget)
        self.widget_8.setGeometry(QtCore.QRect(60, 19, 633, 521))
        self.widget_8.setStyleSheet("border:2px solid lime;\n"
"border-top:20px solid lime;")
        self.widget_8.setObjectName("widget_8")
        self.label_27 = QtWidgets.QLabel(self.widget_8)
        self.label_27.setGeometry(QtCore.QRect(275, 30, 81, 20))
        self.label_27.setStyleSheet("border:none;\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.label_27.setObjectName("label_27")
        self.line_2 = QtWidgets.QFrame(self.widget_8)
        self.line_2.setGeometry(QtCore.QRect(9, 70, 614, 1))
        self.line_2.setStyleSheet("border:none;\n"
"background-color:black;")
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_28 = QtWidgets.QLabel(self.widget_8)
        self.label_28.setGeometry(QtCore.QRect(80, 50, 61, 16))
        self.label_28.setStyleSheet("border:none;\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.label_28.setObjectName("label_28")
        self.label_29 = QtWidgets.QLabel(self.widget_8)
        self.label_29.setGeometry(QtCore.QRect(150, 50, 61, 16))
        self.label_29.setStyleSheet("border:none;\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"color:skyblue;")
        self.label_29.setObjectName("label_29")
        self.label_30 = QtWidgets.QLabel(self.widget_8)
        self.label_30.setGeometry(QtCore.QRect(430, 50, 71, 16))
        self.label_30.setStyleSheet("border:none;\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.label_30.setObjectName("label_30")
        self.label_31 = QtWidgets.QLabel(self.widget_8)
        self.label_31.setGeometry(QtCore.QRect(500, 50, 61, 16))
        self.label_31.setStyleSheet("border:none;\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"color:skyblue;")
        self.label_31.setObjectName("label_31")
        self.line_3 = QtWidgets.QFrame(self.widget_8)
        self.line_3.setGeometry(QtCore.QRect(9, 104, 614, 1))
        self.line_3.setStyleSheet("border:none;\n"
"background-color:black;")
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.widget_8)
        self.line_4.setGeometry(QtCore.QRect(9, 138, 614, 1))
        self.line_4.setStyleSheet("border:none;\n"
"background-color:black;")
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(self.widget_8)
        self.line_5.setGeometry(QtCore.QRect(9, 172, 614, 1))
        self.line_5.setStyleSheet("border:none;\n"
"background-color:black;")
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(self.widget_8)
        self.line_6.setGeometry(QtCore.QRect(9, 206, 614, 1))
        self.line_6.setStyleSheet("border:none;\n"
"background-color:black;")
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_7 = QtWidgets.QFrame(self.widget_8)
        self.line_7.setGeometry(QtCore.QRect(9, 240, 614, 1))
        self.line_7.setStyleSheet("border:none;\n"
"background-color:black;")
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.line_8 = QtWidgets.QFrame(self.widget_8)
        self.line_8.setGeometry(QtCore.QRect(9, 274, 614, 1))
        self.line_8.setStyleSheet("border:none;\n"
"background-color:black;")
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.line_9 = QtWidgets.QFrame(self.widget_8)
        self.line_9.setGeometry(QtCore.QRect(9, 308, 614, 1))
        self.line_9.setStyleSheet("border:none;\n"
"background-color:black;")
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.line_10 = QtWidgets.QFrame(self.widget_8)
        self.line_10.setGeometry(QtCore.QRect(9, 342, 614, 1))
        self.line_10.setStyleSheet("border:none;\n"
"background-color:black;")
        self.line_10.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.line_11 = QtWidgets.QFrame(self.widget_8)
        self.line_11.setGeometry(QtCore.QRect(9, 376, 614, 1))
        self.line_11.setStyleSheet("border:none;\n"
"background-color:black;")
        self.line_11.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.line_12 = QtWidgets.QFrame(self.widget_8)
        self.line_12.setGeometry(QtCore.QRect(9, 410, 614, 1))
        self.line_12.setStyleSheet("border:none;\n"
"background-color:black;")
        self.line_12.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_12.setObjectName("line_12")
        self.line_13 = QtWidgets.QFrame(self.widget_8)
        self.line_13.setGeometry(QtCore.QRect(9, 444, 614, 1))
        self.line_13.setStyleSheet("border:none;\n"
"background-color:black;")
        self.line_13.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_13.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_13.setObjectName("line_13")
        self.line_14 = QtWidgets.QFrame(self.widget_8)
        self.line_14.setGeometry(QtCore.QRect(9, 478, 614, 1))
        self.line_14.setStyleSheet("border:none;\n"
"background-color:black;")
        self.line_14.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_14.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_14.setObjectName("line_14")
        self.line_15 = QtWidgets.QFrame(self.widget_8)
        self.line_15.setGeometry(QtCore.QRect(9, 70, 1, 408))
        self.line_15.setStyleSheet("border:none;\n"
"background-color:black;")
        self.line_15.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_15.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_15.setObjectName("line_15")
        self.line_16 = QtWidgets.QFrame(self.widget_8)
        self.line_16.setGeometry(QtCore.QRect(94, 70, 1, 408))
        self.line_16.setStyleSheet("border:none;\n"
"background-color:black;")
        self.line_16.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_16.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_16.setObjectName("line_16")
        self.line_17 = QtWidgets.QFrame(self.widget_8)
        self.line_17.setGeometry(QtCore.QRect(142, 70, 1, 408))
        self.line_17.setStyleSheet("border:none;\n"
"background-color:black;")
        self.line_17.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_17.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_17.setObjectName("line_17")
        self.line_18 = QtWidgets.QFrame(self.widget_8)
        self.line_18.setGeometry(QtCore.QRect(190, 70, 1, 408))
        self.line_18.setStyleSheet("border:none;\n"
"background-color:black;")
        self.line_18.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_18.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_18.setObjectName("line_18")
        self.line_19 = QtWidgets.QFrame(self.widget_8)
        self.line_19.setGeometry(QtCore.QRect(238, 70, 1, 408))
        self.line_19.setStyleSheet("border:none;\n"
"background-color:black;")
        self.line_19.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_19.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_19.setObjectName("line_19")
        self.line_20 = QtWidgets.QFrame(self.widget_8)
        self.line_20.setGeometry(QtCore.QRect(286, 70, 1, 408))
        self.line_20.setStyleSheet("border:none;\n"
"background-color:black;")
        self.line_20.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_20.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_20.setObjectName("line_20")
        self.line_21 = QtWidgets.QFrame(self.widget_8)
        self.line_21.setGeometry(QtCore.QRect(337, 70, 1, 408))
        self.line_21.setStyleSheet("border:none;\n"
"background-color:black;")
        self.line_21.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_21.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_21.setObjectName("line_21")
        self.line_22 = QtWidgets.QFrame(self.widget_8)
        self.line_22.setGeometry(QtCore.QRect(385, 70, 1, 408))
        self.line_22.setStyleSheet("border:none;\n"
"background-color:black;")
        self.line_22.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_22.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_22.setObjectName("line_22")
        self.line_23 = QtWidgets.QFrame(self.widget_8)
        self.line_23.setGeometry(QtCore.QRect(433, 70, 1, 408))
        self.line_23.setStyleSheet("border:none;\n"
"background-color:black;")
        self.line_23.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_23.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_23.setObjectName("line_23")
        self.line_24 = QtWidgets.QFrame(self.widget_8)
        self.line_24.setGeometry(QtCore.QRect(481, 70, 1, 408))
        self.line_24.setStyleSheet("border:none;\n"
"background-color:black;")
        self.line_24.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_24.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_24.setObjectName("line_24")
        self.line_25 = QtWidgets.QFrame(self.widget_8)
        self.line_25.setGeometry(QtCore.QRect(529, 70, 1, 408))
        self.line_25.setStyleSheet("border:none;\n"
"background-color:black;")
        self.line_25.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_25.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_25.setObjectName("line_25")
        self.line_26 = QtWidgets.QFrame(self.widget_8)
        self.line_26.setGeometry(QtCore.QRect(577, 70, 1, 408))
        self.line_26.setStyleSheet("border:none;\n"
"background-color:black;")
        self.line_26.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_26.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_26.setObjectName("line_26")
        self.line_27 = QtWidgets.QFrame(self.widget_8)
        self.line_27.setGeometry(QtCore.QRect(623, 70, 1, 408))
        self.line_27.setStyleSheet("border:none;\n"
"background-color:black;")
        self.line_27.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_27.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_27.setObjectName("line_27")
        self.label_32 = QtWidgets.QLabel(self.widget_8)
        self.label_32.setGeometry(QtCore.QRect(40, 80, 30, 13))
        self.label_32.setStyleSheet("border:none;\n"
"color:orange;")
        self.label_32.setObjectName("label_32")
        self.label_33 = QtWidgets.QLabel(self.widget_8)
        self.label_33.setGeometry(QtCore.QRect(150, 80, 32, 13))
        self.label_33.setStyleSheet("border:none;\n"
"color: rgb(157, 188, 235);")
        self.label_33.setObjectName("label_33")
        self.label_34 = QtWidgets.QLabel(self.widget_8)
        self.label_34.setGeometry(QtCore.QRect(200, 80, 30, 13))
        self.label_34.setStyleSheet("border:none;\n"
"color: rgb(157, 188, 235);")
        self.label_34.setObjectName("label_34")
        self.label_35 = QtWidgets.QLabel(self.widget_8)
        self.label_35.setGeometry(QtCore.QRect(250, 80, 30, 13))
        self.label_35.setStyleSheet("border:none;\n"
"color: rgb(157, 188, 235);")
        self.label_35.setObjectName("label_35")
        self.label_36 = QtWidgets.QLabel(self.widget_8)
        self.label_36.setGeometry(QtCore.QRect(295, 80, 35, 13))
        self.label_36.setStyleSheet("border:none;\n"
"color: rgb(157, 188, 235);")
        self.label_36.setObjectName("label_36")
        self.label_37 = QtWidgets.QLabel(self.widget_8)
        self.label_37.setGeometry(QtCore.QRect(345, 80, 35, 13))
        self.label_37.setStyleSheet("border:none;\n"
"color: rgb(157, 188, 235);")
        self.label_37.setObjectName("label_37")
        self.label_38 = QtWidgets.QLabel(self.widget_8)
        self.label_38.setGeometry(QtCore.QRect(440, 80, 40, 13))
        self.label_38.setStyleSheet("border:none;\n"
"color: rgb(157, 188, 235);")
        self.label_38.setObjectName("label_38")
        self.label_39 = QtWidgets.QLabel(self.widget_8)
        self.label_39.setGeometry(QtCore.QRect(533, 80, 43, 13))
        self.label_39.setStyleSheet("border:none;\n"
"color: rgb(157, 188, 235);")
        self.label_39.setObjectName("label_39")
        self.label_40 = QtWidgets.QLabel(self.widget_8)
        self.label_40.setGeometry(QtCore.QRect(395, 80, 30, 13))
        self.label_40.setStyleSheet("border:none;\n"
"color: rgb(157, 188, 235);")
        self.label_40.setObjectName("label_40")
        self.label_41 = QtWidgets.QLabel(self.widget_8)
        self.label_41.setGeometry(QtCore.QRect(485, 80, 40, 13))
        self.label_41.setStyleSheet("border:none;\n"
"color: rgb(157, 188, 235);")
        self.label_41.setObjectName("label_41")
        self.label_42 = QtWidgets.QLabel(self.widget_8)
        self.label_42.setGeometry(QtCore.QRect(585, 80, 30, 13))
        self.label_42.setStyleSheet("border:none;\n"
"color: rgb(157, 188, 235);")
        self.label_42.setObjectName("label_42")
        self.label_43 = QtWidgets.QLabel(self.widget_8)
        self.label_43.setGeometry(QtCore.QRect(102, 80, 36, 13))
        self.label_43.setStyleSheet("border:none;\n"
"color: rgb(157, 188, 235);")
        self.label_43.setObjectName("label_43")
        create_scoretext(self)
        self.cancel_match = QtWidgets.QPushButton(self.widget_8)
        self.cancel_match.setGeometry(QtCore.QRect(240, 490, 90, 23))
        self.cancel_match.setStyleSheet("#cancel_match{\n"
"border:1px solid skyblue;\n"
"color:skyblue;\n"
"}\n"
"#cancel_match:hover{\n"
"border:none;\n"
"color:white;\n"
"background-color:orange;\n"
"}")
        self.cancel_match.setObjectName("cancel_match")
        self.save_match = QtWidgets.QPushButton(self.widget_8)
        self.save_match.setGeometry(QtCore.QRect(340, 490, 90, 23))
        self.save_match.setStyleSheet("#save_match{\n"
"border:1px solid skyblue;\n"
"color:skyblue;\n"
"}\n"
"#save_match:hover{\n"
"border:none;\n"
"color:white;\n"
"background-color: rgb(2, 197, 41);\n"
"}")
        self.save_match.setObjectName("save_match")
        MainWindow.setMenuBar(self.menubar)
        self.actionNew_Team = QtWidgets.QAction(MainWindow)
        self.actionNew_Team.setObjectName("actionNew_Team")
        self.actionOpen_Team = QtWidgets.QAction(MainWindow)
        self.actionOpen_Team.setObjectName("actionOpen_Team")
        self.actionSave_Team = QtWidgets.QAction(MainWindow)
        self.actionSave_Team.setObjectName("actionSave_Team")
        self.actionEvaluate_Team = QtWidgets.QAction(MainWindow)
        self.actionEvaluate_Team.setObjectName("actionEvaluate_Team")
        self.actionEvaluate_Team_2 = QtWidgets.QAction(MainWindow)
        self.actionEvaluate_Team_2.setObjectName("actionEvaluate_Team_2")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionQuit_2 = QtWidgets.QAction(MainWindow)
        self.actionQuit_2.setObjectName("actionQuit_2")
        self.menuManage_Teams.addAction(self.actionNew_Team)
        self.menuManage_Teams.addAction(self.actionOpen_Team)
        self.menuManage_Teams.addAction(self.actionSave_Team)
        self.menuManage_Teams.addSeparator()
        self.menuManage_Teams.addAction(self.actionEvaluate_Team_2)
        self.menuManage_Teams.addAction(self.actionQuit_2)
        self.menubar.addAction(self.menuManage_Teams.menuAction())
        self.radio_BAT=self.radioButton_2
        self.radio_BWL=self.radioButton_3
        self.radio_AR=self.radioButton
        self.radio_WK=self.radioButton_4

        self.retranslateUi(MainWindow)
        self.actionNew_Team.triggered.connect(lambda : newTeam_dialog(self,"open"))
        self.pushButton_2.clicked.connect(lambda : newTeam_dialog(self,"close"))
        self.pushButton_3.clicked.connect(lambda : newTeam_dialog(self,"close"))
        self.pushButton.clicked.connect(lambda : newTeam_dialog(self,"close",1))
        self.lineEdit.returnPressed.connect(lambda : newTeam_dialog(self,"close",1))
        self.actionEvaluate_Team_2.triggered.connect(lambda : show_evteam(self,1))
        self.pushButton_5.clicked.connect(lambda : show_evteam(self,2))
        self.actionQuit_2.triggered.connect(MainWindow.close)
        self.actionSave_Team.triggered.connect(lambda : save_team(self,"open"))
        self.pushButton_8.clicked.connect(lambda : save_team(self,"close"))
        self.pushButton_9.clicked.connect(lambda : error_dialog(self,"close"))
        self.radio_BAT.clicked.connect(lambda : self.addPlayers(1))
        self.radio_BWL.clicked.connect(lambda : self.addPlayers(2))
        self.radio_AR.clicked.connect(lambda : self.addPlayers(3))
        self.radio_WK.clicked.connect(lambda : self.addPlayers(4))
        self.listWidget.itemDoubleClicked.connect(self.addPlayer_toTeam)
        self.listWidget_2.itemDoubleClicked.connect(self.removePlayer)
        self.actionOpen_Team.triggered.connect(lambda : openteam(self,"open"))
        self.pushButton_12.clicked.connect(lambda : openteam(self,"close",1))
        self.pushButton_10.clicked.connect(lambda : openteam(self,"close"))
        self.comboBox.activated['int'].connect(lambda : play_thematch(self,"showButton"))
        self.comboBox_2.activated['int'].connect(self.fill_thelist)
        self.playTheMatch.clicked.connect(lambda : play_thematch(self,"play"))
        self.cancelButton.clicked.connect(self.reset_everything)
        self.cancel_match.clicked.connect(lambda : myscore_board(self,"cancel"))
        self.save_match.clicked.connect(lambda : myscore_board(self,"save"))
        self.pushButton_7.clicked.connect(lambda : calculate_points(self))
        self.radio_BAT.setChecked(True)
        self.widget_4.hide()
        self.widget_3.hide()
        self.widget_5.hide()
        self.widget_6.hide()
        self.widget_7.hide()
        self.widget_8.hide()
        self.cancelButton.hide()
        self.playTheMatch.hide()
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_5.setText(_translate("MainWindow", "Your Selections"))
        self.label_4.setText(_translate("MainWindow", "Batsman (BAT):"))
        self.label_6.setText(_translate("MainWindow", "0"))
        self.label.setText(_translate("MainWindow", "Bowlers (BOW):"))
        self.label_7.setText(_translate("MainWindow", "0"))
        self.label_2.setText(_translate("MainWindow", "Allrounders (AR):"))
        self.label_8.setText(_translate("MainWindow", "0"))
        self.label_3.setText(_translate("MainWindow", "Wicket-Keeper (WK):"))
        self.label_9.setText(_translate("MainWindow", "0"))
        self.radioButton_2.setText(_translate("MainWindow", "BAT"))
        self.radioButton_3.setText(_translate("MainWindow", "BOW"))
        self.radioButton.setText(_translate("MainWindow", "AR"))
        self.radioButton_4.setText(_translate("MainWindow", "WK"))
        self.label_12.setText(_translate("MainWindow", "Team Name :"))
        self.label_11.setText(_translate("MainWindow", "---"))
        self.label_10.setText(_translate("MainWindow", ">>>"))
        self.label_14.setText(_translate("MainWindow", "Points Available :"))
        self.label_15.setText(_translate("MainWindow", "1000"))
        self.label_16.setText(_translate("MainWindow", "Points Used :"))
        self.label_13.setText(_translate("MainWindow", "0"))
        self.label_17.setText(_translate("MainWindow", "Enter Team Name :"))
        self.pushButton_2.setText(_translate("MainWindow", "Cancel"))
        self.pushButton.setText(_translate("MainWindow", "OK"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Match 1"))
        self.comboBox.setItemText(1, _translate("MainWindow", "+ Play a New Match"))
        self.playTheMatch.setText(_translate("MainWindow", "Play"))
        self.pushButton_7.setText(_translate("MainWindow", "Calculate"))
        self.label_18.setText(_translate("MainWindow", "Evaluate the Performance of your Fantasy Team"))
        self.label_19.setText(_translate("MainWindow", "Players"))
        self.label_20.setText(_translate("MainWindow", "Points :"))
        self.label_21.setText(_translate("MainWindow", "0"))
        self.label_22.setText(_translate("MainWindow", "Your Team has been Saved Successfully !"))
        self.label_23.setText(_translate("MainWindow", "b"))
        self.pushButton_8.setText(_translate("MainWindow", "OK"))
        self.label_24.setText(_translate("MainWindow", "This Match has been played by another Team !"))
        self.label_25.setText(_translate("MainWindow", "x"))
        self.pushButton_9.setText(_translate("MainWindow", "OK"))
        self.label_26.setText(_translate("MainWindow", "Open Team:"))
        self.pushButton_12.setText(_translate("MainWindow", "Open"))
        self.pushButton_10.setText(_translate("MainWindow", "X"))
        self.cancelButton.setText(_translate("MainWindow", "X"))
        self.label_27.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" text-decoration: underline;\">Scoreboard</span></p></body></html>"))
        self.label_28.setText(_translate("MainWindow", "Match_id :"))
        self.label_29.setText(_translate("MainWindow", "---"))
        self.label_30.setText(_translate("MainWindow", "Played By :"))
        self.label_31.setText(_translate("MainWindow", "---"))
        self.label_32.setText(_translate("MainWindow", "Player"))
        self.label_33.setText(_translate("MainWindow", "Faced"))
        self.label_34.setText(_translate("MainWindow", "Fours"))
        self.label_35.setText(_translate("MainWindow", "Sixes"))
        self.label_36.setText(_translate("MainWindow", "Bowled"))
        self.label_37.setText(_translate("MainWindow", "Maiden"))
        self.label_38.setText(_translate("MainWindow", "Wickets"))
        self.label_39.setText(_translate("MainWindow", "Stumping"))
        self.label_40.setText(_translate("MainWindow", "Given"))
        self.label_41.setText(_translate("MainWindow", "Catches"))
        self.label_42.setText(_translate("MainWindow", "R_out"))
        self.label_43.setText(_translate("MainWindow", "Scored"))
        self.cancel_match.setText(_translate("MainWindow", "Cancel"))
        self.save_match.setText(_translate("MainWindow", "Save"))
        self.menuManage_Teams.setTitle(_translate("MainWindow", "Manage Teams"))
        self.actionNew_Team.setText(_translate("MainWindow", "New Team"))
        self.actionOpen_Team.setText(_translate("MainWindow", "Open Team"))
        self.actionSave_Team.setText(_translate("MainWindow", "Save Team"))
        self.actionEvaluate_Team.setText(_translate("MainWindow", "Evaluate Team"))
        self.actionEvaluate_Team_2.setText(_translate("MainWindow", "Evaluate Team"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionQuit_2.setText(_translate("MainWindow", "Quit"))

    def colorChange(self):
        if int(self.label_15.text())>=750:
            self.label_15.setStyleSheet("color:lime;\n"
    "font: 57 12pt \"Yu Gothic Medium\";")
        elif int(self.label_15.text())>=500 and int(self.label_15.text())<750:
            self.label_15.setStyleSheet("color:yellow;\n"
    "font: 57 12pt \"Yu Gothic Medium\";")
        elif int(self.label_15.text())>=250 and int(self.label_15.text())<500:
            self.label_15.setStyleSheet("color:orange;\n"
    "font: 57 12pt \"Yu Gothic Medium\";")
        elif int(self.label_15.text())<250:
            self.label_15.setStyleSheet("color:red;\n"
    "font: 57 12pt \"Yu Gothic Medium\";")
        if int(self.label_13.text())>=750:
            self.label_13.setStyleSheet("color:lime;\n"
    "font: 57 12pt \"Yu Gothic Medium\";")
        elif int(self.label_13.text())>=500 and int(self.label_15.text())<750:
            self.label_13.setStyleSheet("color:yellow;\n"
    "font: 57 12pt \"Yu Gothic Medium\";")
        elif int(self.label_13.text())>=250 and int(self.label_15.text())<500:
            self.label_13.setStyleSheet("color:orange;\n"
    "font: 57 12pt \"Yu Gothic Medium\";")
        elif int(self.label_13.text())<250:
            self.label_13.setStyleSheet("color:red;\n"
    "font: 57 12pt \"Yu Gothic Medium\";")

    def addPlayers(self,act):
        self.myplayers= sqlite3.connect('fantasy_cricket.db')
        self.cur_players= self.myplayers.cursor()
        self.listWidget.clear()
        if act==1:
            self.cur_players.execute("select player from stats where ctg like 'BAT'")
        elif act==2:
            self.cur_players.execute("select player from stats where ctg like 'BWL'")
        elif act==3:
            self.cur_players.execute("select player from stats where ctg like 'AR'")
        elif act==4:
            self.cur_players.execute("select player from stats where ctg like 'WK'")
        result= self.cur_players.fetchall()
        for player in result:
            item=QtWidgets.QListWidgetItem(player[0])
            self.listWidget.addItem(item)
        self.colorChange()

    def addPlayer_toTeam(self,item):
        flag=False
        if self.label_11.text()!="---":
            if self.listWidget_2.count()>0:
                for i in range(self.listWidget_2.count()):
                    if self.listWidget_2.item(i).text()==item.text():
                        flag=True
            if flag==False and self.listWidget_2.count()<11:
                i_tem=QtWidgets.QListWidgetItem(item.text())
                #----------points----------
                self.cur_players.execute("select value from stats where player like ?;",(item.text(),))
                value=self.cur_players.fetchone()
                toset=int(self.label_13.text())+value[0]
                self.label_13.setText(str(toset))
                toset=1000-int(self.label_13.text())
                self.label_15.setText(str(toset))
                #--------catagory numbers----------
                self.cur_players.execute("select ctg from stats where player like ?;",(item.text(),))
                ct=self.cur_players.fetchone()
                ctg=ct[0]
                if ctg=="BAT":
                    self.label_6.setText(str(int(self.label_6.text())+1))
                    self.listWidget_2.addItem(i_tem)
                elif ctg=="BWL":
                    if int(self.label_7.text())<=7:
                        self.label_7.setText(str(int(self.label_7.text())+1))
                        self.listWidget_2.addItem(i_tem)
                    else:
                        error_dialog(self,"open","Too many Bowlers!")
                elif ctg=="AR":
                    self.label_8.setText(str(int(self.label_8.text())+1))
                    self.listWidget_2.addItem(i_tem)
                elif ctg=="WK":
                    if self.label_9.text()=="0":
                        self.label_9.setText(str(int(self.label_9.text())+1))
                        self.listWidget_2.addItem(i_tem)
                    else:
                        error_dialog(self,"open","Wicket-Keeper can't be more than one!")

            elif flag==True:
                error_dialog(self,"open","This Player is already selected !")
            elif self.listWidget_2.count()>=11:
                error_dialog(self,"open","A Cricket Team has 11 players")
        else:
            newTeam_dialog(self,"open")
        self.colorChange()

    def removePlayer(self,item):
        self.listWidget_2.takeItem(self.listWidget_2.row(item))
        self.cur_players.execute("select value from stats where player like ?;",(item.text(),))
        value=self.cur_players.fetchone()
        toset=int(self.label_13.text())-value[0]
        self.label_13.setText(str(toset))
        toset=1000-int(self.label_13.text())
        self.label_15.setText(str(toset))
        self.cur_players.execute("select ctg from stats where player like ?;",(item.text(),))
        ct=self.cur_players.fetchone()
        ctg=ct[0]
        if ctg=="BAT":
            self.label_6.setText(str(int(self.label_6.text())-1))
        elif ctg=="BWL":
            self.label_7.setText(str(int(self.label_7.text())-1))
        elif ctg=="AR":
            self.label_8.setText(str(int(self.label_8.text())-1))
        elif ctg=="WK":
            self.label_9.setText(str(int(self.label_9.text())-1))
        self.colorChange()
    def fill_thelist(self):
        self.listWidget_3.clear()
        team_name=self.comboBox_2.currentText()
        self.cur_players.execute("select players from teams where name like ?;",(team_name,))
        get_players=self.cur_players.fetchone()
        player_str=get_players[0]
        player_list=json.loads(player_str)
        for player in player_list:
            self.listWidget_3.addItem(player)
        self.listWidget_4.clear()
        for i in range(len(player_list)):
            self.listWidget_4.addItem("0")
        self.label_21.setText("0")

    def reset_everything(self):
        self.listWidget_2.clear()
        self.label_6.setText("0")
        self.label_7.setText("0")
        self.label_8.setText("0")
        self.label_9.setText("0")
        self.label_13.setText("0")
        self.label_15.setText("1000")
        self.label_11.setText("---")
        self.cancelButton.hide()
        self.comboBox.clear()
        self.cur_players.execute("select match_id from match_played")
        match_list=self.cur_players.fetchall()
        for match in match_list:
            self.comboBox.addItem(match[0])
        self.comboBox.addItem("+ Play a New Match")
        self.playTheMatch.hide()
        self.colorChange()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.addPlayers(1)
    MainWindow.setWindowTitle(' Fantasy Cricket')
    MainWindow.setWindowIcon(QtGui.QIcon('cric.png'))
    MainWindow.show()
    sys.exit(app.exec_())
