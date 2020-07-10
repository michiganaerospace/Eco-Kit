# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'weather_ui_2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1101, 865)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        MainWindow.setBaseSize(QtCore.QSize(831, 779))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("1024px-Weather-few-clouds.svg.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pic_label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pic_label.sizePolicy().hasHeightForWidth())
        self.pic_label.setSizePolicy(sizePolicy)
        self.pic_label.setMinimumSize(QtCore.QSize(781, 521))
        self.pic_label.setMaximumSize(QtCore.QSize(99999, 999999))
        self.pic_label.setFrameShape(QtWidgets.QFrame.Box)
        self.pic_label.setText("")
        self.pic_label.setTextFormat(QtCore.Qt.PlainText)
        self.pic_label.setScaledContents(True)
        self.pic_label.setObjectName("pic_label")
        self.verticalLayout_3.addWidget(self.pic_label)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.dev_combo = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dev_combo.sizePolicy().hasHeightForWidth())
        self.dev_combo.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dev_combo.setFont(font)
        self.dev_combo.setObjectName("dev_combo")
        self.dev_combo.addItem("")
        self.dev_combo.addItem("")
        self.dev_combo.addItem("")
        self.dev_combo.addItem("")
        self.dev_combo.addItem("")
        self.dev_combo.addItem("")
        self.dev_combo.addItem("")
        self.horizontalLayout_3.addWidget(self.dev_combo)
        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 3)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.date_start = QtWidgets.QDateTimeEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.date_start.sizePolicy().hasHeightForWidth())
        self.date_start.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.date_start.setFont(font)
        self.date_start.setDateTime(QtCore.QDateTime(QtCore.QDate(2019, 8, 6), QtCore.QTime(0, 0, 0)))
        self.date_start.setTime(QtCore.QTime(0, 0, 0))
        self.date_start.setCurrentSection(QtWidgets.QDateTimeEdit.MonthSection)
        self.date_start.setCalendarPopup(False)
        self.date_start.setObjectName("date_start")
        self.horizontalLayout_2.addWidget(self.date_start)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.date_end = QtWidgets.QDateTimeEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.date_end.sizePolicy().hasHeightForWidth())
        self.date_end.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.date_end.setFont(font)
        self.date_end.setDateTime(QtCore.QDateTime(QtCore.QDate(2019, 8, 6), QtCore.QTime(23, 59, 59)))
        self.date_end.setTime(QtCore.QTime(23, 59, 59))
        self.date_end.setCurrentSection(QtWidgets.QDateTimeEdit.DaySection)
        self.date_end.setObjectName("date_end")
        self.horizontalLayout_2.addWidget(self.date_end)
        self.horizontalLayout_2.setStretch(0, 4)
        self.horizontalLayout_2.setStretch(1, 5)
        self.horizontalLayout_2.setStretch(2, 1)
        self.horizontalLayout_2.setStretch(3, 5)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.gridLayout_2.setSpacing(3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.buttonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.radioButton)
        self.gridLayout_2.addWidget(self.radioButton, 0, 2, 1, 1)
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.buttonGroup.addButton(self.radioButton_2)
        self.gridLayout_2.addWidget(self.radioButton_2, 2, 2, 1, 1)
        self.radioButton_7 = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.radioButton_7.setFont(font)
        self.radioButton_7.setObjectName("radioButton_7")
        self.buttonGroup.addButton(self.radioButton_7)
        self.gridLayout_2.addWidget(self.radioButton_7, 0, 1, 1, 1)
        self.radioButton_3 = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setObjectName("radioButton_3")
        self.buttonGroup.addButton(self.radioButton_3)
        self.gridLayout_2.addWidget(self.radioButton_3, 3, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)
        self.radioButton_4 = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.radioButton_4.setFont(font)
        self.radioButton_4.setObjectName("radioButton_4")
        self.buttonGroup.addButton(self.radioButton_4)
        self.gridLayout_2.addWidget(self.radioButton_4, 4, 1, 1, 1)
        self.radioButton_5 = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.radioButton_5.setFont(font)
        self.radioButton_5.setObjectName("radioButton_5")
        self.buttonGroup.addButton(self.radioButton_5)
        self.gridLayout_2.addWidget(self.radioButton_5, 3, 1, 1, 1)
        self.radioButton_6 = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.radioButton_6.setFont(font)
        self.radioButton_6.setObjectName("radioButton_6")
        self.buttonGroup.addButton(self.radioButton_6)
        self.gridLayout_2.addWidget(self.radioButton_6, 2, 1, 1, 1)
        self.radioButton_8 = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.radioButton_8.setFont(font)
        self.radioButton_8.setObjectName("radioButton_8")
        self.buttonGroup.addButton(self.radioButton_8)
        self.gridLayout_2.addWidget(self.radioButton_8, 4, 2, 1, 1)
        self.gridLayout_2.setColumnStretch(0, 2)
        self.gridLayout_2.setColumnStretch(1, 3)
        self.gridLayout_2.setColumnStretch(2, 3)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout.addWidget(self.line_3)
        self.refreshbutton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.refreshbutton.sizePolicy().hasHeightForWidth())
        self.refreshbutton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.refreshbutton.setFont(font)
        self.refreshbutton.setObjectName("refreshbutton")
        self.verticalLayout.addWidget(self.refreshbutton)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.MAC_LOGO = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MAC_LOGO.sizePolicy().hasHeightForWidth())
        self.MAC_LOGO.setSizePolicy(sizePolicy)
        self.MAC_LOGO.setFrameShape(QtWidgets.QFrame.Panel)
        self.MAC_LOGO.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.MAC_LOGO.setLineWidth(3)
        self.MAC_LOGO.setText("")
        self.MAC_LOGO.setScaledContents(True)
        self.MAC_LOGO.setObjectName("MAC_LOGO")
        self.verticalLayout_2.addWidget(self.MAC_LOGO)
        self.verticalLayout_2.setStretch(0, 3)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        self.horizontalLayout_4.setStretch(0, 6)
        self.horizontalLayout_4.setStretch(1, 2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.verticalLayout_3.setStretch(0, 12)
        self.verticalLayout_3.setStretch(1, 9)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1101, 26))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        self.menuOption = QtWidgets.QMenu(self.menuBar)
        self.menuOption.setObjectName("menuOption")
        self.menuGraph_Resolution = QtWidgets.QMenu(self.menuOption)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.menuGraph_Resolution.setFont(font)
        self.menuGraph_Resolution.setObjectName("menuGraph_Resolution")
        MainWindow.setMenuBar(self.menuBar)
        self.Save_Image = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.Save_Image.setFont(font)
        self.Save_Image.setObjectName("Save_Image")
        self.action200_dpi = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.action200_dpi.setFont(font)
        self.action200_dpi.setObjectName("action200_dpi")
        self.action300_dpi = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.action300_dpi.setFont(font)
        self.action300_dpi.setObjectName("action300_dpi")
        self.action400_dpi = QtWidgets.QAction(MainWindow)
        self.action400_dpi.setCheckable(False)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.action400_dpi.setFont(font)
        self.action400_dpi.setObjectName("action400_dpi")
        self.action600_dpi = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.action600_dpi.setFont(font)
        self.action600_dpi.setObjectName("action600_dpi")
        self.current_dpi = QtWidgets.QAction(MainWindow)
        self.current_dpi.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.current_dpi.setFont(font)
        self.current_dpi.setObjectName("current_dpi")
        self.menuFile.addAction(self.Save_Image)
        self.menuGraph_Resolution.addAction(self.action200_dpi)
        self.menuGraph_Resolution.addAction(self.action300_dpi)
        self.menuGraph_Resolution.addAction(self.action400_dpi)
        self.menuGraph_Resolution.addAction(self.action600_dpi)
        self.menuGraph_Resolution.addSeparator()
        self.menuGraph_Resolution.addAction(self.current_dpi)
        self.menuOption.addAction(self.menuGraph_Resolution.menuAction())
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuOption.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Weather Monitor"))
        self.label.setText(_translate("MainWindow", "Device"))
        self.dev_combo.setCurrentText(_translate("MainWindow", "2"))
        self.dev_combo.setItemText(0, _translate("MainWindow", "2"))
        self.dev_combo.setItemText(1, _translate("MainWindow", "5"))
        self.dev_combo.setItemText(2, _translate("MainWindow", "8"))
        self.dev_combo.setItemText(3, _translate("MainWindow", "10"))
        self.dev_combo.setItemText(4, _translate("MainWindow", "11"))
        self.dev_combo.setItemText(5, _translate("MainWindow", "12"))
        self.dev_combo.setItemText(6, _translate("MainWindow", "13"))
        self.label_2.setText(_translate("MainWindow", "Date Range"))
        self.label_3.setText(_translate("MainWindow", "to"))
        self.radioButton.setText(_translate("MainWindow", "Wind Direction"))
        self.radioButton_2.setText(_translate("MainWindow", "Pressure"))
        self.radioButton_7.setText(_translate("MainWindow", "Temperature"))
        self.radioButton_3.setText(_translate("MainWindow", "Humidity"))
        self.label_4.setText(_translate("MainWindow", "Parameter"))
        self.radioButton_4.setText(_translate("MainWindow", "Soil Temperature"))
        self.radioButton_5.setText(_translate("MainWindow", "Soil Moisture"))
        self.radioButton_6.setText(_translate("MainWindow", "Wind Speed"))
        self.radioButton_8.setText(_translate("MainWindow", "Voltage"))
        self.refreshbutton.setText(_translate("MainWindow", "Refresh Data"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuOption.setTitle(_translate("MainWindow", "Option"))
        self.menuGraph_Resolution.setTitle(_translate("MainWindow", "Graph Resolution"))
        self.Save_Image.setText(_translate("MainWindow", "Save Image"))
        self.action200_dpi.setText(_translate("MainWindow", "200 dpi"))
        self.action300_dpi.setText(_translate("MainWindow", "300 dpi"))
        self.action400_dpi.setText(_translate("MainWindow", "400 dpi"))
        self.action600_dpi.setText(_translate("MainWindow", "600 dpi"))
        self.current_dpi.setText(_translate("MainWindow", "Default is 200 dpi"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

