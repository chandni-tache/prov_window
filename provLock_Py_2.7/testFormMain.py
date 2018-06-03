# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'testFormMain.ui'
#
# Created: Fri Apr 20 15:22:06 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(666, 596)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.bookMarkCombo = QtGui.QComboBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bookMarkCombo.sizePolicy().hasHeightForWidth())
        self.bookMarkCombo.setSizePolicy(sizePolicy)
        self.bookMarkCombo.setEditable(True)
        #self.bookMarkCombo.setCurrentText("BookMarks")
        self.bookMarkCombo.setObjectName("bookMarkCombo")
        self.horizontalLayout.addWidget(self.bookMarkCombo)
        self.bookMark_label = QtGui.QLabel(self.centralwidget)
        self.bookMark_label.setObjectName("bookMark_label")
        self.horizontalLayout.addWidget(self.bookMark_label)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.Quit = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Quit.sizePolicy().hasHeightForWidth())
        self.Quit.setSizePolicy(sizePolicy)
        self.Quit.setObjectName("Quit")
        self.horizontalLayout.addWidget(self.Quit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.test_console = QtGui.QWidget()
        self.test_console.setObjectName("test_console")
        self.tabWidget.addTab(self.test_console, "")
        self.search_option = QtGui.QWidget()
        self.search_option.setObjectName("search_option")
        self.lineEdit = QtGui.QLineEdit(self.search_option)
        self.lineEdit.setGeometry(QtCore.QRect(0, 0, 771, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setReadOnly(True) # this is used to make linedit readable only.
        self.tabWidget.addTab(self.search_option, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 666, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.bookMark_label.setText(QtGui.QApplication.translate("MainWindow", " BookMarks ", None, QtGui.QApplication.UnicodeUTF8))
        self.Quit.setText(QtGui.QApplication.translate("MainWindow", "Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.test_console), QtGui.QApplication.translate("MainWindow", "Test Console", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit.setText(QtGui.QApplication.translate("MainWindow", "serach here for help", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.search_option), QtGui.QApplication.translate("MainWindow", "Search Option", None, QtGui.QApplication.UnicodeUTF8))

