# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'testFormMain.ui'
#
# Created: Wed May 16 16:35:08 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(652, 596)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/favicon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-color: rgb(255, 0, 0);")
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.centralwidget.setStyleSheet("gridline-color: rgb(170, 0, 0);\n"
"background-color: rgb(170, 0, 0);")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setStyleSheet("border-color: rgb(170, 0, 0);")
        self.tabWidget.setObjectName("tabWidget")
        self.test_console = QtGui.QWidget()
        self.test_console.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.test_console.setObjectName("test_console")
        self.tabWidget.addTab(self.test_console, "")
        self.search_option = QtGui.QWidget()
        self.search_option.setStyleSheet("")
        self.search_option.setObjectName("search_option")
        self.formLayout = QtGui.QFormLayout(self.search_option)
        self.formLayout.setObjectName("formLayout")
        self.lineEdit = QtGui.QLineEdit(self.search_option)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setWeight(75)
        font.setItalic(True)
        font.setBold(True)
        self.lineEdit.setFont(font)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtGui.QFormLayout.SpanningRole, self.lineEdit)
        self.tabWidget.addTab(self.search_option, "")
        self.gridLayout.addWidget(self.tabWidget, 1, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.bookMarkCombo = QtGui.QComboBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bookMarkCombo.sizePolicy().hasHeightForWidth())
        self.bookMarkCombo.setSizePolicy(sizePolicy)
        self.bookMarkCombo.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"border-color: rgb(170, 0, 0);\n"
"color: rgb(170, 0, 0);")
        self.bookMarkCombo.setEditable(True)
        #self.bookMarkCombo.setCurrentText("BookMarks")
        self.bookMarkCombo.setObjectName("bookMarkCombo")
        self.horizontalLayout.addWidget(self.bookMarkCombo)
        self.bookMark_label = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(-1)
        font.setWeight(50)
        font.setItalic(True)
        font.setBold(False)
        self.bookMark_label.setFont(font)
        self.bookMark_label.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: italic 10pt \"MS Shell Dlg 2\";\n"
"selection-color: rgb(170, 0, 0);\n"
"color:#eb3754;\n"
"font-size:25px;")
        self.bookMark_label.setTextFormat(QtCore.Qt.RichText)
        self.bookMark_label.setObjectName("bookMark_label")
        self.horizontalLayout.addWidget(self.bookMark_label)
        self.label_provImage = QtGui.QLabel(self.centralwidget)
        self.label_provImage.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_provImage.sizePolicy().hasHeightForWidth())
        self.label_provImage.setSizePolicy(sizePolicy)
        self.label_provImage.setStyleSheet("background-color: rgb(170, 0, 0);\n"
"gridline-color: rgb(255, 0, 0);\n"
"selection-color: rgb(170, 0, 0);")
        self.label_provImage.setText("")
        self.label_provImage.setPixmap(QtGui.QPixmap(":/icons/Prov_logo_main.png"))
        self.label_provImage.setAlignment(QtCore.Qt.AlignCenter)
        self.label_provImage.setWordWrap(True)
        self.label_provImage.setObjectName("label_provImage")
        self.horizontalLayout.addWidget(self.label_provImage)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.Quit = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Quit.sizePolicy().hasHeightForWidth())
        self.Quit.setSizePolicy(sizePolicy)
        self.Quit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Quit.setObjectName("Quit")
        self.horizontalLayout.addWidget(self.Quit)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 652, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.tabWidget, QtCore.SIGNAL("currentChanged(int)"), self.tabWidget.setCurrentIndex)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.test_console), QtGui.QApplication.translate("MainWindow", "Test Console", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit.setText(QtGui.QApplication.translate("MainWindow", "Look Here For Help", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.search_option), QtGui.QApplication.translate("MainWindow", "Search Option", None, QtGui.QApplication.UnicodeUTF8))
        self.bookMark_label.setText(QtGui.QApplication.translate("MainWindow", " BOOKMARKS ", None, QtGui.QApplication.UnicodeUTF8))
        self.Quit.setText(QtGui.QApplication.translate("MainWindow", "Quit", None, QtGui.QApplication.UnicodeUTF8))

import icons_rc
