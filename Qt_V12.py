import os
import re
import sys
import shutil
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QTimer, QDir, QDate, Qt, QObject
from PyQt6.QtWidgets import QFileDialog, QMessageBox, QInputDialog, QApplication, QMainWindow


class Ui_AutoFolder(object):
        def setupUi(self, AutoFolder):
                AutoFolder.setObjectName("AutoFolder")
                AutoFolder.setEnabled(True)
                AutoFolder.resize(898, 671)
                AutoFolder.setMinimumSize(QtCore.QSize(898, 671))
                AutoFolder.setMaximumSize(QtCore.QSize(898, 671))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
                AutoFolder.setFont(font)
                AutoFolder.setMouseTracking(False)
                AutoFolder.setAcceptDrops(False)
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap("images\Folder_Icon3.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
                AutoFolder.setWindowIcon(icon)
                AutoFolder.setWhatsThis("")
                AutoFolder.setAutoFillBackground(True)
                self.label = QtWidgets.QLabel(parent=AutoFolder)
                self.label.setGeometry(QtCore.QRect(30, 11, 261, 91))
                self.label.setText("")
                self.label.setPixmap(QtGui.QPixmap("images\LSG_Sky_Chefs_logo.svg.png"))
                self.label.setScaledContents(True)
                self.label.setObjectName("label")
                self.label_2 = QtWidgets.QLabel(parent=AutoFolder)
                self.label_2.setGeometry(QtCore.QRect(648, 0, 251, 141))
                self.label_2.setText("")
                self.label_2.setPixmap(QtGui.QPixmap("images\maxresdefault.jpg"))
                self.label_2.setScaledContents(True)
                self.label_2.setObjectName("label_2")
                self.widget = QtWidgets.QWidget(parent=AutoFolder)
                self.widget.setGeometry(QtCore.QRect(0, 640, 911, 31))
                self.widget.setStyleSheet("background-color: #f5f5f5; /* Slighter light gray background color */\n"
        "border: none; /* Remove border */\n"
        "padding: 5px; /* Add padding for content spacing */\n"
        "color: #555555; /* Slighter text color */\n"
        "")
                self.widget.setObjectName("widget")
                self.Status_Label = QtWidgets.QLabel(parent=self.widget)
                self.Status_Label.setGeometry(QtCore.QRect(7, 0, 91, 31))
                font = QtGui.QFont()
                font.setPointSize(9)
                font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
                self.Status_Label.setFont(font)
                self.Status_Label.setObjectName("Status_Label")
                self.Version_Label = QtWidgets.QLabel(parent=self.widget)
                self.Version_Label.setGeometry(QtCore.QRect(800, 3, 91, 25))
                font = QtGui.QFont()
                font.setPointSize(9)
                font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
                self.Version_Label.setFont(font)
                self.Version_Label.setObjectName("Version_Label")
                self.tabWidget = QtWidgets.QTabWidget(parent=AutoFolder)
                self.tabWidget.setEnabled(True)
                self.tabWidget.setGeometry(QtCore.QRect(0, 115, 901, 531))
                self.tabWidget.setAutoFillBackground(False)
                self.tabWidget.setTabShape(QtWidgets.QTabWidget.TabShape.Triangular)
                self.tabWidget.setMovable(False)
                self.tabWidget.setObjectName("tabWidget")
                self.tab1 = QtWidgets.QWidget()
                self.tab1.setAutoFillBackground(True)
                self.tab1.setObjectName("tab1")
                self.tab1_NA_Button = QtWidgets.QRadioButton(parent=self.tab1)
                self.tab1_NA_Button.setGeometry(QtCore.QRect(560, 172, 101, 41))
                font = QtGui.QFont()
                font.setFamily("Lufthansa Roman")
                font.setPointSize(12)
                font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
                self.tab1_NA_Button.setFont(font)
                self.tab1_NA_Button.setChecked(True)
                self.tab1_NA_Button.setObjectName("tab1_NA_Button")
                self.buttonGroup1 = QtWidgets.QButtonGroup(AutoFolder)
                self.buttonGroup1.setObjectName("buttonGroup1")
                self.buttonGroup1.addButton(self.tab1_NA_Button)
                self.tab1_Other_Button = QtWidgets.QRadioButton(parent=self.tab1)
                self.tab1_Other_Button.setGeometry(QtCore.QRect(560, 130, 71, 41))
                font = QtGui.QFont()
                font.setFamily("Lufthansa Roman")
                font.setPointSize(12)
                font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
                self.tab1_Other_Button.setFont(font)
                self.tab1_Other_Button.setChecked(False)
                self.tab1_Other_Button.setObjectName("tab1_Other_Button")
                self.buttonGroup1.addButton(self.tab1_Other_Button)
                self.tab1_Multi_CSC_Button = QtWidgets.QRadioButton(parent=self.tab1)
                self.tab1_Multi_CSC_Button.setGeometry(QtCore.QRect(505, 247, 121, 31))
                font = QtGui.QFont()
                font.setFamily("Lufthansa Roman")
                font.setPointSize(11)
                font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
                self.tab1_Multi_CSC_Button.setFont(font)
                self.tab1_Multi_CSC_Button.setObjectName("tab1_Multi_CSC_Button")
                self.tab1_textEdit_6 = QtWidgets.QTextEdit(parent=self.tab1)
                self.tab1_textEdit_6.setGeometry(QtCore.QRect(285, 322, 221, 31))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(False)
                font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
                self.tab1_textEdit_6.setFont(font)
                self.tab1_textEdit_6.setAutoFillBackground(True)
                self.tab1_textEdit_6.setStyleSheet("background-color: transparent;\n"
        "border: none;\n"
        "")
                self.tab1_textEdit_6.setReadOnly(True)
                self.tab1_textEdit_6.setObjectName("tab1_textEdit_6")
                self.tab1_textEdit_5 = QtWidgets.QTextEdit(parent=self.tab1)
                self.tab1_textEdit_5.setGeometry(QtCore.QRect(625, 249, 211, 31))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
                self.tab1_textEdit_5.setFont(font)
                self.tab1_textEdit_5.setAutoFillBackground(True)
                self.tab1_textEdit_5.setStyleSheet("background-color: transparent;\n"
        "border: none;\n"
        "")
                self.tab1_textEdit_5.setReadOnly(True)
                self.tab1_textEdit_5.setObjectName("tab1_textEdit_5")
                self.tab1_textEdit_8 = QtWidgets.QTextEdit(parent=self.tab1)
                self.tab1_textEdit_8.setGeometry(QtCore.QRect(320, 393, 301, 31))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(False)
                font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
                self.tab1_textEdit_8.setFont(font)
                self.tab1_textEdit_8.setAutoFillBackground(True)
                self.tab1_textEdit_8.setStyleSheet("background-color: transparent;\n"
        "border: none;\n"
        "")
                self.tab1_textEdit_8.setReadOnly(True)
                self.tab1_textEdit_8.setObjectName("tab1_textEdit_8")
                self.tab1_Profitability_Button = QtWidgets.QRadioButton(parent=self.tab1)
                self.tab1_Profitability_Button.setGeometry(QtCore.QRect(120, 172, 141, 41))
                font = QtGui.QFont()
                font.setFamily("Lufthansa Roman")
                font.setPointSize(12)
                font.setBold(False)
                font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
                self.tab1_Profitability_Button.setFont(font)
                self.tab1_Profitability_Button.setObjectName("tab1_Profitability_Button")
                self.buttonGroup1.addButton(self.tab1_Profitability_Button)
                self.tab1_buttonBox = QtWidgets.QDialogButtonBox(parent=self.tab1)
                self.tab1_buttonBox.setGeometry(QtCore.QRect(710, 460, 151, 31))
                self.tab1_buttonBox.setMaximumSize(QtCore.QSize(171, 16777215))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
                self.tab1_buttonBox.setFont(font)
                self.tab1_buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
                self.tab1_buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Ok)
                self.tab1_buttonBox.setObjectName("tab1_buttonBox")
                font = QtGui.QFont()
                font.setFamily("Lufthansa Roman")
                font.setPointSize(12)
                font.setBold(False)
                font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
                self.tab1_textEdit_7 = QtWidgets.QTextEdit(parent=self.tab1)
                self.tab1_textEdit_7.setEnabled(True)
                self.tab1_textEdit_7.setGeometry(QtCore.QRect(290, 30, 181, 31))
                self.tab1_textEdit_7.setAutoFillBackground(True)
                self.tab1_textEdit_7.setStyleSheet("background-color: transparent;\n"
        "border: none;\n"
        "")
                self.tab1_textEdit_7.setReadOnly(True)
                self.tab1_textEdit_7.setObjectName("tab1_textEdit_7")
                self.tab1_PreMp_Button = QtWidgets.QRadioButton(parent=self.tab1)
                self.tab1_PreMp_Button.setGeometry(QtCore.QRect(350, 88, 141, 41))
                font = QtGui.QFont()
                font.setFamily("Lufthansa Roman")
                font.setPointSize(12)
                font.setBold(False)
                font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
                self.tab1_PreMp_Button.setFont(font)
                self.tab1_PreMp_Button.setObjectName("tab1_PreMp_Button")
                self.buttonGroup1.addButton(self.tab1_PreMp_Button)
                self.tab1_line_2 = QtWidgets.QFrame(parent=self.tab1)
                self.tab1_line_2.setGeometry(QtCore.QRect(30, 70, 831, 21))
                self.tab1_line_2.setLineWidth(1)
                self.tab1_line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
                self.tab1_line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
                self.tab1_line_2.setObjectName("tab1_line_2")
                self.tab1_PostMp_Button = QtWidgets.QRadioButton(parent=self.tab1)
                self.tab1_PostMp_Button.setGeometry(QtCore.QRect(350, 130, 141, 41))
                font = QtGui.QFont()
                font.setFamily("Lufthansa Roman")
                font.setPointSize(12)
                font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
                self.tab1_PostMp_Button.setFont(font)
                self.tab1_PostMp_Button.setObjectName("tab1_PostMp_Button")
                self.buttonGroup1.addButton(self.tab1_PostMp_Button)
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
                self.tab1_line_5 = QtWidgets.QFrame(parent=self.tab1)
                self.tab1_line_5.setGeometry(QtCore.QRect(0, -8, 895, 21))
                self.tab1_line_5.setStyleSheet("QFrame#verticalSeparator {\n"
        "    border: 1px dotted #007bff; /* Border style */\n"
        "    height: 50px; /* Set the height for vertical separator */\n"
        "}\n"
        "")
                self.tab1_line_5.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
                self.tab1_line_5.setLineWidth(5)
                self.tab1_line_5.setFrameShape(QtWidgets.QFrame.Shape.HLine)
                self.tab1_line_5.setObjectName("tab1_line_5")
                self.tab1_CSC_Other_Box = QtWidgets.QLineEdit(parent=self.tab1)
                self.tab1_CSC_Other_Box.setEnabled(False)
                self.tab1_CSC_Other_Box.setGeometry(QtCore.QRect(630, 133, 161, 31))
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.tab1_CSC_Other_Box.sizePolicy().hasHeightForWidth())
                self.tab1_CSC_Other_Box.setSizePolicy(sizePolicy)
                font = QtGui.QFont()
                font.setFamily("Lufthansa Roman")
                font.setPointSize(11)
                font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferDefault)
                self.tab1_CSC_Other_Box.setFont(font)
                self.tab1_CSC_Other_Box.setStyleSheet("")
                self.tab1_CSC_Other_Box.setMaxLength(25)
                self.tab1_CSC_Other_Box.setObjectName("tab1_CSC_Other_Box")
                self.tab1_textEdit_3 = QtWidgets.QTextEdit(parent=self.tab1)
                self.tab1_textEdit_3.setGeometry(QtCore.QRect(90, 250, 31, 31))
                self.tab1_textEdit_3.setAutoFillBackground(True)
                self.tab1_textEdit_3.setStyleSheet("background-color: transparent;\n"
        "border: none;\n"
        "")
                self.tab1_textEdit_3.setReadOnly(True)
                self.tab1_textEdit_3.setObjectName("tab1_textEdit_3")
                self.tab1_Price_Action_Button = QtWidgets.QRadioButton(parent=self.tab1)
                self.tab1_Price_Action_Button.setGeometry(QtCore.QRect(560, 88, 161, 41))
                font = QtGui.QFont()
                font.setFamily("Lufthansa Roman")
                font.setPointSize(12)
                font.setBold(False)
                font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
                self.tab1_Price_Action_Button.setFont(font)
                self.tab1_Price_Action_Button.setObjectName("tab1_Price_Action_Button")
                self.buttonGroup1.addButton(self.tab1_Price_Action_Button)
                self.tab1_CSC_Input = QtWidgets.QTextEdit(parent=self.tab1)
                self.tab1_CSC_Input.setGeometry(QtCore.QRect(30, 250, 61, 31))
                font = QtGui.QFont()
                font.setPointSize(9)
                font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
                self.tab1_CSC_Input.setFont(font)
                self.tab1_CSC_Input.setAutoFillBackground(True)
                self.tab1_CSC_Input.setStyleSheet("background-color: transparent;\n"
        "border: none;")
                self.tab1_CSC_Input.setReadOnly(True)
                self.tab1_CSC_Input.setObjectName("tab1_CSC_Input")
                self.tab1_RFP_CheckBox = QtWidgets.QCheckBox(parent=self.tab1)
                self.tab1_RFP_CheckBox.setGeometry(QtCore.QRect(120, 88, 141, 41))
                font = QtGui.QFont()
                font.setFamily("Lufthansa Roman")
                font.setPointSize(12)
                font.setBold(False)
                font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
                self.tab1_RFP_CheckBox.setFont(font)
                self.tab1_RFP_CheckBox.setObjectName("tab1_RFP_CheckBox")
                
                #self.buttonGroup12 = QtWidgets.QButtonGroup(AutoFolder)
                #self.buttonGroup12.setObjectName("buttonGroup12")
                #self.buttonGroup12.addButton(self.tab1_RFP_CheckBox)
                font = QtGui.QFont()
                font.setFamily("Lufthansa Roman")
                font.setPointSize(12)
                font.setBold(False)
                font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferDefault)
                font = QtGui.QFont()
                font.setFamily("Lufthansa Roman")
                font.setPointSize(12)
                font.setBold(False)
                font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
                self.tab1_line_3 = QtWidgets.QFrame(parent=self.tab1)
                self.tab1_line_3.setGeometry(QtCore.QRect(30, 215, 831, 20))
                self.tab1_line_3.setLineWidth(1)
                self.tab1_line_3.setMidLineWidth(0)
                self.tab1_line_3.setFrameShape(QtWidgets.QFrame.Shape.HLine)
                self.tab1_line_3.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
                self.tab1_line_3.setObjectName("tab1_line_3")
                self.tab1_textEdit_4 = QtWidgets.QTextEdit(parent=self.tab1)
                self.tab1_textEdit_4.setGeometry(QtCore.QRect(285, 250, 41, 31))
                self.tab1_textEdit_4.setAutoFillBackground(True)
                self.tab1_textEdit_4.setStyleSheet("background-color: transparent;\n"
        "border: none;\n"
        "")
                self.tab1_textEdit_4.setReadOnly(True)
                self.tab1_textEdit_4.setObjectName("tab1_textEdit_4")
                self.tab1_TemplatesCheckBox = QtWidgets.QCheckBox(parent=self.tab1)
                self.tab1_TemplatesCheckBox.setGeometry(QtCore.QRect(36, 390, 301, 31))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
                self.tab1_TemplatesCheckBox.setFont(font)
                self.tab1_TemplatesCheckBox.setAutoFillBackground(False)
                self.tab1_TemplatesCheckBox.setStyleSheet("background-color: transparent;\n"
        "")
                self.tab1_TemplatesCheckBox.setChecked(True)
                self.tab1_TemplatesCheckBox.setObjectName("tab1_TemplatesCheckBox")
                self.tab1_line_4 = QtWidgets.QFrame(parent=self.tab1)
                self.tab1_line_4.setGeometry(QtCore.QRect(30, 290, 831, 20))
                self.tab1_line_4.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
                self.tab1_line_4.setLineWidth(1)
                self.tab1_line_4.setMidLineWidth(0)
                self.tab1_line_4.setFrameShape(QtWidgets.QFrame.Shape.HLine)
                self.tab1_line_4.setObjectName("tab1_line_4")
                self.tab1_RFP_Precheck_CheckBox = QtWidgets.QCheckBox(parent=self.tab1)
                self.tab1_RFP_Precheck_CheckBox.setGeometry(QtCore.QRect(120, 130, 141, 41))
                font = QtGui.QFont()
                font.setFamily("Lufthansa Roman")
                font.setPointSize(12)
                font.setBold(False)
                font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
                self.tab1_RFP_Precheck_CheckBox.setFont(font)
                self.tab1_RFP_Precheck_CheckBox.setObjectName("tab1_RFP_Precheck_CheckBox")
                #self.buttonGroup12.addButton(self.tab1_RFP_Precheck_CheckBox)
                self.tab1_dateEdit = QtWidgets.QDateEdit(parent=self.tab1)
                self.tab1_dateEdit.setGeometry(QtCore.QRect(120, 320, 150, 31))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(False)
                font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
                self.tab1_dateEdit.setFont(font)
                self.tab1_dateEdit.setAutoFillBackground(False)
                self.tab1_dateEdit.setProperty("showGroupSeparator", False)
                self.tab1_dateEdit.setMaximumDateTime(QtCore.QDateTime(QtCore.QDate(3000, 1, 1), QtCore.QTime(17, 59, 59)))
                self.tab1_dateEdit.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(2020, 1, 1), QtCore.QTime(0, 0, 0)))
                self.tab1_dateEdit.setCalendarPopup(True)
                self.tab1_dateEdit.setTimeSpec(QtCore.Qt.TimeSpec.LocalTime)
                self.tab1_dateEdit.setObjectName("tab1_dateEdit")
                self.tab1_AL_Input_Box = QtWidgets.QLineEdit(parent=self.tab1)
                self.tab1_AL_Input_Box.setEnabled(True)
                self.tab1_AL_Input_Box.setGeometry(QtCore.QRect(120, 28, 161, 31))
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.tab1_AL_Input_Box.sizePolicy().hasHeightForWidth())
                self.tab1_AL_Input_Box.setSizePolicy(sizePolicy)
                font = QtGui.QFont()
                font.setFamily("San Francisco")
                font.setPointSize(11)
                self.tab1_AL_Input_Box.setFont(font)
                self.tab1_AL_Input_Box.setStatusTip("")
                self.tab1_AL_Input_Box.setStyleSheet("font-family: \"San Francisco\", Arial, sans-serif;")
                self.tab1_AL_Input_Box.setText("")
                self.tab1_AL_Input_Box.setMaxLength(10)
                self.tab1_AL_Input_Box.setObjectName("tab1_AL_Input_Box")
                self.tab1_Project_Select = QtWidgets.QTextEdit(parent=self.tab1)
                self.tab1_Project_Select.setGeometry(QtCore.QRect(30, 135, 81, 37))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setItalic(False)
                font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
                self.tab1_Project_Select.setFont(font)
                self.tab1_Project_Select.setAutoFillBackground(True)
                self.tab1_Project_Select.setStyleSheet("background-color: transparent;\n"
        "border: none;")
                self.tab1_Project_Select.setReadOnly(True)
                self.tab1_Project_Select.setObjectName("tab1_Project_Select")
                self.tab1_AL_Input_Text = QtWidgets.QTextEdit(parent=self.tab1)
                self.tab1_AL_Input_Text.setGeometry(QtCore.QRect(30, 31, 71, 31))
                font = QtGui.QFont()
                font.setPointSize(9)
                font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
                self.tab1_AL_Input_Text.setFont(font)
                self.tab1_AL_Input_Text.setAutoFillBackground(True)
                self.tab1_AL_Input_Text.setStyleSheet("background-color: transparent;\n"
        "border: none;\n"
        "")
                self.tab1_AL_Input_Text.setReadOnly(True)
                self.tab1_AL_Input_Text.setObjectName("tab1_AL_Input_Text")
                self.tab1_Date_Input = QtWidgets.QTextEdit(parent=self.tab1)
                self.tab1_Date_Input.setGeometry(QtCore.QRect(30, 322, 61, 31))
                self.tab1_Date_Input.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
                self.tab1_Date_Input.setAutoFillBackground(True)
                self.tab1_Date_Input.setStyleSheet("background-color: transparent;\n"
        "border: none;")
                self.tab1_Date_Input.setReadOnly(True)
                self.tab1_Date_Input.setObjectName("tab1_Date_Input")
                self.tab1_Cyc_Button = QtWidgets.QRadioButton(parent=self.tab1)
                self.tab1_Cyc_Button.setGeometry(QtCore.QRect(350, 172, 161, 41))
                font = QtGui.QFont()
                font.setFamily("Lufthansa Roman")
                font.setPointSize(12)
                font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
                self.tab1_Cyc_Button.setFont(font)
                self.tab1_Cyc_Button.setObjectName("tab1_Cyc_Button")
                self.buttonGroup1.addButton(self.tab1_Cyc_Button)
                self.tab1_comboBox_2nd = QtWidgets.QComboBox(parent=self.tab1)
                self.tab1_comboBox_2nd.setGeometry(QtCore.QRect(325, 247, 151, 31))
                font = QtGui.QFont()
                font.setPointSize(11)
                font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
                self.tab1_comboBox_2nd.setFont(font)
                self.tab1_comboBox_2nd.setStyleSheet("")
                self.tab1_comboBox_2nd.setEnabled(False)
                self.tab1_comboBox_2nd.setEditable(True)
                self.tab1_comboBox_2nd.setCurrentText("")
                self.tab1_comboBox_2nd.setPlaceholderText("")
                self.tab1_comboBox_2nd.setObjectName("tab1_comboBox_2nd")
                self.tab1_comboBox_2nd.addItem("")
                self.tab1_comboBox_2nd.setItemText(0, "")
                self.tab1_comboBox_2nd.addItem("")
                self.tab1_comboBox_2nd.addItem("")
                self.tab1_comboBox_2nd.addItem("")
                self.tab1_comboBox_2nd.addItem("")
                self.tab1_comboBox_2nd.addItem("")
                self.tab1_comboBox_2nd.addItem("")
                self.tab1_comboBox_2nd.addItem("")
                self.tab1_comboBox_2nd.addItem("")
                self.tab1_comboBox_2nd.addItem("")
                self.tab1_comboBox_2nd.addItem("")
                self.tab1_comboBox_2nd.addItem("")
                self.tab1_comboBox_2nd.addItem("")
                self.tab1_comboBox_2nd.addItem("")
                self.tab1_comboBox_2nd.addItem("")
                self.tab1_comboBox_2nd.addItem("")
                self.tab1_comboBox_2nd.addItem("")
                self.tab1_comboBox_2nd.addItem("")
                self.tab1_comboBox_2nd.addItem("")
                self.tab1_comboBox_2nd.addItem("")
                self.tab1_comboBox_2nd.addItem("")
                self.tab1_comboBox_2nd.addItem("")
                self.tab1_comboBox_2nd.addItem("")
                self.tab1_comboBox_2nd.addItem("")
                self.tab1_comboBox_2nd.addItem("")
                self.tab1_comboBox_2nd.addItem("")
                self.tab1_comboBox_2nd.addItem("")
                self.tab1_comboBox_2nd.addItem("")
                self.tab1_comboBox_2nd.addItem("")
                self.tab1_comboBox_2nd.addItem("")
                self.tab1_comboBox_2nd.addItem("")
                self.tab1_comboBox_2nd.addItem("")
                self.tab1_comboBox_2nd.addItem("")
                self.tab1_comboBox_2nd.addItem("")
                self.tab1_comboBox_2nd.addItem("")
                self.tab1_comboBox_2nd.addItem("")
                self.tab1_comboBox_2nd.addItem("")
                self.tab1_comboBox_2nd.addItem("")
                self.tab1_comboBox_2nd.addItem("")
                self.tab1_comboBox_2nd.addItem("")
                self.tab1_comboBox_2nd.addItem("")
                self.tab1_comboBox_2nd.addItem("")
                self.tab1_comboBox_2nd.addItem("")
                self.tab1_comboBox_2nd.addItem("")
                self.tab1_comboBox_2nd.addItem("")
                self.tab1_comboBox_1st = QtWidgets.QComboBox(parent=self.tab1)
                self.tab1_comboBox_1st.setGeometry(QtCore.QRect(120, 247, 151, 31))
                font = QtGui.QFont()
                font.setPointSize(11)
                font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
                self.tab1_comboBox_1st.setFont(font)
                self.tab1_comboBox_1st.setStyleSheet("")
                self.tab1_comboBox_1st.setEditable(True)
                self.tab1_comboBox_1st.setFrame(True)
                self.tab1_comboBox_1st.setObjectName("tab1_comboBox_1st")
                self.tab1_comboBox_1st.addItem("")
                self.tab1_comboBox_1st.setItemText(0, "")
                self.tab1_comboBox_1st.addItem("")
                self.tab1_comboBox_1st.addItem("")
                self.tab1_comboBox_1st.addItem("")
                self.tab1_comboBox_1st.addItem("")
                self.tab1_comboBox_1st.addItem("")
                self.tab1_comboBox_1st.addItem("")
                self.tab1_comboBox_1st.addItem("")
                self.tab1_comboBox_1st.addItem("")
                self.tab1_comboBox_1st.addItem("")
                self.tab1_comboBox_1st.addItem("")
                self.tab1_comboBox_1st.addItem("")
                self.tab1_comboBox_1st.addItem("")
                self.tab1_comboBox_1st.addItem("")
                self.tab1_comboBox_1st.addItem("")
                self.tab1_comboBox_1st.addItem("")
                self.tab1_comboBox_1st.addItem("")
                self.tab1_comboBox_1st.addItem("")
                self.tab1_comboBox_1st.addItem("")
                self.tab1_comboBox_1st.addItem("")
                self.tab1_comboBox_1st.addItem("")
                self.tab1_comboBox_1st.addItem("")
                self.tab1_comboBox_1st.addItem("")
                self.tab1_comboBox_1st.addItem("")
                self.tab1_comboBox_1st.addItem("")
                self.tab1_comboBox_1st.addItem("")
                self.tab1_comboBox_1st.addItem("")
                self.tab1_comboBox_1st.addItem("")
                self.tab1_comboBox_1st.addItem("")
                self.tab1_comboBox_1st.addItem("")
                self.tab1_comboBox_1st.addItem("")
                self.tab1_comboBox_1st.addItem("")
                self.tab1_comboBox_1st.addItem("")
                self.tab1_comboBox_1st.addItem("")
                self.tab1_comboBox_1st.addItem("")
                self.tab1_comboBox_1st.addItem("")
                self.tab1_comboBox_1st.addItem("")
                self.tab1_comboBox_1st.addItem("")
                self.tab1_comboBox_1st.addItem("")
                self.tab1_comboBox_1st.addItem("")
                self.tab1_comboBox_1st.addItem("")
                self.tab1_comboBox_1st.addItem("")
                self.tab1_comboBox_1st.addItem("")
                self.tab1_comboBox_1st.addItem("")
                self.tab1_comboBox_1st.addItem("")
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
                self.tabWidget.addTab(self.tab1, "")
                self.tab_2 = QtWidgets.QWidget()
                self.tab_2.setEnabled(False)
                self.tab_2.setAutoFillBackground(True)
                self.tab_2.setObjectName("tab_2")
                self.tab2_line_1 = QtWidgets.QFrame(parent=self.tab_2)
                self.tab2_line_1.setGeometry(QtCore.QRect(0, -8, 895, 21))
                self.tab2_line_1.setStyleSheet("QFrame#verticalSeparator {\n"
        "    border: 1px dotted #007bff; /* Border style */\n"
        "    height: 50px; /* Set the height for vertical separator */\n"
        "}\n"
        "")
                self.tab2_line_1.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
                self.tab2_line_1.setLineWidth(5)
                self.tab2_line_1.setFrameShape(QtWidgets.QFrame.Shape.HLine)
                self.tab2_line_1.setObjectName("tab2_line_1")
                self.tab2_textEdit_7 = QtWidgets.QTextEdit(parent=self.tab_2)
                self.tab2_textEdit_7.setEnabled(False)
                self.tab2_textEdit_7.setGeometry(QtCore.QRect(290, 30, 181, 31))
                self.tab2_textEdit_7.setAutoFillBackground(True)
                self.tab2_textEdit_7.setStyleSheet("background-color: transparent;\n"
        "border: none;\n"
        "")
                self.tab2_textEdit_7.setReadOnly(True)
                self.tab2_textEdit_7.setObjectName("tab2_textEdit_7")
                self.tab2_AL_Input_Box = QtWidgets.QLineEdit(parent=self.tab_2)
                self.tab2_AL_Input_Box.setGeometry(QtCore.QRect(120, 28, 161, 31))
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.tab2_AL_Input_Box.sizePolicy().hasHeightForWidth())
                self.tab2_AL_Input_Box.setSizePolicy(sizePolicy)
                font = QtGui.QFont()
                font.setFamily("San Francisco")
                font.setPointSize(11)
                self.tab2_AL_Input_Box.setFont(font)
                self.tab2_AL_Input_Box.setStatusTip("")
                self.tab2_AL_Input_Box.setStyleSheet("font-family: \"San Francisco\", Arial, sans-serif;")
                self.tab2_AL_Input_Box.setText("")
                self.tab2_AL_Input_Box.setMaxLength(10)
                self.tab2_AL_Input_Box.setObjectName("tab2_AL_Input_Box")
                self.tab2_AL_Input_Text = QtWidgets.QTextEdit(parent=self.tab_2)
                self.tab2_AL_Input_Text.setGeometry(QtCore.QRect(30, 31, 71, 31))
                font = QtGui.QFont()
                font.setPointSize(9)
                font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
                self.tab2_AL_Input_Text.setFont(font)
                self.tab2_AL_Input_Text.setAutoFillBackground(True)
                self.tab2_AL_Input_Text.setStyleSheet("background-color: transparent;\n"
        "border: none;\n"
        "")
                self.tab2_AL_Input_Text.setReadOnly(True)
                self.tab2_AL_Input_Text.setObjectName("tab2_AL_Input_Text")
                self.tab2_FolderNumber = QtWidgets.QTextEdit(parent=self.tab_2)
                self.tab2_FolderNumber.setGeometry(QtCore.QRect(520, 30, 151, 31))
                font = QtGui.QFont()
                font.setPointSize(9)
                font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
                self.tab2_FolderNumber.setFont(font)
                self.tab2_FolderNumber.setAutoFillBackground(True)
                self.tab2_FolderNumber.setStyleSheet("background-color: transparent;\n"
        "border: none;\n"
        "")
                self.tab2_FolderNumber.setReadOnly(True)
                self.tab2_FolderNumber.setObjectName("tab2_FolderNumber")
                self.tab2_FolderNumberBox = QtWidgets.QLineEdit(parent=self.tab_2)
                self.tab2_FolderNumberBox.setGeometry(QtCore.QRect(660, 28, 111, 31))
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.tab2_FolderNumberBox.sizePolicy().hasHeightForWidth())
                self.tab2_FolderNumberBox.setSizePolicy(sizePolicy)
                font = QtGui.QFont()
                font.setFamily("San Francisco")
                font.setPointSize(11)
                self.tab2_FolderNumberBox.setFont(font)
                self.tab2_FolderNumberBox.setStatusTip("")
                self.tab2_FolderNumberBox.setStyleSheet("font-family: \"San Francisco\", Arial, sans-serif;")
                self.tab2_FolderNumberBox.setText("")
                self.tab2_FolderNumberBox.setMaxLength(10)
                self.tab2_FolderNumberBox.setObjectName("tab2_FolderNumberBox")
                self.tab2_line_2 = QtWidgets.QFrame(parent=self.tab_2)
                self.tab2_line_2.setGeometry(QtCore.QRect(30, 70, 831, 21))
                self.tab2_line_2.setLineWidth(1)
                self.tab2_line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
                self.tab2_line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
                self.tab2_line_2.setObjectName("tab2_line_2")
                self.tab2_CSC_Input = QtWidgets.QTextEdit(parent=self.tab_2)
                self.tab2_CSC_Input.setGeometry(QtCore.QRect(30, 210, 61, 31))
                font = QtGui.QFont()
                font.setPointSize(9)
                font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
                self.tab2_CSC_Input.setFont(font)
                self.tab2_CSC_Input.setAutoFillBackground(True)
                self.tab2_CSC_Input.setStyleSheet("background-color: transparent;\n"
        "border: none;")
                self.tab2_CSC_Input.setReadOnly(True)
                self.tab2_CSC_Input.setObjectName("tab2_CSC_Input")
                self.tab2_comboBox_1st = QtWidgets.QComboBox(parent=self.tab_2)
                self.tab2_comboBox_1st.setGeometry(QtCore.QRect(120, 180, 151, 31))
                font = QtGui.QFont()
                font.setPointSize(11)
                font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
                self.tab2_comboBox_1st.setFont(font)
                self.tab2_comboBox_1st.setStyleSheet("")
                self.tab2_comboBox_1st.setEditable(True)
                self.tab2_comboBox_1st.setPlaceholderText("")
                self.tab2_comboBox_1st.setFrame(True)
                self.tab2_comboBox_1st.setObjectName("tab2_comboBox_1st")
                self.tab2_comboBox_1st.addItem("")
                self.tab2_comboBox_1st.setItemText(0, "")
                self.tab2_comboBox_1st.addItem("")
                self.tab2_comboBox_1st.addItem("")
                self.tab2_comboBox_1st.addItem("")
                self.tab2_comboBox_1st.addItem("")
                self.tab2_comboBox_1st.addItem("")
                self.tab2_comboBox_1st.addItem("")
                self.tab2_comboBox_1st.addItem("")
                self.tab2_comboBox_1st.addItem("")
                self.tab2_comboBox_1st.addItem("")
                self.tab2_comboBox_1st.addItem("")
                self.tab2_comboBox_1st.addItem("")
                self.tab2_comboBox_1st.addItem("")
                self.tab2_comboBox_1st.addItem("")
                self.tab2_comboBox_1st.addItem("")
                self.tab2_comboBox_1st.addItem("")
                self.tab2_comboBox_1st.addItem("")
                self.tab2_comboBox_1st.addItem("")
                self.tab2_comboBox_1st.addItem("")
                self.tab2_comboBox_1st.addItem("")
                self.tab2_comboBox_1st.addItem("")
                self.tab2_comboBox_1st.addItem("")
                self.tab2_comboBox_1st.addItem("")
                self.tab2_comboBox_1st.addItem("")
                self.tab2_comboBox_1st.addItem("")
                self.tab2_comboBox_1st.addItem("")
                self.tab2_comboBox_1st.addItem("")
                self.tab2_comboBox_1st.addItem("")
                self.tab2_comboBox_1st.addItem("")
                self.tab2_comboBox_1st.addItem("")
                self.tab2_comboBox_1st.addItem("")
                self.tab2_comboBox_1st.addItem("")
                self.tab2_comboBox_1st.addItem("")
                self.tab2_comboBox_1st.addItem("")
                self.tab2_comboBox_1st.addItem("")
                self.tab2_comboBox_1st.addItem("")
                self.tab2_comboBox_1st.addItem("")
                self.tab2_comboBox_1st.addItem("")
                self.tab2_comboBox_1st.addItem("")
                self.tab2_comboBox_1st.addItem("")
                self.tab2_comboBox_1st.addItem("")
                self.tab2_comboBox_1st.addItem("")
                self.tab2_comboBox_1st.addItem("")
                self.tab2_comboBox_1st.addItem("")
                self.tab2_comboBox_1st.addItem("")
                self.tab2_comboBox_2nd = QtWidgets.QComboBox(parent=self.tab_2)
                self.tab2_comboBox_2nd.setGeometry(QtCore.QRect(370, 180, 151, 31))
                font = QtGui.QFont()
                font.setPointSize(11)
                font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
                self.tab2_comboBox_2nd.setFont(font)
                self.tab2_comboBox_2nd.setStyleSheet("")
                self.tab2_comboBox_2nd.setEditable(True)
                self.tab2_comboBox_2nd.setPlaceholderText("")
                self.tab2_comboBox_2nd.setFrame(True)
                self.tab2_comboBox_2nd.setObjectName("tab2_comboBox_2nd")
                self.tab2_comboBox_2nd.addItem("")
                self.tab2_comboBox_2nd.setItemText(0, "")
                self.tab2_comboBox_2nd.addItem("")
                self.tab2_comboBox_2nd.addItem("")
                self.tab2_comboBox_2nd.addItem("")
                self.tab2_comboBox_2nd.addItem("")
                self.tab2_comboBox_2nd.addItem("")
                self.tab2_comboBox_2nd.addItem("")
                self.tab2_comboBox_2nd.addItem("")
                self.tab2_comboBox_2nd.addItem("")
                self.tab2_comboBox_2nd.addItem("")
                self.tab2_comboBox_2nd.addItem("")
                self.tab2_comboBox_2nd.addItem("")
                self.tab2_comboBox_2nd.addItem("")
                self.tab2_comboBox_2nd.addItem("")
                self.tab2_comboBox_2nd.addItem("")
                self.tab2_comboBox_2nd.addItem("")
                self.tab2_comboBox_2nd.addItem("")
                self.tab2_comboBox_2nd.addItem("")
                self.tab2_comboBox_2nd.addItem("")
                self.tab2_comboBox_2nd.addItem("")
                self.tab2_comboBox_2nd.addItem("")
                self.tab2_comboBox_2nd.addItem("")
                self.tab2_comboBox_2nd.addItem("")
                self.tab2_comboBox_2nd.addItem("")
                self.tab2_comboBox_2nd.addItem("")
                self.tab2_comboBox_2nd.addItem("")
                self.tab2_comboBox_2nd.addItem("")
                self.tab2_comboBox_2nd.addItem("")
                self.tab2_comboBox_2nd.addItem("")
                self.tab2_comboBox_2nd.addItem("")
                self.tab2_comboBox_2nd.addItem("")
                self.tab2_comboBox_2nd.addItem("")
                self.tab2_comboBox_2nd.addItem("")
                self.tab2_comboBox_2nd.addItem("")
                self.tab2_comboBox_2nd.addItem("")
                self.tab2_comboBox_2nd.addItem("")
                self.tab2_comboBox_2nd.addItem("")
                self.tab2_comboBox_2nd.addItem("")
                self.tab2_comboBox_2nd.addItem("")
                self.tab2_comboBox_2nd.addItem("")
                self.tab2_comboBox_2nd.addItem("")
                self.tab2_comboBox_2nd.addItem("")
                self.tab2_comboBox_2nd.addItem("")
                self.tab2_comboBox_2nd.addItem("")
                self.tab2_comboBox_2nd.addItem("")
                self.tab2_comboBox_3rd = QtWidgets.QComboBox(parent=self.tab_2)
                self.tab2_comboBox_3rd.setGeometry(QtCore.QRect(620, 180, 151, 31))
                font = QtGui.QFont()
                font.setPointSize(11)
                font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
                self.tab2_comboBox_3rd.setFont(font)
                self.tab2_comboBox_3rd.setStyleSheet("")
                self.tab2_comboBox_3rd.setEditable(True)
                self.tab2_comboBox_3rd.setPlaceholderText("")
                self.tab2_comboBox_3rd.setFrame(True)
                self.tab2_comboBox_3rd.setObjectName("tab2_comboBox_3rd")
                self.tab2_comboBox_3rd.addItem("")
                self.tab2_comboBox_3rd.setItemText(0, "")
                self.tab2_comboBox_3rd.addItem("")
                self.tab2_comboBox_3rd.addItem("")
                self.tab2_comboBox_3rd.addItem("")
                self.tab2_comboBox_3rd.addItem("")
                self.tab2_comboBox_3rd.addItem("")
                self.tab2_comboBox_3rd.addItem("")
                self.tab2_comboBox_3rd.addItem("")
                self.tab2_comboBox_3rd.addItem("")
                self.tab2_comboBox_3rd.addItem("")
                self.tab2_comboBox_3rd.addItem("")
                self.tab2_comboBox_3rd.addItem("")
                self.tab2_comboBox_3rd.addItem("")
                self.tab2_comboBox_3rd.addItem("")
                self.tab2_comboBox_3rd.addItem("")
                self.tab2_comboBox_3rd.addItem("")
                self.tab2_comboBox_3rd.addItem("")
                self.tab2_comboBox_3rd.addItem("")
                self.tab2_comboBox_3rd.addItem("")
                self.tab2_comboBox_3rd.addItem("")
                self.tab2_comboBox_3rd.addItem("")
                self.tab2_comboBox_3rd.addItem("")
                self.tab2_comboBox_3rd.addItem("")
                self.tab2_comboBox_3rd.addItem("")
                self.tab2_comboBox_3rd.addItem("")
                self.tab2_comboBox_3rd.addItem("")
                self.tab2_comboBox_3rd.addItem("")
                self.tab2_comboBox_3rd.addItem("")
                self.tab2_comboBox_3rd.addItem("")
                self.tab2_comboBox_3rd.addItem("")
                self.tab2_comboBox_3rd.addItem("")
                self.tab2_comboBox_3rd.addItem("")
                self.tab2_comboBox_3rd.addItem("")
                self.tab2_comboBox_3rd.addItem("")
                self.tab2_comboBox_3rd.addItem("")
                self.tab2_comboBox_3rd.addItem("")
                self.tab2_comboBox_3rd.addItem("")
                self.tab2_comboBox_3rd.addItem("")
                self.tab2_comboBox_3rd.addItem("")
                self.tab2_comboBox_3rd.addItem("")
                self.tab2_comboBox_3rd.addItem("")
                self.tab2_comboBox_3rd.addItem("")
                self.tab2_comboBox_3rd.addItem("")
                self.tab2_comboBox_3rd.addItem("")
                self.tab2_comboBox_3rd.addItem("")
                self.tab2_comboBox_4th = QtWidgets.QComboBox(parent=self.tab_2)
                self.tab2_comboBox_4th.setGeometry(QtCore.QRect(120, 240, 151, 31))
                font = QtGui.QFont()
                font.setPointSize(11)
                font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
                self.tab2_comboBox_4th.setFont(font)
                self.tab2_comboBox_4th.setStyleSheet("")
                self.tab2_comboBox_4th.setEditable(True)
                self.tab2_comboBox_4th.setPlaceholderText("")
                self.tab2_comboBox_4th.setFrame(True)
                self.tab2_comboBox_4th.setObjectName("tab2_comboBox_4th")
                self.tab2_comboBox_4th.addItem("")
                self.tab2_comboBox_4th.setItemText(0, "")
                self.tab2_comboBox_4th.addItem("")
                self.tab2_comboBox_4th.addItem("")
                self.tab2_comboBox_4th.addItem("")
                self.tab2_comboBox_4th.addItem("")
                self.tab2_comboBox_4th.addItem("")
                self.tab2_comboBox_4th.addItem("")
                self.tab2_comboBox_4th.addItem("")
                self.tab2_comboBox_4th.addItem("")
                self.tab2_comboBox_4th.addItem("")
                self.tab2_comboBox_4th.addItem("")
                self.tab2_comboBox_4th.addItem("")
                self.tab2_comboBox_4th.addItem("")
                self.tab2_comboBox_4th.addItem("")
                self.tab2_comboBox_4th.addItem("")
                self.tab2_comboBox_4th.addItem("")
                self.tab2_comboBox_4th.addItem("")
                self.tab2_comboBox_4th.addItem("")
                self.tab2_comboBox_4th.addItem("")
                self.tab2_comboBox_4th.addItem("")
                self.tab2_comboBox_4th.addItem("")
                self.tab2_comboBox_4th.addItem("")
                self.tab2_comboBox_4th.addItem("")
                self.tab2_comboBox_4th.addItem("")
                self.tab2_comboBox_4th.addItem("")
                self.tab2_comboBox_4th.addItem("")
                self.tab2_comboBox_4th.addItem("")
                self.tab2_comboBox_4th.addItem("")
                self.tab2_comboBox_4th.addItem("")
                self.tab2_comboBox_4th.addItem("")
                self.tab2_comboBox_4th.addItem("")
                self.tab2_comboBox_4th.addItem("")
                self.tab2_comboBox_4th.addItem("")
                self.tab2_comboBox_4th.addItem("")
                self.tab2_comboBox_4th.addItem("")
                self.tab2_comboBox_4th.addItem("")
                self.tab2_comboBox_4th.addItem("")
                self.tab2_comboBox_4th.addItem("")
                self.tab2_comboBox_4th.addItem("")
                self.tab2_comboBox_4th.addItem("")
                self.tab2_comboBox_4th.addItem("")
                self.tab2_comboBox_4th.addItem("")
                self.tab2_comboBox_4th.addItem("")
                self.tab2_comboBox_4th.addItem("")
                self.tab2_comboBox_4th.addItem("")
                self.tab2_comboBox_5th = QtWidgets.QComboBox(parent=self.tab_2)
                self.tab2_comboBox_5th.setGeometry(QtCore.QRect(370, 240, 151, 31))
                font = QtGui.QFont()
                font.setPointSize(11)
                font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
                self.tab2_comboBox_5th.setFont(font)
                self.tab2_comboBox_5th.setStyleSheet("")
                self.tab2_comboBox_5th.setEditable(True)
                self.tab2_comboBox_5th.setPlaceholderText("")
                self.tab2_comboBox_5th.setFrame(True)
                self.tab2_comboBox_5th.setObjectName("tab2_comboBox_5th")
                self.tab2_comboBox_5th.addItem("")
                self.tab2_comboBox_5th.setItemText(0, "")
                self.tab2_comboBox_5th.addItem("")
                self.tab2_comboBox_5th.addItem("")
                self.tab2_comboBox_5th.addItem("")
                self.tab2_comboBox_5th.addItem("")
                self.tab2_comboBox_5th.addItem("")
                self.tab2_comboBox_5th.addItem("")
                self.tab2_comboBox_5th.addItem("")
                self.tab2_comboBox_5th.addItem("")
                self.tab2_comboBox_5th.addItem("")
                self.tab2_comboBox_5th.addItem("")
                self.tab2_comboBox_5th.addItem("")
                self.tab2_comboBox_5th.addItem("")
                self.tab2_comboBox_5th.addItem("")
                self.tab2_comboBox_5th.addItem("")
                self.tab2_comboBox_5th.addItem("")
                self.tab2_comboBox_5th.addItem("")
                self.tab2_comboBox_5th.addItem("")
                self.tab2_comboBox_5th.addItem("")
                self.tab2_comboBox_5th.addItem("")
                self.tab2_comboBox_5th.addItem("")
                self.tab2_comboBox_5th.addItem("")
                self.tab2_comboBox_5th.addItem("")
                self.tab2_comboBox_5th.addItem("")
                self.tab2_comboBox_5th.addItem("")
                self.tab2_comboBox_5th.addItem("")
                self.tab2_comboBox_5th.addItem("")
                self.tab2_comboBox_5th.addItem("")
                self.tab2_comboBox_5th.addItem("")
                self.tab2_comboBox_5th.addItem("")
                self.tab2_comboBox_5th.addItem("")
                self.tab2_comboBox_5th.addItem("")
                self.tab2_comboBox_5th.addItem("")
                self.tab2_comboBox_5th.addItem("")
                self.tab2_comboBox_5th.addItem("")
                self.tab2_comboBox_5th.addItem("")
                self.tab2_comboBox_5th.addItem("")
                self.tab2_comboBox_5th.addItem("")
                self.tab2_comboBox_5th.addItem("")
                self.tab2_comboBox_5th.addItem("")
                self.tab2_comboBox_5th.addItem("")
                self.tab2_comboBox_5th.addItem("")
                self.tab2_comboBox_5th.addItem("")
                self.tab2_comboBox_5th.addItem("")
                self.tab2_comboBox_5th.addItem("")
                self.tab2_comboBox_6th = QtWidgets.QComboBox(parent=self.tab_2)
                self.tab2_comboBox_6th.setGeometry(QtCore.QRect(620, 240, 151, 31))
                font = QtGui.QFont()
                font.setPointSize(11)
                font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
                self.tab2_comboBox_6th.setFont(font)
                self.tab2_comboBox_6th.setStyleSheet("")
                self.tab2_comboBox_6th.setEditable(True)
                self.tab2_comboBox_6th.setPlaceholderText("")
                self.tab2_comboBox_6th.setFrame(True)
                self.tab2_comboBox_6th.setObjectName("tab2_comboBox_6th")
                self.tab2_comboBox_6th.addItem("")
                self.tab2_comboBox_6th.setItemText(0, "")
                self.tab2_comboBox_6th.addItem("")
                self.tab2_comboBox_6th.addItem("")
                self.tab2_comboBox_6th.addItem("")
                self.tab2_comboBox_6th.addItem("")
                self.tab2_comboBox_6th.addItem("")
                self.tab2_comboBox_6th.addItem("")
                self.tab2_comboBox_6th.addItem("")
                self.tab2_comboBox_6th.addItem("")
                self.tab2_comboBox_6th.addItem("")
                self.tab2_comboBox_6th.addItem("")
                self.tab2_comboBox_6th.addItem("")
                self.tab2_comboBox_6th.addItem("")
                self.tab2_comboBox_6th.addItem("")
                self.tab2_comboBox_6th.addItem("")
                self.tab2_comboBox_6th.addItem("")
                self.tab2_comboBox_6th.addItem("")
                self.tab2_comboBox_6th.addItem("")
                self.tab2_comboBox_6th.addItem("")
                self.tab2_comboBox_6th.addItem("")
                self.tab2_comboBox_6th.addItem("")
                self.tab2_comboBox_6th.addItem("")
                self.tab2_comboBox_6th.addItem("")
                self.tab2_comboBox_6th.addItem("")
                self.tab2_comboBox_6th.addItem("")
                self.tab2_comboBox_6th.addItem("")
                self.tab2_comboBox_6th.addItem("")
                self.tab2_comboBox_6th.addItem("")
                self.tab2_comboBox_6th.addItem("")
                self.tab2_comboBox_6th.addItem("")
                self.tab2_comboBox_6th.addItem("")
                self.tab2_comboBox_6th.addItem("")
                self.tab2_comboBox_6th.addItem("")
                self.tab2_comboBox_6th.addItem("")
                self.tab2_comboBox_6th.addItem("")
                self.tab2_comboBox_6th.addItem("")
                self.tab2_comboBox_6th.addItem("")
                self.tab2_comboBox_6th.addItem("")
                self.tab2_comboBox_6th.addItem("")
                self.tab2_comboBox_6th.addItem("")
                self.tab2_comboBox_6th.addItem("")
                self.tab2_comboBox_6th.addItem("")
                self.tab2_comboBox_6th.addItem("")
                self.tab2_comboBox_6th.addItem("")
                self.tab2_comboBox_6th.addItem("")
                self.tab2_textEdit_3 = QtWidgets.QTextEdit(parent=self.tab_2)
                self.tab2_textEdit_3.setGeometry(QtCore.QRect(90, 185, 31, 31))
                self.tab2_textEdit_3.setAutoFillBackground(True)
                self.tab2_textEdit_3.setStyleSheet("background-color: transparent;\n"
        "border: none;\n"
        "")
                self.tab2_textEdit_3.setReadOnly(True)
                self.tab2_textEdit_3.setObjectName("tab2_textEdit_3")
                self.tab2_textEdit_4 = QtWidgets.QTextEdit(parent=self.tab_2)
                self.tab2_textEdit_4.setGeometry(QtCore.QRect(330, 185, 41, 31))
                self.tab2_textEdit_4.setAutoFillBackground(True)
                self.tab2_textEdit_4.setStyleSheet("background-color: transparent;\n"
        "border: none;\n"
        "")
                self.tab2_textEdit_4.setReadOnly(True)
                self.tab2_textEdit_4.setObjectName("tab2_textEdit_4")
                self.tab2_textEdit_5 = QtWidgets.QTextEdit(parent=self.tab_2)
                self.tab2_textEdit_5.setGeometry(QtCore.QRect(580, 185, 41, 31))
                self.tab2_textEdit_5.setAutoFillBackground(True)
                self.tab2_textEdit_5.setStyleSheet("background-color: transparent;\n"
        "border: none;\n"
        "")
                self.tab2_textEdit_5.setReadOnly(True)
                self.tab2_textEdit_5.setObjectName("tab2_textEdit_5")
                self.tab2_textEdit_6 = QtWidgets.QTextEdit(parent=self.tab_2)
                self.tab2_textEdit_6.setGeometry(QtCore.QRect(80, 245, 41, 31))
                self.tab2_textEdit_6.setAutoFillBackground(True)
                self.tab2_textEdit_6.setStyleSheet("background-color: transparent;\n"
        "border: none;\n"
        "")
                self.tab2_textEdit_6.setReadOnly(True)
                self.tab2_textEdit_6.setObjectName("tab2_textEdit_6")
                self.tab2_textEdit_8 = QtWidgets.QTextEdit(parent=self.tab_2)
                self.tab2_textEdit_8.setGeometry(QtCore.QRect(330, 245, 41, 31))
                self.tab2_textEdit_8.setAutoFillBackground(True)
                self.tab2_textEdit_8.setStyleSheet("background-color: transparent;\n"
        "border: none;\n"
        "")
                self.tab2_textEdit_8.setReadOnly(True)
                self.tab2_textEdit_8.setObjectName("tab2_textEdit_8")
                self.tab2_textEdit_9 = QtWidgets.QTextEdit(parent=self.tab_2)
                self.tab2_textEdit_9.setGeometry(QtCore.QRect(580, 245, 41, 31))
                self.tab2_textEdit_9.setAutoFillBackground(True)
                self.tab2_textEdit_9.setStyleSheet("background-color: transparent;\n"
        "border: none;\n"
        "")
                self.tab2_textEdit_9.setReadOnly(True)
                self.tab2_textEdit_9.setObjectName("tab2_textEdit_9")
                self.tab2_Date_Input = QtWidgets.QTextEdit(parent=self.tab_2)
                self.tab2_Date_Input.setGeometry(QtCore.QRect(30, 330, 61, 31))
                self.tab2_Date_Input.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
                self.tab2_Date_Input.setAutoFillBackground(True)
                self.tab2_Date_Input.setStyleSheet("background-color: transparent;\n"
        "border: none;")
                self.tab2_Date_Input.setReadOnly(True)
                self.tab2_Date_Input.setObjectName("tab2_Date_Input")
                self.tab2_dateEdit = QtWidgets.QDateEdit(parent=self.tab_2)
                self.tab2_dateEdit.setGeometry(QtCore.QRect(120, 325, 150, 31))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(False)
                font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
                self.tab2_dateEdit.setFont(font)
                self.tab2_dateEdit.setAutoFillBackground(False)
                self.tab2_dateEdit.setProperty("showGroupSeparator", False)
                self.tab2_dateEdit.setMaximumDateTime(QtCore.QDateTime(QtCore.QDate(3000, 1, 1), QtCore.QTime(17, 59, 59)))
                self.tab2_dateEdit.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(2020, 1, 1), QtCore.QTime(0, 0, 0)))
                self.tab2_dateEdit.setCalendarPopup(True)
                self.tab2_dateEdit.setTimeSpec(QtCore.Qt.TimeSpec.LocalTime)
                self.tab2_dateEdit.setObjectName("tab2_dateEdit")
                self.tab2_textEdit_10 = QtWidgets.QTextEdit(parent=self.tab_2)
                self.tab2_textEdit_10.setGeometry(QtCore.QRect(290, 328, 221, 31))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(False)
                font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
                self.tab2_textEdit_10.setFont(font)
                self.tab2_textEdit_10.setAutoFillBackground(True)
                self.tab2_textEdit_10.setStyleSheet("background-color: transparent;\n"
        "border: none;\n"
        "")
                self.tab2_textEdit_10.setReadOnly(True)
                self.tab2_textEdit_10.setObjectName("tab2_textEdit_10")
                self.tab2_MPL_CheckBox = QtWidgets.QCheckBox(parent=self.tab_2)
                self.tab2_MPL_CheckBox.setGeometry(QtCore.QRect(240, 94, 91, 41))
                font = QtGui.QFont()
                font.setFamily("Lufthansa Roman")
                font.setPointSize(13)
                font.setBold(False)
                font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferDefault)
                self.tab2_MPL_CheckBox.setFont(font)
                self.tab2_MPL_CheckBox.setAutoFillBackground(False)
                self.tab2_MPL_CheckBox.setStyleSheet("")
                self.tab2_MPL_CheckBox.setObjectName("tab2_MPL_CheckBox")
                self.buttonGroup2 = QtWidgets.QButtonGroup(AutoFolder)
                self.buttonGroup2.setObjectName("buttonGroup2")
                self.buttonGroup2.addButton(self.tab2_MPL_CheckBox)
                self.tab2_Output_CheckBox = QtWidgets.QCheckBox(parent=self.tab_2)
                self.tab2_Output_CheckBox.setGeometry(QtCore.QRect(350, 94, 131, 41))
                font = QtGui.QFont()
                font.setFamily("Lufthansa Roman")
                font.setPointSize(13)
                font.setBold(False)
                font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferDefault)
                self.tab2_Output_CheckBox.setFont(font)
                self.tab2_Output_CheckBox.setAutoFillBackground(False)
                self.tab2_Output_CheckBox.setStyleSheet("")
                self.tab2_Output_CheckBox.setObjectName("tab2_Output_CheckBox")
                self.buttonGroup2.addButton(self.tab2_Output_CheckBox)
                self.tab2_line_3 = QtWidgets.QFrame(parent=self.tab_2)
                self.tab2_line_3.setGeometry(QtCore.QRect(30, 140, 831, 21))
                self.tab2_line_3.setLineWidth(1)
                self.tab2_line_3.setFrameShape(QtWidgets.QFrame.Shape.HLine)
                self.tab2_line_3.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
                self.tab2_line_3.setObjectName("tab2_line_3")
                self.tab2_FileType = QtWidgets.QTextEdit(parent=self.tab_2)
                self.tab2_FileType.setGeometry(QtCore.QRect(30, 100, 191, 31))
                font = QtGui.QFont()
                font.setPointSize(9)
                font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
                self.tab2_FileType.setFont(font)
                self.tab2_FileType.setAutoFillBackground(True)
                self.tab2_FileType.setStyleSheet("background-color: transparent;\n"
        "border: none;\n"
        "")
                self.tab2_FileType.setReadOnly(True)
                self.tab2_FileType.setObjectName("tab2_FileType")
                self.tab2_AcService_CheckBox = QtWidgets.QCheckBox(parent=self.tab_2)
                self.tab2_AcService_CheckBox.setGeometry(QtCore.QRect(510, 94, 131, 41))
                font = QtGui.QFont()
                font.setFamily("Lufthansa Roman")
                font.setPointSize(13)
                font.setBold(False)
                font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferDefault)
                self.tab2_AcService_CheckBox.setFont(font)
                self.tab2_AcService_CheckBox.setAutoFillBackground(False)
                self.tab2_AcService_CheckBox.setStyleSheet("")
                self.tab2_AcService_CheckBox.setObjectName("tab2_AcService_CheckBox")
                self.buttonGroup2.addButton(self.tab2_AcService_CheckBox)
                self.tab2_line_4 = QtWidgets.QFrame(parent=self.tab_2)
                self.tab2_line_4.setGeometry(QtCore.QRect(30, 290, 831, 21))
                self.tab2_line_4.setLineWidth(1)
                self.tab2_line_4.setFrameShape(QtWidgets.QFrame.Shape.HLine)
                self.tab2_line_4.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
                self.tab2_line_4.setObjectName("tab2_line_4")
                self.tab2_buttonBox_2 = QtWidgets.QDialogButtonBox(parent=self.tab_2)
                self.tab2_buttonBox_2.setGeometry(QtCore.QRect(710, 460, 151, 31))
                self.tab2_buttonBox_2.setMaximumSize(QtCore.QSize(171, 16777215))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
                self.tab2_buttonBox_2.setFont(font)
                self.tab2_buttonBox_2.setOrientation(QtCore.Qt.Orientation.Horizontal)
                self.tab2_buttonBox_2.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Ok)
                self.tab2_buttonBox_2.setObjectName("tab2_buttonBox_2")
                self.tab2_textEdit_11 = QtWidgets.QTextEdit(parent=self.tab_2)
                self.tab2_textEdit_11.setGeometry(QtCore.QRect(30, 395, 801, 31))
                font = QtGui.QFont()
                font.setFamily("Segoe UI")
                font.setPointSize(11)
                font.setBold(False)
                font.setItalic(False)
                font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
                self.tab2_textEdit_11.setFont(font)
                self.tab2_textEdit_11.setAutoFillBackground(True)
                self.tab2_textEdit_11.setStyleSheet("background-color: transparent;\n"
        "font: 11pt \"Segoe UI\";\n"
        "border: none;\n"
        "")
                self.tab2_textEdit_11.setReadOnly(True)
                self.tab2_textEdit_11.setObjectName("tab2_textEdit_11")
                self.tab2_Strawman_CheckBox = QtWidgets.QCheckBox(parent=self.tab_2)
                self.tab2_Strawman_CheckBox.setGeometry(QtCore.QRect(670, 94, 131, 41))
                font = QtGui.QFont()
                font.setFamily("Lufthansa Roman")
                font.setPointSize(13)
                font.setBold(False)
                font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferDefault)
                self.tab2_Strawman_CheckBox.setFont(font)
                self.tab2_Strawman_CheckBox.setAutoFillBackground(False)
                self.tab2_Strawman_CheckBox.setStyleSheet("")
                self.tab2_Strawman_CheckBox.setObjectName("tab2_Strawman_CheckBox")
                self.buttonGroup2.addButton(self.tab2_Strawman_CheckBox)
                self.tabWidget.addTab(self.tab_2, "")
                self.tab_3 = QtWidgets.QWidget()
                self.tab_3.setEnabled(False)
                self.tab_3.setAutoFillBackground(True)
                self.tab_3.setObjectName("tab_3")
                self.tab3_line_1 = QtWidgets.QFrame(parent=self.tab_3)
                self.tab3_line_1.setGeometry(QtCore.QRect(0, -8, 895, 21))
                self.tab3_line_1.setStyleSheet("QFrame#verticalSeparator {\n"
        "    border: 1px dotted #007bff; /* Border style */\n"
        "    height: 50px; /* Set the height for vertical separator */\n"
        "}\n"
        "")
                self.tab3_line_1.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
                self.tab3_line_1.setLineWidth(5)
                self.tab3_line_1.setFrameShape(QtWidgets.QFrame.Shape.HLine)
                self.tab3_line_1.setObjectName("tab3_line_1")
                self.tab3_line_2 = QtWidgets.QFrame(parent=self.tab_3)
                self.tab3_line_2.setGeometry(QtCore.QRect(440, 20, 20, 321))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
                self.tab3_line_2.setFont(font)
                self.tab3_line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
                self.tab3_line_2.setLineWidth(2)
                self.tab3_line_2.setFrameShape(QtWidgets.QFrame.Shape.VLine)
                self.tab3_line_2.setObjectName("tab3_line_2")
                self.tab3_textEdit_12 = QtWidgets.QTextEdit(parent=self.tab_3)
                self.tab3_textEdit_12.setGeometry(QtCore.QRect(60, 350, 801, 81))
                font = QtGui.QFont()
                font.setFamily("Segoe UI")
                font.setPointSize(11)
                font.setBold(False)
                font.setItalic(False)
                font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
                self.tab3_textEdit_12.setFont(font)
                self.tab3_textEdit_12.setAutoFillBackground(True)
                self.tab3_textEdit_12.setStyleSheet("background-color: transparent;\n"
        "font: 11pt \"Segoe UI\";\n"
        "border: none;\n"
        "")
                self.tab3_textEdit_12.setReadOnly(True)
                self.tab3_textEdit_12.setObjectName("tab3_textEdit_12")
                self.tab3_Copy_Text = QtWidgets.QTextEdit(parent=self.tab_3)
                self.tab3_Copy_Text.setGeometry(QtCore.QRect(160, 30, 121, 31))
                font = QtGui.QFont()
                font.setPointSize(9)
                font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
                self.tab3_Copy_Text.setFont(font)
                self.tab3_Copy_Text.setAutoFillBackground(True)
                self.tab3_Copy_Text.setStyleSheet("background-color: transparent;\n"
        "border: none;\n"
        "")
                self.tab3_Copy_Text.setReadOnly(True)
                self.tab3_Copy_Text.setObjectName("tab3_Copy_Text")
                self.tab3_Paste_Text = QtWidgets.QTextEdit(parent=self.tab_3)
                self.tab3_Paste_Text.setGeometry(QtCore.QRect(640, 30, 121, 31))
                font = QtGui.QFont()
                font.setPointSize(9)
                font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
                self.tab3_Paste_Text.setFont(font)
                self.tab3_Paste_Text.setAutoFillBackground(True)
                self.tab3_Paste_Text.setStyleSheet("background-color: transparent;\n"
        "border: none;\n"
        "")
                self.tab3_Paste_Text.setReadOnly(True)
                self.tab3_Paste_Text.setObjectName("tab3_Paste_Text")
                self.tab3_AL_Input_Text_2 = QtWidgets.QTextEdit(parent=self.tab_3)
                self.tab3_AL_Input_Text_2.setGeometry(QtCore.QRect(60, 120, 71, 31))
                font = QtGui.QFont()
                font.setPointSize(9)
                font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
                self.tab3_AL_Input_Text_2.setFont(font)
                self.tab3_AL_Input_Text_2.setAutoFillBackground(True)
                self.tab3_AL_Input_Text_2.setStyleSheet("background-color: transparent;\n"
        "border: none;\n"
        "")
                self.tab3_AL_Input_Text_2.setReadOnly(True)
                self.tab3_AL_Input_Text_2.setObjectName("tab3_AL_Input_Text_2")
                self.tab3_AL_Input_Box_2 = QtWidgets.QLineEdit(parent=self.tab_3)
                self.tab3_AL_Input_Box_2.setGeometry(QtCore.QRect(130, 115, 171, 31))
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.tab3_AL_Input_Box_2.sizePolicy().hasHeightForWidth())
                self.tab3_AL_Input_Box_2.setSizePolicy(sizePolicy)
                font = QtGui.QFont()
                font.setFamily("San Francisco")
                font.setPointSize(11)
                self.tab3_AL_Input_Box_2.setFont(font)
                self.tab3_AL_Input_Box_2.setStatusTip("")
                self.tab3_AL_Input_Box_2.setStyleSheet("font-family: \"San Francisco\", Arial, sans-serif;")
                self.tab3_AL_Input_Box_2.setText("")
                self.tab3_AL_Input_Box_2.setMaxLength(10)
                self.tab3_AL_Input_Box_2.setObjectName("tab3_AL_Input_Box_2")
                self.tab3_FolderNumber_2 = QtWidgets.QTextEdit(parent=self.tab_3)
                self.tab3_FolderNumber_2.setGeometry(QtCore.QRect(60, 215, 151, 31))
                font = QtGui.QFont()
                font.setPointSize(9)
                font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
                self.tab3_FolderNumber_2.setFont(font)
                self.tab3_FolderNumber_2.setAutoFillBackground(True)
                self.tab3_FolderNumber_2.setStyleSheet("background-color: transparent;\n"
        "border: none;\n"
        "")
                self.tab3_FolderNumber_2.setReadOnly(True)
                self.tab3_FolderNumber_2.setObjectName("tab3_FolderNumber_2")
                self.tab3_FolderNumberBox_2 = QtWidgets.QLineEdit(parent=self.tab_3)
                self.tab3_FolderNumberBox_2.setGeometry(QtCore.QRect(200, 210, 101, 31))
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.tab3_FolderNumberBox_2.sizePolicy().hasHeightForWidth())
                self.tab3_FolderNumberBox_2.setSizePolicy(sizePolicy)
                font = QtGui.QFont()
                font.setFamily("San Francisco")
                font.setPointSize(11)
                self.tab3_FolderNumberBox_2.setFont(font)
                self.tab3_FolderNumberBox_2.setStatusTip("")
                self.tab3_FolderNumberBox_2.setStyleSheet("font-family: \"San Francisco\", Arial, sans-serif;")
                self.tab3_FolderNumberBox_2.setText("")
                self.tab3_FolderNumberBox_2.setMaxLength(10)
                self.tab3_FolderNumberBox_2.setObjectName("tab3_FolderNumberBox_2")
                self.tab3_AL_Input_Text_3 = QtWidgets.QTextEdit(parent=self.tab_3)
                self.tab3_AL_Input_Text_3.setGeometry(QtCore.QRect(490, 120, 111, 31))
                font = QtGui.QFont()
                font.setPointSize(9)
                font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
                self.tab3_AL_Input_Text_3.setFont(font)
                self.tab3_AL_Input_Text_3.setAutoFillBackground(True)
                self.tab3_AL_Input_Text_3.setStyleSheet("background-color: transparent;\n"
        "border: none;\n"
        "")
                self.tab3_AL_Input_Text_3.setReadOnly(True)
                self.tab3_AL_Input_Text_3.setObjectName("tab3_AL_Input_Text_3")
                self.tab3_AL_Input_Text_4 = QtWidgets.QTextEdit(parent=self.tab_3)
                self.tab3_AL_Input_Text_4.setGeometry(QtCore.QRect(490, 210, 111, 31))
                font = QtGui.QFont()
                font.setPointSize(9)
                font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
                self.tab3_AL_Input_Text_4.setFont(font)
                self.tab3_AL_Input_Text_4.setAutoFillBackground(True)
                self.tab3_AL_Input_Text_4.setStyleSheet("background-color: transparent;\n"
        "border: none;\n"
        "")
                self.tab3_AL_Input_Text_4.setReadOnly(True)
                self.tab3_AL_Input_Text_4.setObjectName("tab3_AL_Input_Text_4")
                self.tab3_buttonBox_3 = QtWidgets.QDialogButtonBox(parent=self.tab_3)
                self.tab3_buttonBox_3.setGeometry(QtCore.QRect(710, 460, 151, 31))
                self.tab3_buttonBox_3.setMaximumSize(QtCore.QSize(171, 16777215))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
                self.tab3_buttonBox_3.setFont(font)
                self.tab3_buttonBox_3.setOrientation(QtCore.Qt.Orientation.Horizontal)
                self.tab3_buttonBox_3.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Ok)
                self.tab3_buttonBox_3.setObjectName("tab3_buttonBox_3")
                self.tabWidget.addTab(self.tab_3, "")

                self.retranslateUi(AutoFolder)
                self.tabWidget.setCurrentIndex(0)
                
                self.tab1_buttonBox.accepted.connect(self.create_folder) 
                self.tab1_buttonBox.rejected.connect(AutoFolder.close)
                self.tab1_TemplatesCheckBox.stateChanged.connect(self.enable_copy_button)
                self.tab1_buttonBox.button(QtWidgets.QDialogButtonBox.StandardButton.Ok).setEnabled(False)
                self.tab1_AL_Input_Box.textChanged.connect(self.mandatory_info_input)
                self.buttonGroup1.buttonClicked.connect(self.enable_disable_button)
                self.tab1_comboBox_1st.currentIndexChanged.connect(self.checkComboBoxes)
                self.tab1_comboBox_2nd.currentIndexChanged.connect(self.checkComboBoxes)
                self.tab1_comboBox_1st.currentIndexChanged.connect(self.updateComboBox2nd)
                self.tab1_Multi_CSC_Button.setChecked(False)
                self.tab1_Multi_CSC_Button.toggled.connect(self.multiple_CSC_select)
                self.tab1_RFP_CheckBox.clicked.connect(lambda: self.updateCheckBoxesState(self.tab1_RFP_CheckBox))
                self.tab1_RFP_Precheck_CheckBox.clicked.connect(lambda: self.updateCheckBoxesState(self.tab1_RFP_Precheck_CheckBox))
                self.tab1_RFP_Precheck_CheckBox.clicked.connect(lambda: self.disableButtonsInGroup2(self.tab1_RFP_Precheck_CheckBox))
                self.tab1_RFP_Precheck_CheckBox.stateChanged.connect(lambda: self.disableButtonsInGroup2(self.tab1_RFP_Precheck_CheckBox))
                self.tab1_RFP_CheckBox.clicked.connect(lambda: self.disableButtonsInGroup1(self.tab1_RFP_CheckBox))
                self.tab1_RFP_CheckBox.stateChanged.connect(lambda: self.disableButtonsInGroup1(self.tab1_RFP_CheckBox))
                current_date = QDate.currentDate()
                ui.tab1_dateEdit.setDate(current_date)
                
                QtCore.QMetaObject.connectSlotsByName(AutoFolder)

        def retranslateUi(self, AutoFolder):
                _translate = QtCore.QCoreApplication.translate
                AutoFolder.setWindowTitle(_translate("AutoFolder", "AutoFolder"))
                self.Status_Label.setText(_translate("AutoFolder", "Ready"))
                self.Version_Label.setText(_translate("AutoFolder", "Version 1 . 1 . 0"))
                self.tab1_Other_Button.setText(_translate("AutoFolder", "Other"))
                self.tab1_NA_Button.setText(_translate("AutoFolder", "N/A"))
                self.tab1_Multi_CSC_Button.setText(_translate("AutoFolder", "Multiple CSCs"))
                self.tab1_textEdit_6.setHtml(_translate("AutoFolder", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "hr { height: 1px; border-width: 0; }\n"
        "li.unchecked::marker { content: \"\\2610\"; }\n"
        "li.checked::marker { content: \"\\2612\"; }\n"
        "</style></head><body style=\" font-family:\'Segoe UI\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700; color:#7b7dff;\">( pick any day of the month )</span></p></body></html>"))
                self.tab1_textEdit_5.setHtml(_translate("AutoFolder", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "hr { height: 1px; border-width: 0; }\n"
        "li.unchecked::marker { content: \"\\2610\"; }\n"
        "li.checked::marker { content: \"\\2612\"; }\n"
        "</style></head><body style=\" font-family:\'Segoe UI\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700; color:#7b7dff;\">( select if three or more CSCs )</span></p></body></html>"))
                self.tab1_textEdit_8.setHtml(_translate("AutoFolder", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "hr { height: 1px; border-width: 0; }\n"
        "li.unchecked::marker { content: \"\\2610\"; }\n"
        "li.checked::marker { content: \"\\2612\"; }\n"
        "</style></head><body style=\" font-family:\'Segoe UI\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700; color:#7b7dff;\">( AS templates will be copied for AS project )</span></p></body></html>"))
                self.tab1_Profitability_Button.setText(_translate("AutoFolder", "Profitability"))
                self.tab1_textEdit_7.setHtml(_translate("AutoFolder", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "hr { height: 1px; border-width: 0; }\n"
        "li.unchecked::marker { content: \"\\2610\"; }\n"
        "li.checked::marker { content: \"\\2612\"; }\n"
        "</style></head><body style=\" font-family:\'Segoe UI\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#000000;\">(e.g., AA, B6, LH, 5Y, ARH)</span></p></body></html>"))
                self.tab1_PreMp_Button.setText(_translate("AutoFolder", "PreMP"))
                self.tab1_PostMp_Button.setText(_translate("AutoFolder", "PostMP"))
                self.tab1_textEdit_3.setHtml(_translate("AutoFolder", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "hr { height: 1px; border-width: 0; }\n"
        "li.unchecked::marker { content: \"\\2610\"; }\n"
        "li.checked::marker { content: \"\\2612\"; }\n"
        "</style></head><body style=\" font-family:\'Segoe UI\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
        "<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; text-decoration: underline; color:#000000;\">1</span><span style=\" font-size:9pt; text-decoration: underline; color:#000000;\">st</span><span style=\" text-decoration: underline; color:#000000;\">:</span></p></body></html>"))
                self.tab1_Price_Action_Button.setText(_translate("AutoFolder", "Price Action"))
                self.tab1_CSC_Input.setHtml(_translate("AutoFolder", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "hr { height: 1px; border-width: 0; }\n"
        "li.unchecked::marker { content: \"\\2610\"; }\n"
        "li.checked::marker { content: \"\\2612\"; }\n"
        "</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'San Francisco\'; font-size:11pt; font-weight:700;\">CSC</span></p></body></html>"))
                self.tab1_RFP_CheckBox.setText(_translate("AutoFolder", "RFP"))
                self.tab1_textEdit_4.setHtml(_translate("AutoFolder", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "hr { height: 1px; border-width: 0; }\n"
        "li.unchecked::marker { content: \"\\2610\"; }\n"
        "li.checked::marker { content: \"\\2612\"; }\n"
        "</style></head><body style=\" font-family:\'Segoe UI\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
        "<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; text-decoration: underline; color:#000000;\">2</span><span style=\" font-size:9pt; text-decoration: underline; color:#000000;\">nd</span><span style=\" text-decoration: underline; color:#000000;\">:</span></p></body></html>"))
                self.tab1_TemplatesCheckBox.setText(_translate("AutoFolder", "Copy RFP and MP templates from OSCAR"))
                self.tab1_RFP_Precheck_CheckBox.setText(_translate("AutoFolder", "RFP Precheck"))
                self.tab1_AL_Input_Box.setPlaceholderText(_translate("AutoFolder", "code only"))
                self.tab1_Project_Select.setHtml(_translate("AutoFolder", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "hr { height: 1px; border-width: 0; }\n"
        "li.unchecked::marker { content: \"\\2610\"; }\n"
        "li.checked::marker { content: \"\\2612\"; }\n"
        "</style></head><body style=\" font-family:\'Segoe UI\'; font-size:10pt; font-weight:700; font-style:normal;\">\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'San Francisco\'; font-size:11pt;\">Project</span></p></body></html>"))
                self.tab1_AL_Input_Text.setHtml(_translate("AutoFolder", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "hr { height: 1px; border-width: 0; }\n"
        "li.unchecked::marker { content: \"\\2610\"; }\n"
        "li.checked::marker { content: \"\\2612\"; }\n"
        "</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'San Francisco\'; font-size:11pt; font-weight:700;\">Airline</span></p></body></html>"))
                self.tab1_Date_Input.setHtml(_translate("AutoFolder", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "hr { height: 1px; border-width: 0; }\n"
        "li.unchecked::marker { content: \"\\2610\"; }\n"
        "li.checked::marker { content: \"\\2612\"; }\n"
        "</style></head><body style=\" font-family:\'Segoe UI\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'San Francisco\'; font-size:11pt; font-weight:700;\">Date</span></p></body></html>"))
                self.tab1_Cyc_Button.setText(_translate("AutoFolder", "Cycle Change"))
                self.tab1_comboBox_2nd.setItemText(1, _translate("AutoFolder", "ANC 1616"))
                self.tab1_comboBox_2nd.setItemText(2, _translate("AutoFolder", "ATL 1608"))
                self.tab1_comboBox_2nd.setItemText(3, _translate("AutoFolder", "AUS 0260"))
                self.tab1_comboBox_2nd.setItemText(4, _translate("AutoFolder", "BOS 1379"))
                self.tab1_comboBox_2nd.setItemText(5, _translate("AutoFolder", "BUR 1382"))
                self.tab1_comboBox_2nd.setItemText(6, _translate("AutoFolder", "BWI 1060"))
                self.tab1_comboBox_2nd.setItemText(7, _translate("AutoFolder", "CLT 1468"))
                self.tab1_comboBox_2nd.setItemText(8, _translate("AutoFolder", "DAL 3016"))
                self.tab1_comboBox_2nd.setItemText(9, _translate("AutoFolder", "DCA 1026"))
                self.tab1_comboBox_2nd.setItemText(10, _translate("AutoFolder", "DEN 0235"))
                self.tab1_comboBox_2nd.setItemText(11, _translate("AutoFolder", "DFIB 0194"))
                self.tab1_comboBox_2nd.setItemText(12, _translate("AutoFolder", "DFW 0195"))
                self.tab1_comboBox_2nd.setItemText(13, _translate("AutoFolder", "FLL 1682"))
                self.tab1_comboBox_2nd.setItemText(14, _translate("AutoFolder", "IAD 1059"))
                self.tab1_comboBox_2nd.setItemText(15, _translate("AutoFolder", "IAH 1316"))
                self.tab1_comboBox_2nd.setItemText(16, _translate("AutoFolder", "JFK 0425"))
                self.tab1_comboBox_2nd.setItemText(17, _translate("AutoFolder", "JFK 1371"))
                self.tab1_comboBox_2nd.setItemText(18, _translate("AutoFolder", "LAS 1681"))
                self.tab1_comboBox_2nd.setItemText(19, _translate("AutoFolder", "LAX 0370"))
                self.tab1_comboBox_2nd.setItemText(20, _translate("AutoFolder", "LGA 1505"))
                self.tab1_comboBox_2nd.setItemText(21, _translate("AutoFolder", "MCO 1479"))
                self.tab1_comboBox_2nd.setItemText(22, _translate("AutoFolder", "MIA 0145"))
                self.tab1_comboBox_2nd.setItemText(23, _translate("AutoFolder", "MIA 1366"))
                self.tab1_comboBox_2nd.setItemText(24, _translate("AutoFolder", "MSP 1390"))
                self.tab1_comboBox_2nd.setItemText(25, _translate("AutoFolder", "OAK 1304"))
                self.tab1_comboBox_2nd.setItemText(26, _translate("AutoFolder", "ONT 1383"))
                self.tab1_comboBox_2nd.setItemText(27, _translate("AutoFolder", "ORD 0165"))
                self.tab1_comboBox_2nd.setItemText(28, _translate("AutoFolder", "PAE 1611"))
                self.tab1_comboBox_2nd.setItemText(29, _translate("AutoFolder", "PBI 1476"))
                self.tab1_comboBox_2nd.setItemText(30, _translate("AutoFolder", "PDX 0710"))
                self.tab1_comboBox_2nd.setItemText(31, _translate("AutoFolder", "PHL 1376"))
                self.tab1_comboBox_2nd.setItemText(32, _translate("AutoFolder", "PHX 1692"))
                self.tab1_comboBox_2nd.setItemText(33, _translate("AutoFolder", "PIT 1375"))
                self.tab1_comboBox_2nd.setItemText(34, _translate("AutoFolder", "PSP 1683"))
                self.tab1_comboBox_2nd.setItemText(35, _translate("AutoFolder", "RDU 0460"))
                self.tab1_comboBox_2nd.setItemText(36, _translate("AutoFolder", "RSW 1481"))
                self.tab1_comboBox_2nd.setItemText(37, _translate("AutoFolder", "SAN 1721"))
                self.tab1_comboBox_2nd.setItemText(38, _translate("AutoFolder", "SEA 1612"))
                self.tab1_comboBox_2nd.setItemText(39, _translate("AutoFolder", "SFO 0790"))
                self.tab1_comboBox_2nd.setItemText(40, _translate("AutoFolder", "SJC 1393"))
                self.tab1_comboBox_2nd.setItemText(41, _translate("AutoFolder", "SMF 1302"))
                self.tab1_comboBox_2nd.setItemText(42, _translate("AutoFolder", "SNA 1381"))
                self.tab1_comboBox_2nd.setItemText(43, _translate("AutoFolder", "TPA 1483"))
                self.tab1_comboBox_2nd.setItemText(44, _translate("AutoFolder", "TUL 0870"))
                self.tab1_comboBox_1st.setPlaceholderText(_translate("AutoFolder", "1st"))
                self.tab1_comboBox_1st.setItemText(1, _translate("AutoFolder", "ANC 1616"))
                self.tab1_comboBox_1st.setItemText(2, _translate("AutoFolder", "ATL 1608"))
                self.tab1_comboBox_1st.setItemText(3, _translate("AutoFolder", "AUS 0260"))
                self.tab1_comboBox_1st.setItemText(4, _translate("AutoFolder", "BOS 1379"))
                self.tab1_comboBox_1st.setItemText(5, _translate("AutoFolder", "BUR 1382"))
                self.tab1_comboBox_1st.setItemText(6, _translate("AutoFolder", "BWI 1060"))
                self.tab1_comboBox_1st.setItemText(7, _translate("AutoFolder", "CLT 1468"))
                self.tab1_comboBox_1st.setItemText(8, _translate("AutoFolder", "DAL 3016"))
                self.tab1_comboBox_1st.setItemText(9, _translate("AutoFolder", "DCA 1026"))
                self.tab1_comboBox_1st.setItemText(10, _translate("AutoFolder", "DEN 0235"))
                self.tab1_comboBox_1st.setItemText(11, _translate("AutoFolder", "DFIB 0194"))
                self.tab1_comboBox_1st.setItemText(12, _translate("AutoFolder", "DFW 0195"))
                self.tab1_comboBox_1st.setItemText(13, _translate("AutoFolder", "FLL 1682"))
                self.tab1_comboBox_1st.setItemText(14, _translate("AutoFolder", "IAD 1059"))
                self.tab1_comboBox_1st.setItemText(15, _translate("AutoFolder", "IAH 1316"))
                self.tab1_comboBox_1st.setItemText(16, _translate("AutoFolder", "JFK 0425"))
                self.tab1_comboBox_1st.setItemText(17, _translate("AutoFolder", "JFK 1371"))
                self.tab1_comboBox_1st.setItemText(18, _translate("AutoFolder", "LAS 1681"))
                self.tab1_comboBox_1st.setItemText(19, _translate("AutoFolder", "LAX 0370"))
                self.tab1_comboBox_1st.setItemText(20, _translate("AutoFolder", "LGA 1505"))
                self.tab1_comboBox_1st.setItemText(21, _translate("AutoFolder", "MCO 1479"))
                self.tab1_comboBox_1st.setItemText(22, _translate("AutoFolder", "MIA 0145"))
                self.tab1_comboBox_1st.setItemText(23, _translate("AutoFolder", "MIA 1366"))
                self.tab1_comboBox_1st.setItemText(24, _translate("AutoFolder", "MSP 1390"))
                self.tab1_comboBox_1st.setItemText(25, _translate("AutoFolder", "OAK 1304"))
                self.tab1_comboBox_1st.setItemText(26, _translate("AutoFolder", "ONT 1383"))
                self.tab1_comboBox_1st.setItemText(27, _translate("AutoFolder", "ORD 0165"))
                self.tab1_comboBox_1st.setItemText(28, _translate("AutoFolder", "PAE 1611"))
                self.tab1_comboBox_1st.setItemText(29, _translate("AutoFolder", "PBI 1476"))
                self.tab1_comboBox_1st.setItemText(30, _translate("AutoFolder", "PDX 0710"))
                self.tab1_comboBox_1st.setItemText(31, _translate("AutoFolder", "PHL 1376"))
                self.tab1_comboBox_1st.setItemText(32, _translate("AutoFolder", "PHX 1692"))
                self.tab1_comboBox_1st.setItemText(33, _translate("AutoFolder", "PIT 1375"))
                self.tab1_comboBox_1st.setItemText(34, _translate("AutoFolder", "PSP 1683"))
                self.tab1_comboBox_1st.setItemText(35, _translate("AutoFolder", "RDU 0460"))
                self.tab1_comboBox_1st.setItemText(36, _translate("AutoFolder", "RSW 1481"))
                self.tab1_comboBox_1st.setItemText(37, _translate("AutoFolder", "SAN 1721"))
                self.tab1_comboBox_1st.setItemText(38, _translate("AutoFolder", "SEA 1612"))
                self.tab1_comboBox_1st.setItemText(39, _translate("AutoFolder", "SFO 0790"))
                self.tab1_comboBox_1st.setItemText(40, _translate("AutoFolder", "SJC 1393"))
                self.tab1_comboBox_1st.setItemText(41, _translate("AutoFolder", "SMF 1302"))
                self.tab1_comboBox_1st.setItemText(42, _translate("AutoFolder", "SNA 1381"))
                self.tab1_comboBox_1st.setItemText(43, _translate("AutoFolder", "TPA 1483"))
                self.tab1_comboBox_1st.setItemText(44, _translate("AutoFolder", "TUL 0870"))
                self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), _translate("AutoFolder", "Airline Folder"))
                self.tab2_textEdit_7.setHtml(_translate("AutoFolder", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "hr { height: 1px; border-width: 0; }\n"
        "li.unchecked::marker { content: \"\\2610\"; }\n"
        "li.checked::marker { content: \"\\2612\"; }\n"
        "</style></head><body style=\" font-family:\'Segoe UI\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#000000;\">(e.g., AA, B6, LH, 5Y, ARH)</span></p></body></html>"))
                self.tab2_AL_Input_Box.setPlaceholderText(_translate("AutoFolder", "code only"))
                self.tab2_AL_Input_Text.setHtml(_translate("AutoFolder", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "hr { height: 1px; border-width: 0; }\n"
        "li.unchecked::marker { content: \"\\2610\"; }\n"
        "li.checked::marker { content: \"\\2612\"; }\n"
        "</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'San Francisco\'; font-size:11pt; font-weight:700;\">Airline</span></p></body></html>"))
                self.tab2_FolderNumber.setHtml(_translate("AutoFolder", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "hr { height: 1px; border-width: 0; }\n"
        "li.unchecked::marker { content: \"\\2610\"; }\n"
        "li.checked::marker { content: \"\\2612\"; }\n"
        "</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'San Francisco\'; font-size:11pt; font-weight:700;\">Target Folder #</span></p></body></html>"))
                self.tab2_FolderNumberBox.setPlaceholderText(_translate("AutoFolder", "number only"))
                self.tab2_CSC_Input.setHtml(_translate("AutoFolder", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "hr { height: 1px; border-width: 0; }\n"
        "li.unchecked::marker { content: \"\\2610\"; }\n"
        "li.checked::marker { content: \"\\2612\"; }\n"
        "</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'San Francisco\'; font-size:11pt; font-weight:700;\">CSC</span></p></body></html>"))
                self.tab2_comboBox_1st.setItemText(1, _translate("AutoFolder", "ANC 1616"))
                self.tab2_comboBox_1st.setItemText(2, _translate("AutoFolder", "ATL 1608"))
                self.tab2_comboBox_1st.setItemText(3, _translate("AutoFolder", "AUS 0260"))
                self.tab2_comboBox_1st.setItemText(4, _translate("AutoFolder", "BOS 1379"))
                self.tab2_comboBox_1st.setItemText(5, _translate("AutoFolder", "BUR 1382"))
                self.tab2_comboBox_1st.setItemText(6, _translate("AutoFolder", "BWI 1060"))
                self.tab2_comboBox_1st.setItemText(7, _translate("AutoFolder", "CLT 1468"))
                self.tab2_comboBox_1st.setItemText(8, _translate("AutoFolder", "DAL 3016"))
                self.tab2_comboBox_1st.setItemText(9, _translate("AutoFolder", "DCA 1026"))
                self.tab2_comboBox_1st.setItemText(10, _translate("AutoFolder", "DEN 0235"))
                self.tab2_comboBox_1st.setItemText(11, _translate("AutoFolder", "DFIB 0194"))
                self.tab2_comboBox_1st.setItemText(12, _translate("AutoFolder", "DFW 0195"))
                self.tab2_comboBox_1st.setItemText(13, _translate("AutoFolder", "FLL 1682"))
                self.tab2_comboBox_1st.setItemText(14, _translate("AutoFolder", "IAD 1059"))
                self.tab2_comboBox_1st.setItemText(15, _translate("AutoFolder", "IAH 1316"))
                self.tab2_comboBox_1st.setItemText(16, _translate("AutoFolder", "JFK 0425"))
                self.tab2_comboBox_1st.setItemText(17, _translate("AutoFolder", "JFK 1371"))
                self.tab2_comboBox_1st.setItemText(18, _translate("AutoFolder", "LAS 1681"))
                self.tab2_comboBox_1st.setItemText(19, _translate("AutoFolder", "LAX 0370"))
                self.tab2_comboBox_1st.setItemText(20, _translate("AutoFolder", "LGA 1505"))
                self.tab2_comboBox_1st.setItemText(21, _translate("AutoFolder", "MCO 1479"))
                self.tab2_comboBox_1st.setItemText(22, _translate("AutoFolder", "MIA 0145"))
                self.tab2_comboBox_1st.setItemText(23, _translate("AutoFolder", "MIA 1366"))
                self.tab2_comboBox_1st.setItemText(24, _translate("AutoFolder", "MSP 1390"))
                self.tab2_comboBox_1st.setItemText(25, _translate("AutoFolder", "OAK 1304"))
                self.tab2_comboBox_1st.setItemText(26, _translate("AutoFolder", "ONT 1383"))
                self.tab2_comboBox_1st.setItemText(27, _translate("AutoFolder", "ORD 0165"))
                self.tab2_comboBox_1st.setItemText(28, _translate("AutoFolder", "PAE 1611"))
                self.tab2_comboBox_1st.setItemText(29, _translate("AutoFolder", "PBI 1476"))
                self.tab2_comboBox_1st.setItemText(30, _translate("AutoFolder", "PDX 0710"))
                self.tab2_comboBox_1st.setItemText(31, _translate("AutoFolder", "PHL 1376"))
                self.tab2_comboBox_1st.setItemText(32, _translate("AutoFolder", "PHX 1692"))
                self.tab2_comboBox_1st.setItemText(33, _translate("AutoFolder", "PIT 1375"))
                self.tab2_comboBox_1st.setItemText(34, _translate("AutoFolder", "PSP 1683"))
                self.tab2_comboBox_1st.setItemText(35, _translate("AutoFolder", "RDU 0460"))
                self.tab2_comboBox_1st.setItemText(36, _translate("AutoFolder", "RSW 1481"))
                self.tab2_comboBox_1st.setItemText(37, _translate("AutoFolder", "SAN 1721"))
                self.tab2_comboBox_1st.setItemText(38, _translate("AutoFolder", "SEA 1612"))
                self.tab2_comboBox_1st.setItemText(39, _translate("AutoFolder", "SFO 0790"))
                self.tab2_comboBox_1st.setItemText(40, _translate("AutoFolder", "SJC 1393"))
                self.tab2_comboBox_1st.setItemText(41, _translate("AutoFolder", "SMF 1302"))
                self.tab2_comboBox_1st.setItemText(42, _translate("AutoFolder", "SNA 1381"))
                self.tab2_comboBox_1st.setItemText(43, _translate("AutoFolder", "TPA 1483"))
                self.tab2_comboBox_1st.setItemText(44, _translate("AutoFolder", "TUL 0870"))
                self.tab2_comboBox_2nd.setItemText(1, _translate("AutoFolder", "ANC 1616"))
                self.tab2_comboBox_2nd.setItemText(2, _translate("AutoFolder", "ATL 1608"))
                self.tab2_comboBox_2nd.setItemText(3, _translate("AutoFolder", "AUS 0260"))
                self.tab2_comboBox_2nd.setItemText(4, _translate("AutoFolder", "BOS 1379"))
                self.tab2_comboBox_2nd.setItemText(5, _translate("AutoFolder", "BUR 1382"))
                self.tab2_comboBox_2nd.setItemText(6, _translate("AutoFolder", "BWI 1060"))
                self.tab2_comboBox_2nd.setItemText(7, _translate("AutoFolder", "CLT 1468"))
                self.tab2_comboBox_2nd.setItemText(8, _translate("AutoFolder", "DAL 3016"))
                self.tab2_comboBox_2nd.setItemText(9, _translate("AutoFolder", "DCA 1026"))
                self.tab2_comboBox_2nd.setItemText(10, _translate("AutoFolder", "DEN 0235"))
                self.tab2_comboBox_2nd.setItemText(11, _translate("AutoFolder", "DFIB 0194"))
                self.tab2_comboBox_2nd.setItemText(12, _translate("AutoFolder", "DFW 0195"))
                self.tab2_comboBox_2nd.setItemText(13, _translate("AutoFolder", "FLL 1682"))
                self.tab2_comboBox_2nd.setItemText(14, _translate("AutoFolder", "IAD 1059"))
                self.tab2_comboBox_2nd.setItemText(15, _translate("AutoFolder", "IAH 1316"))
                self.tab2_comboBox_2nd.setItemText(16, _translate("AutoFolder", "JFK 0425"))
                self.tab2_comboBox_2nd.setItemText(17, _translate("AutoFolder", "JFK 1371"))
                self.tab2_comboBox_2nd.setItemText(18, _translate("AutoFolder", "LAS 1681"))
                self.tab2_comboBox_2nd.setItemText(19, _translate("AutoFolder", "LAX 0370"))
                self.tab2_comboBox_2nd.setItemText(20, _translate("AutoFolder", "LGA 1505"))
                self.tab2_comboBox_2nd.setItemText(21, _translate("AutoFolder", "MCO 1479"))
                self.tab2_comboBox_2nd.setItemText(22, _translate("AutoFolder", "MIA 0145"))
                self.tab2_comboBox_2nd.setItemText(23, _translate("AutoFolder", "MIA 1366"))
                self.tab2_comboBox_2nd.setItemText(24, _translate("AutoFolder", "MSP 1390"))
                self.tab2_comboBox_2nd.setItemText(25, _translate("AutoFolder", "OAK 1304"))
                self.tab2_comboBox_2nd.setItemText(26, _translate("AutoFolder", "ONT 1383"))
                self.tab2_comboBox_2nd.setItemText(27, _translate("AutoFolder", "ORD 0165"))
                self.tab2_comboBox_2nd.setItemText(28, _translate("AutoFolder", "PAE 1611"))
                self.tab2_comboBox_2nd.setItemText(29, _translate("AutoFolder", "PBI 1476"))
                self.tab2_comboBox_2nd.setItemText(30, _translate("AutoFolder", "PDX 0710"))
                self.tab2_comboBox_2nd.setItemText(31, _translate("AutoFolder", "PHL 1376"))
                self.tab2_comboBox_2nd.setItemText(32, _translate("AutoFolder", "PHX 1692"))
                self.tab2_comboBox_2nd.setItemText(33, _translate("AutoFolder", "PIT 1375"))
                self.tab2_comboBox_2nd.setItemText(34, _translate("AutoFolder", "PSP 1683"))
                self.tab2_comboBox_2nd.setItemText(35, _translate("AutoFolder", "RDU 0460"))
                self.tab2_comboBox_2nd.setItemText(36, _translate("AutoFolder", "RSW 1481"))
                self.tab2_comboBox_2nd.setItemText(37, _translate("AutoFolder", "SAN 1721"))
                self.tab2_comboBox_2nd.setItemText(38, _translate("AutoFolder", "SEA 1612"))
                self.tab2_comboBox_2nd.setItemText(39, _translate("AutoFolder", "SFO 0790"))
                self.tab2_comboBox_2nd.setItemText(40, _translate("AutoFolder", "SJC 1393"))
                self.tab2_comboBox_2nd.setItemText(41, _translate("AutoFolder", "SMF 1302"))
                self.tab2_comboBox_2nd.setItemText(42, _translate("AutoFolder", "SNA 1381"))
                self.tab2_comboBox_2nd.setItemText(43, _translate("AutoFolder", "TPA 1483"))
                self.tab2_comboBox_2nd.setItemText(44, _translate("AutoFolder", "TUL 0870"))
                self.tab2_comboBox_3rd.setItemText(1, _translate("AutoFolder", "ANC 1616"))
                self.tab2_comboBox_3rd.setItemText(2, _translate("AutoFolder", "ATL 1608"))
                self.tab2_comboBox_3rd.setItemText(3, _translate("AutoFolder", "AUS 0260"))
                self.tab2_comboBox_3rd.setItemText(4, _translate("AutoFolder", "BOS 1379"))
                self.tab2_comboBox_3rd.setItemText(5, _translate("AutoFolder", "BUR 1382"))
                self.tab2_comboBox_3rd.setItemText(6, _translate("AutoFolder", "BWI 1060"))
                self.tab2_comboBox_3rd.setItemText(7, _translate("AutoFolder", "CLT 1468"))
                self.tab2_comboBox_3rd.setItemText(8, _translate("AutoFolder", "DAL 3016"))
                self.tab2_comboBox_3rd.setItemText(9, _translate("AutoFolder", "DCA 1026"))
                self.tab2_comboBox_3rd.setItemText(10, _translate("AutoFolder", "DEN 0235"))
                self.tab2_comboBox_3rd.setItemText(11, _translate("AutoFolder", "DFIB 0194"))
                self.tab2_comboBox_3rd.setItemText(12, _translate("AutoFolder", "DFW 0195"))
                self.tab2_comboBox_3rd.setItemText(13, _translate("AutoFolder", "FLL 1682"))
                self.tab2_comboBox_3rd.setItemText(14, _translate("AutoFolder", "IAD 1059"))
                self.tab2_comboBox_3rd.setItemText(15, _translate("AutoFolder", "IAH 1316"))
                self.tab2_comboBox_3rd.setItemText(16, _translate("AutoFolder", "JFK 0425"))
                self.tab2_comboBox_3rd.setItemText(17, _translate("AutoFolder", "JFK 1371"))
                self.tab2_comboBox_3rd.setItemText(18, _translate("AutoFolder", "LAS 1681"))
                self.tab2_comboBox_3rd.setItemText(19, _translate("AutoFolder", "LAX 0370"))
                self.tab2_comboBox_3rd.setItemText(20, _translate("AutoFolder", "LGA 1505"))
                self.tab2_comboBox_3rd.setItemText(21, _translate("AutoFolder", "MCO 1479"))
                self.tab2_comboBox_3rd.setItemText(22, _translate("AutoFolder", "MIA 0145"))
                self.tab2_comboBox_3rd.setItemText(23, _translate("AutoFolder", "MIA 1366"))
                self.tab2_comboBox_3rd.setItemText(24, _translate("AutoFolder", "MSP 1390"))
                self.tab2_comboBox_3rd.setItemText(25, _translate("AutoFolder", "OAK 1304"))
                self.tab2_comboBox_3rd.setItemText(26, _translate("AutoFolder", "ONT 1383"))
                self.tab2_comboBox_3rd.setItemText(27, _translate("AutoFolder", "ORD 0165"))
                self.tab2_comboBox_3rd.setItemText(28, _translate("AutoFolder", "PAE 1611"))
                self.tab2_comboBox_3rd.setItemText(29, _translate("AutoFolder", "PBI 1476"))
                self.tab2_comboBox_3rd.setItemText(30, _translate("AutoFolder", "PDX 0710"))
                self.tab2_comboBox_3rd.setItemText(31, _translate("AutoFolder", "PHL 1376"))
                self.tab2_comboBox_3rd.setItemText(32, _translate("AutoFolder", "PHX 1692"))
                self.tab2_comboBox_3rd.setItemText(33, _translate("AutoFolder", "PIT 1375"))
                self.tab2_comboBox_3rd.setItemText(34, _translate("AutoFolder", "PSP 1683"))
                self.tab2_comboBox_3rd.setItemText(35, _translate("AutoFolder", "RDU 0460"))
                self.tab2_comboBox_3rd.setItemText(36, _translate("AutoFolder", "RSW 1481"))
                self.tab2_comboBox_3rd.setItemText(37, _translate("AutoFolder", "SAN 1721"))
                self.tab2_comboBox_3rd.setItemText(38, _translate("AutoFolder", "SEA 1612"))
                self.tab2_comboBox_3rd.setItemText(39, _translate("AutoFolder", "SFO 0790"))
                self.tab2_comboBox_3rd.setItemText(40, _translate("AutoFolder", "SJC 1393"))
                self.tab2_comboBox_3rd.setItemText(41, _translate("AutoFolder", "SMF 1302"))
                self.tab2_comboBox_3rd.setItemText(42, _translate("AutoFolder", "SNA 1381"))
                self.tab2_comboBox_3rd.setItemText(43, _translate("AutoFolder", "TPA 1483"))
                self.tab2_comboBox_3rd.setItemText(44, _translate("AutoFolder", "TUL 0870"))
                self.tab2_comboBox_4th.setItemText(1, _translate("AutoFolder", "ANC 1616"))
                self.tab2_comboBox_4th.setItemText(2, _translate("AutoFolder", "ATL 1608"))
                self.tab2_comboBox_4th.setItemText(3, _translate("AutoFolder", "AUS 0260"))
                self.tab2_comboBox_4th.setItemText(4, _translate("AutoFolder", "BOS 1379"))
                self.tab2_comboBox_4th.setItemText(5, _translate("AutoFolder", "BUR 1382"))
                self.tab2_comboBox_4th.setItemText(6, _translate("AutoFolder", "BWI 1060"))
                self.tab2_comboBox_4th.setItemText(7, _translate("AutoFolder", "CLT 1468"))
                self.tab2_comboBox_4th.setItemText(8, _translate("AutoFolder", "DAL 3016"))
                self.tab2_comboBox_4th.setItemText(9, _translate("AutoFolder", "DCA 1026"))
                self.tab2_comboBox_4th.setItemText(10, _translate("AutoFolder", "DEN 0235"))
                self.tab2_comboBox_4th.setItemText(11, _translate("AutoFolder", "DFIB 0194"))
                self.tab2_comboBox_4th.setItemText(12, _translate("AutoFolder", "DFW 0195"))
                self.tab2_comboBox_4th.setItemText(13, _translate("AutoFolder", "FLL 1682"))
                self.tab2_comboBox_4th.setItemText(14, _translate("AutoFolder", "IAD 1059"))
                self.tab2_comboBox_4th.setItemText(15, _translate("AutoFolder", "IAH 1316"))
                self.tab2_comboBox_4th.setItemText(16, _translate("AutoFolder", "JFK 0425"))
                self.tab2_comboBox_4th.setItemText(17, _translate("AutoFolder", "JFK 1371"))
                self.tab2_comboBox_4th.setItemText(18, _translate("AutoFolder", "LAS 1681"))
                self.tab2_comboBox_4th.setItemText(19, _translate("AutoFolder", "LAX 0370"))
                self.tab2_comboBox_4th.setItemText(20, _translate("AutoFolder", "LGA 1505"))
                self.tab2_comboBox_4th.setItemText(21, _translate("AutoFolder", "MCO 1479"))
                self.tab2_comboBox_4th.setItemText(22, _translate("AutoFolder", "MIA 0145"))
                self.tab2_comboBox_4th.setItemText(23, _translate("AutoFolder", "MIA 1366"))
                self.tab2_comboBox_4th.setItemText(24, _translate("AutoFolder", "MSP 1390"))
                self.tab2_comboBox_4th.setItemText(25, _translate("AutoFolder", "OAK 1304"))
                self.tab2_comboBox_4th.setItemText(26, _translate("AutoFolder", "ONT 1383"))
                self.tab2_comboBox_4th.setItemText(27, _translate("AutoFolder", "ORD 0165"))
                self.tab2_comboBox_4th.setItemText(28, _translate("AutoFolder", "PAE 1611"))
                self.tab2_comboBox_4th.setItemText(29, _translate("AutoFolder", "PBI 1476"))
                self.tab2_comboBox_4th.setItemText(30, _translate("AutoFolder", "PDX 0710"))
                self.tab2_comboBox_4th.setItemText(31, _translate("AutoFolder", "PHL 1376"))
                self.tab2_comboBox_4th.setItemText(32, _translate("AutoFolder", "PHX 1692"))
                self.tab2_comboBox_4th.setItemText(33, _translate("AutoFolder", "PIT 1375"))
                self.tab2_comboBox_4th.setItemText(34, _translate("AutoFolder", "PSP 1683"))
                self.tab2_comboBox_4th.setItemText(35, _translate("AutoFolder", "RDU 0460"))
                self.tab2_comboBox_4th.setItemText(36, _translate("AutoFolder", "RSW 1481"))
                self.tab2_comboBox_4th.setItemText(37, _translate("AutoFolder", "SAN 1721"))
                self.tab2_comboBox_4th.setItemText(38, _translate("AutoFolder", "SEA 1612"))
                self.tab2_comboBox_4th.setItemText(39, _translate("AutoFolder", "SFO 0790"))
                self.tab2_comboBox_4th.setItemText(40, _translate("AutoFolder", "SJC 1393"))
                self.tab2_comboBox_4th.setItemText(41, _translate("AutoFolder", "SMF 1302"))
                self.tab2_comboBox_4th.setItemText(42, _translate("AutoFolder", "SNA 1381"))
                self.tab2_comboBox_4th.setItemText(43, _translate("AutoFolder", "TPA 1483"))
                self.tab2_comboBox_4th.setItemText(44, _translate("AutoFolder", "TUL 0870"))
                self.tab2_comboBox_5th.setItemText(1, _translate("AutoFolder", "ANC 1616"))
                self.tab2_comboBox_5th.setItemText(2, _translate("AutoFolder", "ATL 1608"))
                self.tab2_comboBox_5th.setItemText(3, _translate("AutoFolder", "AUS 0260"))
                self.tab2_comboBox_5th.setItemText(4, _translate("AutoFolder", "BOS 1379"))
                self.tab2_comboBox_5th.setItemText(5, _translate("AutoFolder", "BUR 1382"))
                self.tab2_comboBox_5th.setItemText(6, _translate("AutoFolder", "BWI 1060"))
                self.tab2_comboBox_5th.setItemText(7, _translate("AutoFolder", "CLT 1468"))
                self.tab2_comboBox_5th.setItemText(8, _translate("AutoFolder", "DAL 3016"))
                self.tab2_comboBox_5th.setItemText(9, _translate("AutoFolder", "DCA 1026"))
                self.tab2_comboBox_5th.setItemText(10, _translate("AutoFolder", "DEN 0235"))
                self.tab2_comboBox_5th.setItemText(11, _translate("AutoFolder", "DFIB 0194"))
                self.tab2_comboBox_5th.setItemText(12, _translate("AutoFolder", "DFW 0195"))
                self.tab2_comboBox_5th.setItemText(13, _translate("AutoFolder", "FLL 1682"))
                self.tab2_comboBox_5th.setItemText(14, _translate("AutoFolder", "IAD 1059"))
                self.tab2_comboBox_5th.setItemText(15, _translate("AutoFolder", "IAH 1316"))
                self.tab2_comboBox_5th.setItemText(16, _translate("AutoFolder", "JFK 0425"))
                self.tab2_comboBox_5th.setItemText(17, _translate("AutoFolder", "JFK 1371"))
                self.tab2_comboBox_5th.setItemText(18, _translate("AutoFolder", "LAS 1681"))
                self.tab2_comboBox_5th.setItemText(19, _translate("AutoFolder", "LAX 0370"))
                self.tab2_comboBox_5th.setItemText(20, _translate("AutoFolder", "LGA 1505"))
                self.tab2_comboBox_5th.setItemText(21, _translate("AutoFolder", "MCO 1479"))
                self.tab2_comboBox_5th.setItemText(22, _translate("AutoFolder", "MIA 0145"))
                self.tab2_comboBox_5th.setItemText(23, _translate("AutoFolder", "MIA 1366"))
                self.tab2_comboBox_5th.setItemText(24, _translate("AutoFolder", "MSP 1390"))
                self.tab2_comboBox_5th.setItemText(25, _translate("AutoFolder", "OAK 1304"))
                self.tab2_comboBox_5th.setItemText(26, _translate("AutoFolder", "ONT 1383"))
                self.tab2_comboBox_5th.setItemText(27, _translate("AutoFolder", "ORD 0165"))
                self.tab2_comboBox_5th.setItemText(28, _translate("AutoFolder", "PAE 1611"))
                self.tab2_comboBox_5th.setItemText(29, _translate("AutoFolder", "PBI 1476"))
                self.tab2_comboBox_5th.setItemText(30, _translate("AutoFolder", "PDX 0710"))
                self.tab2_comboBox_5th.setItemText(31, _translate("AutoFolder", "PHL 1376"))
                self.tab2_comboBox_5th.setItemText(32, _translate("AutoFolder", "PHX 1692"))
                self.tab2_comboBox_5th.setItemText(33, _translate("AutoFolder", "PIT 1375"))
                self.tab2_comboBox_5th.setItemText(34, _translate("AutoFolder", "PSP 1683"))
                self.tab2_comboBox_5th.setItemText(35, _translate("AutoFolder", "RDU 0460"))
                self.tab2_comboBox_5th.setItemText(36, _translate("AutoFolder", "RSW 1481"))
                self.tab2_comboBox_5th.setItemText(37, _translate("AutoFolder", "SAN 1721"))
                self.tab2_comboBox_5th.setItemText(38, _translate("AutoFolder", "SEA 1612"))
                self.tab2_comboBox_5th.setItemText(39, _translate("AutoFolder", "SFO 0790"))
                self.tab2_comboBox_5th.setItemText(40, _translate("AutoFolder", "SJC 1393"))
                self.tab2_comboBox_5th.setItemText(41, _translate("AutoFolder", "SMF 1302"))
                self.tab2_comboBox_5th.setItemText(42, _translate("AutoFolder", "SNA 1381"))
                self.tab2_comboBox_5th.setItemText(43, _translate("AutoFolder", "TPA 1483"))
                self.tab2_comboBox_5th.setItemText(44, _translate("AutoFolder", "TUL 0870"))
                self.tab2_comboBox_6th.setItemText(1, _translate("AutoFolder", "ANC 1616"))
                self.tab2_comboBox_6th.setItemText(2, _translate("AutoFolder", "ATL 1608"))
                self.tab2_comboBox_6th.setItemText(3, _translate("AutoFolder", "AUS 0260"))
                self.tab2_comboBox_6th.setItemText(4, _translate("AutoFolder", "BOS 1379"))
                self.tab2_comboBox_6th.setItemText(5, _translate("AutoFolder", "BUR 1382"))
                self.tab2_comboBox_6th.setItemText(6, _translate("AutoFolder", "BWI 1060"))
                self.tab2_comboBox_6th.setItemText(7, _translate("AutoFolder", "CLT 1468"))
                self.tab2_comboBox_6th.setItemText(8, _translate("AutoFolder", "DAL 3016"))
                self.tab2_comboBox_6th.setItemText(9, _translate("AutoFolder", "DCA 1026"))
                self.tab2_comboBox_6th.setItemText(10, _translate("AutoFolder", "DEN 0235"))
                self.tab2_comboBox_6th.setItemText(11, _translate("AutoFolder", "DFIB 0194"))
                self.tab2_comboBox_6th.setItemText(12, _translate("AutoFolder", "DFW 0195"))
                self.tab2_comboBox_6th.setItemText(13, _translate("AutoFolder", "FLL 1682"))
                self.tab2_comboBox_6th.setItemText(14, _translate("AutoFolder", "IAD 1059"))
                self.tab2_comboBox_6th.setItemText(15, _translate("AutoFolder", "IAH 1316"))
                self.tab2_comboBox_6th.setItemText(16, _translate("AutoFolder", "JFK 0425"))
                self.tab2_comboBox_6th.setItemText(17, _translate("AutoFolder", "JFK 1371"))
                self.tab2_comboBox_6th.setItemText(18, _translate("AutoFolder", "LAS 1681"))
                self.tab2_comboBox_6th.setItemText(19, _translate("AutoFolder", "LAX 0370"))
                self.tab2_comboBox_6th.setItemText(20, _translate("AutoFolder", "LGA 1505"))
                self.tab2_comboBox_6th.setItemText(21, _translate("AutoFolder", "MCO 1479"))
                self.tab2_comboBox_6th.setItemText(22, _translate("AutoFolder", "MIA 0145"))
                self.tab2_comboBox_6th.setItemText(23, _translate("AutoFolder", "MIA 1366"))
                self.tab2_comboBox_6th.setItemText(24, _translate("AutoFolder", "MSP 1390"))
                self.tab2_comboBox_6th.setItemText(25, _translate("AutoFolder", "OAK 1304"))
                self.tab2_comboBox_6th.setItemText(26, _translate("AutoFolder", "ONT 1383"))
                self.tab2_comboBox_6th.setItemText(27, _translate("AutoFolder", "ORD 0165"))
                self.tab2_comboBox_6th.setItemText(28, _translate("AutoFolder", "PAE 1611"))
                self.tab2_comboBox_6th.setItemText(29, _translate("AutoFolder", "PBI 1476"))
                self.tab2_comboBox_6th.setItemText(30, _translate("AutoFolder", "PDX 0710"))
                self.tab2_comboBox_6th.setItemText(31, _translate("AutoFolder", "PHL 1376"))
                self.tab2_comboBox_6th.setItemText(32, _translate("AutoFolder", "PHX 1692"))
                self.tab2_comboBox_6th.setItemText(33, _translate("AutoFolder", "PIT 1375"))
                self.tab2_comboBox_6th.setItemText(34, _translate("AutoFolder", "PSP 1683"))
                self.tab2_comboBox_6th.setItemText(35, _translate("AutoFolder", "RDU 0460"))
                self.tab2_comboBox_6th.setItemText(36, _translate("AutoFolder", "RSW 1481"))
                self.tab2_comboBox_6th.setItemText(37, _translate("AutoFolder", "SAN 1721"))
                self.tab2_comboBox_6th.setItemText(38, _translate("AutoFolder", "SEA 1612"))
                self.tab2_comboBox_6th.setItemText(39, _translate("AutoFolder", "SFO 0790"))
                self.tab2_comboBox_6th.setItemText(40, _translate("AutoFolder", "SJC 1393"))
                self.tab2_comboBox_6th.setItemText(41, _translate("AutoFolder", "SMF 1302"))
                self.tab2_comboBox_6th.setItemText(42, _translate("AutoFolder", "SNA 1381"))
                self.tab2_comboBox_6th.setItemText(43, _translate("AutoFolder", "TPA 1483"))
                self.tab2_comboBox_6th.setItemText(44, _translate("AutoFolder", "TUL 0870"))
                self.tab2_textEdit_3.setHtml(_translate("AutoFolder", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "hr { height: 1px; border-width: 0; }\n"
        "li.unchecked::marker { content: \"\\2610\"; }\n"
        "li.checked::marker { content: \"\\2612\"; }\n"
        "</style></head><body style=\" font-family:\'Segoe UI\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
        "<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; text-decoration: underline; color:#000000;\">1</span><span style=\" font-size:9pt; text-decoration: underline; color:#000000;\">st</span><span style=\" text-decoration: underline; color:#000000;\">:</span></p></body></html>"))
                self.tab2_textEdit_4.setHtml(_translate("AutoFolder", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "hr { height: 1px; border-width: 0; }\n"
        "li.unchecked::marker { content: \"\\2610\"; }\n"
        "li.checked::marker { content: \"\\2612\"; }\n"
        "</style></head><body style=\" font-family:\'Segoe UI\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
        "<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; text-decoration: underline; color:#000000;\">2</span><span style=\" font-size:9pt; text-decoration: underline; color:#000000;\">nd</span><span style=\" text-decoration: underline; color:#000000;\">:</span></p></body></html>"))
                self.tab2_textEdit_5.setHtml(_translate("AutoFolder", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "hr { height: 1px; border-width: 0; }\n"
        "li.unchecked::marker { content: \"\\2610\"; }\n"
        "li.checked::marker { content: \"\\2612\"; }\n"
        "</style></head><body style=\" font-family:\'Segoe UI\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
        "<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; text-decoration: underline; color:#000000;\">3</span><span style=\" font-size:9pt; text-decoration: underline; color:#000000;\">rd</span><span style=\" text-decoration: underline; color:#000000;\">:</span></p></body></html>"))
                self.tab2_textEdit_6.setHtml(_translate("AutoFolder", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "hr { height: 1px; border-width: 0; }\n"
        "li.unchecked::marker { content: \"\\2610\"; }\n"
        "li.checked::marker { content: \"\\2612\"; }\n"
        "</style></head><body style=\" font-family:\'Segoe UI\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
        "<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; text-decoration: underline; color:#000000;\">4</span><span style=\" font-size:9pt; text-decoration: underline; color:#000000;\">th</span><span style=\" text-decoration: underline; color:#000000;\">:</span></p></body></html>"))
                self.tab2_textEdit_8.setHtml(_translate("AutoFolder", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "hr { height: 1px; border-width: 0; }\n"
        "li.unchecked::marker { content: \"\\2610\"; }\n"
        "li.checked::marker { content: \"\\2612\"; }\n"
        "</style></head><body style=\" font-family:\'Segoe UI\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
        "<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; text-decoration: underline; color:#000000;\">5</span><span style=\" font-size:9pt; text-decoration: underline; color:#000000;\">th</span><span style=\" text-decoration: underline; color:#000000;\">:</span></p></body></html>"))
                self.tab2_textEdit_9.setHtml(_translate("AutoFolder", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "hr { height: 1px; border-width: 0; }\n"
        "li.unchecked::marker { content: \"\\2610\"; }\n"
        "li.checked::marker { content: \"\\2612\"; }\n"
        "</style></head><body style=\" font-family:\'Segoe UI\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
        "<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; text-decoration: underline; color:#000000;\">6</span><span style=\" font-size:9pt; text-decoration: underline; color:#000000;\">th</span><span style=\" text-decoration: underline; color:#000000;\">:</span></p></body></html>"))
                self.tab2_Date_Input.setHtml(_translate("AutoFolder", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "hr { height: 1px; border-width: 0; }\n"
        "li.unchecked::marker { content: \"\\2610\"; }\n"
        "li.checked::marker { content: \"\\2612\"; }\n"
        "</style></head><body style=\" font-family:\'Segoe UI\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'San Francisco\'; font-size:11pt; font-weight:700;\">Date</span></p></body></html>"))
                self.tab2_textEdit_10.setHtml(_translate("AutoFolder", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "hr { height: 1px; border-width: 0; }\n"
        "li.unchecked::marker { content: \"\\2610\"; }\n"
        "li.checked::marker { content: \"\\2612\"; }\n"
        "</style></head><body style=\" font-family:\'Segoe UI\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700; color:#7b7dff;\">( pick any day of the month )</span></p></body></html>"))
                self.tab2_MPL_CheckBox.setText(_translate("AutoFolder", "MPL"))
                self.tab2_Output_CheckBox.setText(_translate("AutoFolder", "Output File"))
                self.tab2_FileType.setHtml(_translate("AutoFolder", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "hr { height: 1px; border-width: 0; }\n"
        "li.unchecked::marker { content: \"\\2610\"; }\n"
        "li.checked::marker { content: \"\\2612\"; }\n"
        "</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'San Francisco\'; font-size:11pt; font-weight:700;\">Select File to Create</span></p></body></html>"))
                self.tab2_AcService_CheckBox.setText(_translate("AutoFolder", "AC_Service"))
                self.tab2_textEdit_11.setHtml(_translate("AutoFolder", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "hr { height: 1px; border-width: 0; }\n"
        "li.unchecked::marker { content: \"\\2610\"; }\n"
        "li.checked::marker { content: \"\\2612\"; }\n"
        "</style></head><body style=\" font-family:\'Segoe UI\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:700; color:#7b7dff;\">Note: Only one MPL file will be created regradless the selection of CSC</span></p></body></html>"))
                self.tab2_Strawman_CheckBox.setText(_translate("AutoFolder", "Strawman"))
                self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("AutoFolder", "Costing Files"))
                self.tab3_textEdit_12.setHtml(_translate("AutoFolder", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "hr { height: 1px; border-width: 0; }\n"
        "li.unchecked::marker { content: \"\\2610\"; }\n"
        "li.checked::marker { content: \"\\2612\"; }\n"
        "</style></head><body style=\" font-family:\'Segoe UI\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700; color:#7b7dff;\">This tab serves two purposes:</span></p>\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700; color:#7b7dff;\">1. Automaticly create a total costing deliverable folder for project submission, based on the AL selected</span></p>\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700; color:#7b7dff;\">2. Copy and paste costing deliverables into the new folder</span></p></body></html>"))
                self.tab3_Copy_Text.setHtml(_translate("AutoFolder", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "hr { height: 1px; border-width: 0; }\n"
        "li.unchecked::marker { content: \"\\2610\"; }\n"
        "li.checked::marker { content: \"\\2612\"; }\n"
        "</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'San Francisco\'; font-size:12pt; font-weight:700;\">Copy From</span></p></body></html>"))
                self.tab3_Paste_Text.setHtml(_translate("AutoFolder", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "hr { height: 1px; border-width: 0; }\n"
        "li.unchecked::marker { content: \"\\2610\"; }\n"
        "li.checked::marker { content: \"\\2612\"; }\n"
        "</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'San Francisco\'; font-size:12pt; font-weight:700;\">Paste To</span></p></body></html>"))
                self.tab3_AL_Input_Text_2.setHtml(_translate("AutoFolder", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "hr { height: 1px; border-width: 0; }\n"
        "li.unchecked::marker { content: \"\\2610\"; }\n"
        "li.checked::marker { content: \"\\2612\"; }\n"
        "</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'San Francisco\'; font-size:11pt; font-weight:700;\">Airline</span></p></body></html>"))
                self.tab3_AL_Input_Box_2.setPlaceholderText(_translate("AutoFolder", "code only"))
                self.tab3_FolderNumber_2.setHtml(_translate("AutoFolder", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "hr { height: 1px; border-width: 0; }\n"
        "li.unchecked::marker { content: \"\\2610\"; }\n"
        "li.checked::marker { content: \"\\2612\"; }\n"
        "</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'San Francisco\'; font-size:11pt; font-weight:700;\">Source Folder #</span></p></body></html>"))
                self.tab3_FolderNumberBox_2.setPlaceholderText(_translate("AutoFolder", "number only"))
                self.tab3_AL_Input_Text_3.setHtml(_translate("AutoFolder", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "hr { height: 1px; border-width: 0; }\n"
        "li.unchecked::marker { content: \"\\2610\"; }\n"
        "li.checked::marker { content: \"\\2612\"; }\n"
        "</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'San Francisco\'; font-size:11pt; font-weight:700;\">Location</span></p></body></html>"))
                self.tab3_AL_Input_Text_4.setHtml(_translate("AutoFolder", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "hr { height: 1px; border-width: 0; }\n"
        "li.unchecked::marker { content: \"\\2610\"; }\n"
        "li.checked::marker { content: \"\\2612\"; }\n"
        "</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'San Francisco\'; font-size:11pt; font-weight:700;\">Folder Name</span></p></body></html>"))
                self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("AutoFolder", "Deliverable Folder"))


        def enable_disable_button(self, button):
                selected_button = self.buttonGroup1.checkedButton()
                # Check if the selected button text is not 'Other'
                if selected_button != self.tab1_Other_Button:
                        self.tab1_CSC_Other_Box.setEnabled(False)
                else:
                        self.tab1_CSC_Other_Box.setEnabled(True)
        
        def updateCheckBoxesState(self, sender):
                if sender == self.tab1_RFP_CheckBox:
                        self.tab1_RFP_Precheck_CheckBox.setChecked(False)
                elif sender == self.tab1_RFP_Precheck_CheckBox:
                        self.tab1_RFP_CheckBox.setChecked(False)

        def disableButtonsInGroup1(self, checkbox):
                if checkbox == self.tab1_RFP_CheckBox and checkbox.isChecked():
                        for button in self.buttonGroup1.buttons():
                                if button.text() not in ['PreMP', 'PostMP', 'N/A']:
                                        button.setEnabled(False)
                else:
                        # If the checkbox is unchecked or another checkbox is clicked, enable all buttons
                        for button in self.buttonGroup1.buttons():
                                button.setEnabled(True)
                                self.tab1_NA_Button.setChecked(True)

        def disableButtonsInGroup2(self, checkbox):
                if checkbox == self.tab1_RFP_Precheck_CheckBox and checkbox.isChecked():
                        for button in self.buttonGroup1.buttons():
                                if button.text() not in ['PreMP', 'PostMP', 'N/A']:
                                        button.setEnabled(False)
                else:
                        # If the checkbox is unchecked or another checkbox is clicked, enable all buttons
                        for button in self.buttonGroup1.buttons():
                                button.setEnabled(True)
                                self.tab1_NA_Button.setChecked(True)


        def checkComboBoxes(self):
                CSC_One_Text = self.tab1_comboBox_1st.currentText()
                CSC_Two_Text = self.tab1_comboBox_2nd.currentText()

                if CSC_One_Text and CSC_One_Text == CSC_Two_Text:
                        QtWidgets.QMessageBox.warning(None, "Warning", "Two CSCs cannot be same input, please select a different CSC.")
                        self.tab1_comboBox_2nd.setCurrentIndex(0)  # Set the second combo box to the first option
                        return
                
        def updateComboBox2nd(self):
                # Get the current index of comboBox_1st
                index = self.tab1_comboBox_1st.currentIndex()

                # Enable or disable comboBox_2nd based on the selection of comboBox_1st
                if index != 0:  # Assuming 0 is the index of the default/empty selection
                        self.tab1_comboBox_2nd.setEnabled(True)
                else:
                        self.tab1_comboBox_2nd.setEnabled(False)

        def multiple_CSC_select(self):
                if self.tab1_Multi_CSC_Button.isChecked():
                        self.tab1_comboBox_1st.setEnabled(False)
                        self.tab1_comboBox_2nd.setEnabled(False)
                        self.tab1_comboBox_1st.setCurrentIndex(0)
                        self.tab1_comboBox_2nd.setCurrentIndex(0)
                else:
                        self.tab1_comboBox_1st.setEnabled(True)


        def create_folder(self):
                # Get the text from AL_Input_Box and convert it to uppercase
                al_input_text = self.tab1_AL_Input_Box.text().upper()

                # Get the selected value from the QButtonGroup
                selected_button = self.buttonGroup1.checkedButton()

                # Manually enter folder name in CSC_Other_Box
                CSC_Other_Box_Text = self.tab1_CSC_Other_Box.text()

                # Convert comboBox selections to strings
                CSC_One_Text = self.tab1_comboBox_1st.currentText()
                CSC_Two_Text = self.tab1_comboBox_2nd.currentText()

                Multi_CSC_Text = 'Multi'

                selected_date = self.tab1_dateEdit.date()
                date_text = selected_date.toString("MMMyyyy").upper()

                if selected_button:
                        selected_value = selected_button.text()
                        if selected_value == 'N/A':
                                # Display a warning if 'N/A' is selected without 'RFP'
                                if not self.tab1_RFP_CheckBox.isChecked() and not self.tab1_RFP_Precheck_CheckBox.isChecked():
                                        QtWidgets.QMessageBox.warning(None, "Warning", "Please Select A Valid Project Category.")
                                        return
                else:
                        # Handle the case where no button is checked
                        QtWidgets.QMessageBox.warning(None, "Warning", "Please Select A Valid Project Category.")
                        return

                # Define a dictionary to map selected values to folder name suffixes
                rename_mapping = {
                        "PreMP": "PreMP",
                        "PostMP": "PostMP",
                        "Profitability": "Profitability",
                        "Cycle Change": "CyChange",
                        "Price Action": "Price_Action",
                        "Other": CSC_Other_Box_Text
                }

                # Check if the selected value needs to be renamed based on the mapping
                if selected_value in rename_mapping:
                        selected_value = rename_mapping[selected_value]

                base_path = "M:\\LSGN\\ARHD38-LSGN2\\ease-labor-standards\\000 Costing\\02 Total Costing - OSCAR\\4. Customer"
                sub_folder_path = None

                for existing_folder in os.listdir(base_path):
                        if existing_folder.startswith(al_input_text):
                                sub_folder_path = os.path.join(base_path, existing_folder)
                                break
                        
                if not sub_folder_path:
                        QtWidgets.QMessageBox.warning(None, "Warning", f"No Matching Airline Found for Input {al_input_text}.")
                        return
                
                # Find all folders within the subfolder
                existing_folders = [entry for entry in os.listdir(sub_folder_path) if os.path.isdir(os.path.join(sub_folder_path, entry))]

                # Extract and increment the largest number in the folder names
                largest_number = 0
                for entry in existing_folders:
                        match = re.match(r'^(\d+)\.', entry)  # Match the number at the beginning of the folder name
                        if match:
                                entry_number = int(match.group(1))  # Extract and convert the matched number to an integer
                                largest_number = max(largest_number, entry_number)  # Find the largest number

                # Increment the largest number by 1
                largest_number += 1

                # Use either "RFP" or "RFP_Precheck" based on the selection in buttonGroup1
                rfp_suffix = ""
                if self.tab1_RFP_Precheck_CheckBox.isChecked():
                        rfp_suffix = "RFP_Precheck"
                elif self.tab1_RFP_CheckBox.isChecked():
                        rfp_suffix = "RFP"

                # Check if Multi_CSC_Button is checked
                if self.tab1_Multi_CSC_Button.isChecked():
                        if self.tab1_NA_Button.isChecked() and self.tab1_RFP_CheckBox.isChecked():
                                folder_name = f"{al_input_text}_{Multi_CSC_Text}_{rfp_suffix}_{date_text}"
                        elif self.tab1_NA_Button.isChecked() and self.tab1_RFP_Precheck_CheckBox.isChecked():
                                folder_name = f"{al_input_text}_{Multi_CSC_Text}_{rfp_suffix}_{date_text}"
                        else:
                                folder_name = f"{al_input_text}_{Multi_CSC_Text}_{rfp_suffix}_{selected_value}_{date_text}"
                else:
                        folder_name = f"{al_input_text}_{CSC_One_Text[0:-5]}"
                        if CSC_Two_Text:
                                folder_name += f"_{CSC_Two_Text[0:-5]}"

                        if self.tab1_NA_Button.isChecked() and self.tab1_RFP_CheckBox.isChecked():
                                folder_name += f"_{rfp_suffix}_{date_text}"
                        elif self.tab1_NA_Button.isChecked() and self.tab1_RFP_Precheck_CheckBox.isChecked():
                                folder_name += f"_{rfp_suffix}_{date_text}"
                        else:
                                folder_name += f"_{rfp_suffix}_{selected_value}_{date_text}"

                # Add the incremented number to the folder name
                folder_name = f"{largest_number:02d}. {folder_name}"
                #folder_name = f"{largest_number:02d}. {al_input_text}_{rfp_suffix}_{selected_value}_{date_text}"


                # Check if folder_name is empty
                if not folder_name:
                        QtWidgets.QMessageBox.warning(None, "Warning", "Please Enter A valid AL Code.")
                        return

                destination_path = os.path.join(sub_folder_path, folder_name)

                try:
                        if not os.path.exists(destination_path):
                                os.makedirs(destination_path)

                        source_path = None

                        if self.tab1_TemplatesCheckBox.isChecked():
                        # Copy everything from source path when AL_Input_Box is 'AS'
                                if self.tab1_AL_Input_Box.text().upper() == "AS":
                                        source_path = "M:\\LSGN\\ARHD38-LSGN2\\ease-labor-standards\\000 Costing\\02 Total Costing - OSCAR\\1. OSCAR Templates\\ALASKA_Pre or PostMP_MON_2020"
                                        for item in os.listdir(source_path):
                                                src_item = os.path.join(source_path, item)
                                                dst_item = os.path.join(destination_path, item)
                                                if os.path.isdir(src_item):
                                                        shutil.copytree(src_item, dst_item)
                                                else:
                                                        shutil.copy2(src_item, dst_item)
                                else:
                                        # Copy specific folders based on selected_value
                                        source_path = "M:\\LSGN\\ARHD38-LSGN2\\ease-labor-standards\\000 Costing\\02 Total Costing - OSCAR\\1. OSCAR Templates\\AL_RFP or MP_Pre or Post_CSC_MTH20XX_TEMPLATE"
                                        folders_to_copy = []

                                        if self.tab1_RFP_Precheck_CheckBox.isChecked() or self.tab1_RFP_CheckBox.isChecked():
                                                folders_to_copy = ["!Total Cost Worksheet", "1. System Reports", "2. Documents", "3. Strawman"]
                                        elif selected_value in ["PreMP", "PostMP", "CyChange", "Price_Action"]:
                                                folders_to_copy = ["!Total Cost Worksheet", "1. System Reports", "2. Documents"]
                                        elif selected_value == "Profitability":
                                                folders_to_copy = ["3. Strawman"]

                                        else:
                                                for item in os.listdir(source_path):
                                                        src_item = os.path.join(source_path, item)
                                                        dst_item = os.path.join(destination_path, item)
                                                        if os.path.isdir(src_item):
                                                                shutil.copytree(src_item, dst_item)
                                                        else:
                                                                shutil.copy2(src_item, dst_item)
                                                # Copy specific folders if defined
                                        for folder_name in folders_to_copy:
                                                source_folder_path = os.path.join(source_path, folder_name)
                                                destination_folder_path = os.path.join(destination_path, folder_name)
                                                if os.path.exists(source_folder_path):
                                                        shutil.copytree(source_folder_path, destination_folder_path)

                        QtWidgets.QMessageBox.information(None, "Success", f"Folder Created Successfully at {destination_path}")
                except Exception as e:
                        print("Error:", e)
                        QtWidgets.QMessageBox.critical(None, "Error", f"Failed to Create Folder. Error: {str(e)}")



        def mandatory_info_input(self):
                al_input_text = self.tab1_AL_Input_Box.text()
                # AL_Input_Box is empty or contain only whitespace
                if not al_input_text.strip():
                        self.tab1_buttonBox.button(QtWidgets.QDialogButtonBox.StandardButton.Ok).setEnabled(False)
                else:
                        self.tab1_buttonBox.button(QtWidgets.QDialogButtonBox.StandardButton.Ok).setEnabled(True)


        def enable_copy_button(self, state):
                pass

app = QtWidgets.QApplication([])
AutoFolder = QtWidgets.QMainWindow()

# Add the following lines to enable the minimize button
AutoFolder.setWindowFlag(QtCore.Qt.WindowType.WindowMinimizeButtonHint, True)

# Create an instance of your UI class and set up the UI
ui = Ui_AutoFolder()
ui.setupUi(AutoFolder)

# Show the main window
AutoFolder.show()

# Start the application event loop
sys.exit(app.exec())



'''if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AutoFolder = QtWidgets.QDialog()
    ui = Ui_AutoFolder()
    ui.setupUi(AutoFolder)
    AutoFolder.show()
    sys.exit(app.exec())'''
