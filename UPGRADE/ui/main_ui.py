# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(791, 382)
        MainWindow.setStyleSheet(_fromUtf8("background-color: #0F2D40;\n"
"color: #2ecc71;\n"
"font: 10pt \"MS Shell Dlg 2\";"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setStyleSheet(_fromUtf8("QWidget#centralwidget {\n"
"background: url(:/icons/assets/bg.png) no-repeat center center fixed;\n"
"background-color: #0F2D40;\n"
"color: #2ecc71;\n"
"border-radius: 3px;\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"}"))
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.MainTabWidget = QtGui.QTabWidget(self.centralwidget)
        self.MainTabWidget.setStyleSheet(_fromUtf8(" QTabBar::tab {\n"
"  background-color: #194759;\n"
"  padding: 10px;\n"
"  padding-left: 15px;\n"
"  width: 70%;\n"
"  border: 1px outset;\n"
"  border-color: #0F2D40;\n"
" }\n"
"\n"
" QTabBar::tab:selected {\n"
"   background: #0F2D40;;\n"
" }\n"
"\n"
" QTabBar::pane {\n"
"   background-color: #194759;\n"
" }\n"
"\n"
"QTabWidget::pane {\n"
"    color: rgb(246, 246, 244);\n"
"    margin: 0px,1px,1px,1px;\n"
"    border: 1px ridge;\n"
"    border-color: #0F2D40;\n"
"    background-color: #194759;\n"
"    background-position: center;\n"
"      }"))
        self.MainTabWidget.setObjectName(_fromUtf8("MainTabWidget"))
        self.serversTab = QtGui.QWidget()
        self.serversTab.setObjectName(_fromUtf8("serversTab"))
        self.gridLayout_2 = QtGui.QGridLayout(self.serversTab)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.serversTable = QtGui.QTableWidget(self.serversTab)
        self.serversTable.setStyleSheet(_fromUtf8("QHeaderView::section {\n"
"    background-color: #194759;\n"
"    padding: 2px;\n"
"    color: white;\n"
"}\n"
"\n"
"QTableWidget#serversTable {\n"
"    background-position: center;\n"
"    border: 1px outset;\n"
"    border-color: #0F2D40;\n"
"    border-radius: 2px;\n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 #061014, stop:1 #050C0F);\n"
"}\n"
"\n"
"QTableWidget#serversTable:item:selected {\n"
"background-color: #194759;\n"
"height: 50px;\n"
"color: #2ecc71;\n"
"border: none;\n"
"}"))
        self.serversTable.setFrameShadow(QtGui.QFrame.Plain)
        self.serversTable.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.serversTable.setDragDropOverwriteMode(False)
        self.serversTable.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.serversTable.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.serversTable.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.serversTable.setShowGrid(False)
        self.serversTable.setObjectName(_fromUtf8("serversTable"))
        self.serversTable.setColumnCount(5)
        self.serversTable.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.serversTable.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.serversTable.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.serversTable.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.serversTable.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.serversTable.setHorizontalHeaderItem(4, item)
        self.serversTable.horizontalHeader().setCascadingSectionResizes(True)
        self.serversTable.horizontalHeader().setDefaultSectionSize(100)
        self.serversTable.horizontalHeader().setSortIndicatorShown(False)
        self.serversTable.horizontalHeader().setStretchLastSection(True)
        self.serversTable.verticalHeader().setVisible(False)
        self.gridLayout_2.addWidget(self.serversTable, 0, 0, 1, 1)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/server.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.MainTabWidget.addTab(self.serversTab, icon, _fromUtf8(""))
        self.logsTab = QtGui.QWidget()
        self.logsTab.setObjectName(_fromUtf8("logsTab"))
        self.gridLayout_3 = QtGui.QGridLayout(self.logsTab)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.textEdit = QtGui.QTextEdit(self.logsTab)
        self.textEdit.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 #061014, stop:1 #050C0F);\n"
"background-position: center;\n"
"border: 1px ridge;\n"
"border-color: #0F2D40;\n"
"border-radius: 2px;"))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.gridLayout_3.addWidget(self.textEdit, 0, 0, 1, 1)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/log.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.MainTabWidget.addTab(self.logsTab, icon1, _fromUtf8(""))
        self.gridLayout.addWidget(self.MainTabWidget, 1, 0, 1, 3)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.creditLabel = QtGui.QLabel(self.centralwidget)
        self.creditLabel.setStyleSheet(_fromUtf8("padding: 5px;"))
        self.creditLabel.setObjectName(_fromUtf8("creditLabel"))
        self.horizontalLayout_5.addWidget(self.creditLabel)
        self.versionLabel = QtGui.QLabel(self.centralwidget)
        self.versionLabel.setStyleSheet(_fromUtf8("padding: 5px;"))
        self.versionLabel.setObjectName(_fromUtf8("versionLabel"))
        self.horizontalLayout_5.addWidget(self.versionLabel)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.gridLayout.addLayout(self.horizontalLayout_5, 2, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.clientStatusLabel = QtGui.QLabel(self.centralwidget)
        self.clientStatusLabel.setStyleSheet(_fromUtf8("padding: 5px;"))
        self.clientStatusLabel.setObjectName(_fromUtf8("clientStatusLabel"))
        self.horizontalLayout_2.addWidget(self.clientStatusLabel)
        self.statusLabel = QtGui.QLabel(self.centralwidget)
        self.statusLabel.setStyleSheet(_fromUtf8("padding: 5px;\n"
"color: red;"))
        self.statusLabel.setObjectName(_fromUtf8("statusLabel"))
        self.horizontalLayout_2.addWidget(self.statusLabel)
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 1, 1, 1)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.serversOnlineStatus = QtGui.QLabel(self.centralwidget)
        self.serversOnlineStatus.setStyleSheet(_fromUtf8("padding: 5px;"))
        self.serversOnlineStatus.setObjectName(_fromUtf8("serversOnlineStatus"))
        self.horizontalLayout_4.addWidget(self.serversOnlineStatus)
        self.onlineStatus = QtGui.QLabel(self.centralwidget)
        self.onlineStatus.setStyleSheet(_fromUtf8("padding: 5px;"))
        self.onlineStatus.setObjectName(_fromUtf8("onlineStatus"))
        self.horizontalLayout_4.addWidget(self.onlineStatus)
        self.gridLayout.addLayout(self.horizontalLayout_4, 2, 2, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.startListenButton = QtGui.QPushButton(self.centralwidget)
        self.startListenButton.setMinimumSize(QtCore.QSize(32, 32))
        self.startListenButton.setMaximumSize(QtCore.QSize(32, 32))
        self.startListenButton.setStyleSheet(_fromUtf8("QPushButton#startListenButton {\n"
"            background: #194759;\n"
"            border: 1px outset;\n"
"            border-color: #0F2D40;\n"
"            text-decoration: none;\n"
"            background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 #194759, stop:1 #225E75);\n"
"            }\n"
"\n"
"QPushButton#startListenButton:pressed {\n"
"            background: #194759;\n"
"            border: 1px outset;\n"
"            border-color: #0F2D40;\n"
"            background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 #112F3B, stop:1 #1B4C5E);\n"
"            }"))
        self.startListenButton.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/start.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.startListenButton.setIcon(icon2)
        self.startListenButton.setIconSize(QtCore.QSize(22, 22))
        self.startListenButton.setObjectName(_fromUtf8("startListenButton"))
        self.horizontalLayout.addWidget(self.startListenButton)
        self.StopListenButton = QtGui.QPushButton(self.centralwidget)
        self.StopListenButton.setMinimumSize(QtCore.QSize(32, 32))
        self.StopListenButton.setMaximumSize(QtCore.QSize(32, 32))
        self.StopListenButton.setStyleSheet(_fromUtf8("QPushButton#StopListenButton {\n"
"            background: #194759;\n"
"            border: 1px outset;\n"
"            border-color: #0F2D40;\n"
"            text-decoration: none;\n"
"            background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 #194759, stop:1 #225E75);\n"
"            }\n"
"\n"
"QPushButton#StopListenButton:pressed {\n"
"            background: #194759;\n"
"            border: 1px outset;\n"
"            border-color: #0F2D40;\n"
"            background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 #112F3B, stop:1 #1B4C5E);\n"
"            }"))
        self.StopListenButton.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/stop.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.StopListenButton.setIcon(icon3)
        self.StopListenButton.setIconSize(QtCore.QSize(20, 20))
        self.StopListenButton.setObjectName(_fromUtf8("StopListenButton"))
        self.horizontalLayout.addWidget(self.StopListenButton)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 791, 24))
        self.menubar.setStyleSheet(_fromUtf8("QMenuBar {\n"
"            background-color: #0C2230;\n"
"            color: rgb(255,255,255);\n"
"            border: 1px solid #000;\n"
"        }\n"
"\n"
"        QMenuBar::item {\n"
"            background-color: #0C2230;\n"
"            color: rgb(255,255,255);\n"
"        }\n"
"\n"
"        QMenuBar::item::selected {\n"
"            background-color: #0F2D40;\n"
"        }\n"
"\n"
"        QMenu {\n"
"            background-color: #0C2230;\n"
"            color: rgb(255,255,255);\n"
"            border: 1px solid #000;           \n"
"        }\n"
"\n"
"        QMenu::item::selected {\n"
"            background-color: #0F2D40;\n"
"        }"))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuClient = QtGui.QMenu(self.menubar)
        self.menuClient.setObjectName(_fromUtf8("menuClient"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionStartListen_for_connections = QtGui.QAction(MainWindow)
        self.actionStartListen_for_connections.setObjectName(_fromUtf8("actionStartListen_for_connections"))
        self.actionStopListen_for_connections = QtGui.QAction(MainWindow)
        self.actionStopListen_for_connections.setObjectName(_fromUtf8("actionStopListen_for_connections"))
        self.actionClient_Configuration = QtGui.QAction(MainWindow)
        self.actionClient_Configuration.setObjectName(_fromUtf8("actionClient_Configuration"))
        self.menuClient.addAction(self.actionStartListen_for_connections)
        self.menuClient.addAction(self.actionStopListen_for_connections)
        self.menuClient.addSeparator()
        self.menuClient.addAction(self.actionClient_Configuration)
        self.menubar.addAction(self.menuClient.menuAction())

        self.retranslateUi(MainWindow)
        self.MainTabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Mirakuru Client", None))
        self.serversTable.setSortingEnabled(True)
        item = self.serversTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Ip Address", None))
        item = self.serversTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Location", None))
        item = self.serversTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Socket", None))
        item = self.serversTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Protection", None))
        item = self.serversTable.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "OS", None))
        self.MainTabWidget.setTabText(self.MainTabWidget.indexOf(self.serversTab), _translate("MainWindow", "Servers", None))
        self.MainTabWidget.setTabText(self.MainTabWidget.indexOf(self.logsTab), _translate("MainWindow", "Logs", None))
        self.creditLabel.setText(_translate("MainWindow", "Coded By Uri Patton (c) 2015", None))
        self.versionLabel.setText(_translate("MainWindow", "Version 2.0", None))
        self.clientStatusLabel.setText(_translate("MainWindow", "Client Status: ", None))
        self.statusLabel.setText(_translate("MainWindow", "Not Listening", None))
        self.serversOnlineStatus.setText(_translate("MainWindow", "Servers Online: ", None))
        self.onlineStatus.setText(_translate("MainWindow", "0", None))
        self.menuClient.setTitle(_translate("MainWindow", "Client", None))
        self.actionStartListen_for_connections.setText(_translate("MainWindow", "Start Listening", None))
        self.actionStopListen_for_connections.setText(_translate("MainWindow", "Stop Listening", None))
        self.actionClient_Configuration.setText(_translate("MainWindow", "Client Configuration", None))

import res
