# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created: Thu Oct 29 14:09:06 2015
#      by: PyQt4 UI code generator 4.11.2
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.setWindowModality(QtCore.Qt.NonModal)
        Form.resize(1006, 672)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Shell Dlg 2"))
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        Form.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/assets/icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet(_fromUtf8("background-color: #0F2D40;\n"
"color: #2ecc71;\n"
"border-radius: 3px;\n"
"font: 10pt \"MS Shell Dlg 2\";"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.splitter_7 = QtGui.QSplitter(Form)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Shell Dlg 2"))
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.splitter_7.setFont(font)
        self.splitter_7.setOrientation(QtCore.Qt.Vertical)
        self.splitter_7.setObjectName(_fromUtf8("splitter_7"))
        self.splitter_5 = QtGui.QSplitter(self.splitter_7)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Shell Dlg 2"))
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.splitter_5.setFont(font)
        self.splitter_5.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_5.setObjectName(_fromUtf8("splitter_5"))
        self.splitter_4 = QtGui.QSplitter(self.splitter_5)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Shell Dlg 2"))
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.splitter_4.setFont(font)
        self.splitter_4.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_4.setObjectName(_fromUtf8("splitter_4"))
        self.tabWidget = QtGui.QTabWidget(self.splitter_4)
        self.tabWidget.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Shell Dlg 2"))
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.tabWidget.setFont(font)
        self.tabWidget.setFocusPolicy(QtCore.Qt.TabFocus)
        self.tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet(_fromUtf8("\n"
"\n"
"\n"
"\n"
" QTabBar::tab {\n"
"  background-color: #194759;\n"
"  color: white;\n"
"  padding: 10px;\n"
"  padding-left: 15px;\n"
"  width: 30%;\n"
"  border: 1px outset;\n"
"  border-color: #0F2D40;\n"
" }\n"
"\n"
" QTabBar::tab:selected {\n"
"   background: #0F2D40;;\n"
" }\n"
"\n"
" QTabBar::pane {\n"
"   background-color: rgb(28, 29, 33);\n"
" }\n"
"\n"
"QTabWidget::pane {\n"
"    color: rgb(246, 246, 244);\n"
"    margin: 0px,1px,1px,1px;\n"
"    border: 1px ridge;\n"
"    border-color: #0F2D40;\n"
"    background-color: rgb(28, 29, 33);\n"
"    background-position: center;\n"
"      }"))
        self.tabWidget.setTabPosition(QtGui.QTabWidget.North)
        self.tabWidget.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabWidget.setIconSize(QtCore.QSize(32, 32))
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.shellTab = QtGui.QWidget()
        self.shellTab.setObjectName(_fromUtf8("shellTab"))
        self.gridLayout = QtGui.QGridLayout(self.shellTab)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.shellLayout = QtGui.QVBoxLayout()
        self.shellLayout.setObjectName(_fromUtf8("shellLayout"))
        self.gridLayout.addLayout(self.shellLayout, 0, 0, 1, 1)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/assets/terminal.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.shellTab, icon1, _fromUtf8(""))
        self.remotepythonTab = QtGui.QWidget()
        self.remotepythonTab.setObjectName(_fromUtf8("remotepythonTab"))
        self.gridLayout_2 = QtGui.QGridLayout(self.remotepythonTab)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.executeButton = QtGui.QPushButton(self.remotepythonTab)
        self.executeButton.setMinimumSize(QtCore.QSize(32, 32))
        self.executeButton.setMaximumSize(QtCore.QSize(32, 32))
        self.executeButton.setStyleSheet(_fromUtf8("QPushButton#executeButton {\n"
"            background: #194759;\n"
"            border: 1px outset;\n"
"            border-color: #0F2D40;\n"
"            text-decoration: none;\n"
"            background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 #194759, stop:1 #225E75);\n"
"            }\n"
"\n"
"QPushButton#executeButton:pressed {\n"
"            background: #194759;\n"
"            border: 1px outset;\n"
"            border-color: #0F2D40;\n"
"            background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 #112F3B, stop:1 #1B4C5E);\n"
"            }"))
        self.executeButton.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/assets/execute.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.executeButton.setIcon(icon2)
        self.executeButton.setIconSize(QtCore.QSize(18, 18))
        self.executeButton.setObjectName(_fromUtf8("executeButton"))
        self.horizontalLayout_3.addWidget(self.executeButton)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
        self.splitter = QtGui.QSplitter(self.remotepythonTab)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.layoutWidget = QtGui.QWidget(self.splitter)
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.remoteScriptLabel = QtGui.QLabel(self.layoutWidget)
        self.remoteScriptLabel.setMinimumSize(QtCore.QSize(0, 14))
        self.remoteScriptLabel.setMaximumSize(QtCore.QSize(16777215, 14))
        self.remoteScriptLabel.setStyleSheet(_fromUtf8("background-color:#194759;\n"
"border-radius: none;"))
        self.remoteScriptLabel.setTextFormat(QtCore.Qt.AutoText)
        self.remoteScriptLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.remoteScriptLabel.setObjectName(_fromUtf8("remoteScriptLabel"))
        self.verticalLayout.addWidget(self.remoteScriptLabel)
        self.LeditorLayout = QtGui.QVBoxLayout()
        self.LeditorLayout.setObjectName(_fromUtf8("LeditorLayout"))
        self.verticalLayout.addLayout(self.LeditorLayout)
        self.layoutWidget1 = QtGui.QWidget(self.splitter)
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.localScriptLabel = QtGui.QLabel(self.layoutWidget1)
        self.localScriptLabel.setMinimumSize(QtCore.QSize(0, 14))
        self.localScriptLabel.setMaximumSize(QtCore.QSize(16777215, 14))
        self.localScriptLabel.setStyleSheet(_fromUtf8("background-color:#194759;\n"
"border-radius: none;"))
        self.localScriptLabel.setTextFormat(QtCore.Qt.AutoText)
        self.localScriptLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.localScriptLabel.setObjectName(_fromUtf8("localScriptLabel"))
        self.verticalLayout_2.addWidget(self.localScriptLabel)
        self.ReditorLayout = QtGui.QVBoxLayout()
        self.ReditorLayout.setObjectName(_fromUtf8("ReditorLayout"))
        self.verticalLayout_2.addLayout(self.ReditorLayout)
        self.gridLayout_2.addWidget(self.splitter, 1, 0, 1, 1)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/assets/python.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.remotepythonTab, icon3, _fromUtf8(""))
        self.explorerTab = QtGui.QWidget()
        self.explorerTab.setObjectName(_fromUtf8("explorerTab"))
        self.gridLayout_6 = QtGui.QGridLayout(self.explorerTab)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.explorerDrivesDrop = QtGui.QComboBox(self.explorerTab)
        self.explorerDrivesDrop.setMinimumSize(QtCore.QSize(0, 32))
        self.explorerDrivesDrop.setBaseSize(QtCore.QSize(0, 0))
        self.explorerDrivesDrop.setStyleSheet(_fromUtf8("height: 15px;\n"
"color: rgb(97, 163, 94);\n"
"border: 1px outset;\n"
"border-color: #0F2D40;\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 #194759, stop:1 #225E75);"))
        self.explorerDrivesDrop.setObjectName(_fromUtf8("explorerDrivesDrop"))
        self.gridLayout_6.addWidget(self.explorerDrivesDrop, 0, 0, 1, 1)
        self.refreshexplorerButton = QtGui.QPushButton(self.explorerTab)
        self.refreshexplorerButton.setMinimumSize(QtCore.QSize(32, 32))
        self.refreshexplorerButton.setMaximumSize(QtCore.QSize(32, 32))
        self.refreshexplorerButton.setStyleSheet(_fromUtf8("QPushButton#refreshexplorerButton {\n"
"            background: #194759;\n"
"            border: 1px outset;\n"
"            border-color: #0F2D40;\n"
"            text-decoration: none;\n"
"            background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 #194759, stop:1 #225E75);\n"
"            }\n"
"\n"
"QPushButton#refreshexplorerButton:pressed {\n"
"            background: #194759;\n"
"            border: 1px outset;\n"
"            border-color: #0F2D40;\n"
"            background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 #112F3B, stop:1 #1B4C5E);\n"
"            }"))
        self.refreshexplorerButton.setText(_fromUtf8(""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/assets/refresh.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.refreshexplorerButton.setIcon(icon4)
        self.refreshexplorerButton.setIconSize(QtCore.QSize(20, 20))
        self.refreshexplorerButton.setObjectName(_fromUtf8("refreshexplorerButton"))
        self.gridLayout_6.addWidget(self.refreshexplorerButton, 0, 1, 1, 1)
        self.upexplorerButton = QtGui.QPushButton(self.explorerTab)
        self.upexplorerButton.setMinimumSize(QtCore.QSize(32, 32))
        self.upexplorerButton.setMaximumSize(QtCore.QSize(32, 32))
        self.upexplorerButton.setStyleSheet(_fromUtf8("QPushButton#upexplorerButton {\n"
"            background: #194759;\n"
"            border: 1px outset;\n"
"            border-color: #0F2D40;\n"
"            text-decoration: none;\n"
"            background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 #194759, stop:1 #225E75);\n"
"            }\n"
"\n"
"QPushButton#upexplorerButton:pressed {\n"
"            background: #194759;\n"
"            border: 1px outset;\n"
"            border-color: #0F2D40;\n"
"            background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 #112F3B, stop:1 #1B4C5E);\n"
"            }"))
        self.upexplorerButton.setText(_fromUtf8(""))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/assets/up_folder.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.upexplorerButton.setIcon(icon5)
        self.upexplorerButton.setIconSize(QtCore.QSize(20, 20))
        self.upexplorerButton.setObjectName(_fromUtf8("upexplorerButton"))
        self.gridLayout_6.addWidget(self.upexplorerButton, 0, 2, 1, 1)
        self.mkfileexplorerButton = QtGui.QPushButton(self.explorerTab)
        self.mkfileexplorerButton.setMinimumSize(QtCore.QSize(32, 32))
        self.mkfileexplorerButton.setMaximumSize(QtCore.QSize(32, 32))
        self.mkfileexplorerButton.setStyleSheet(_fromUtf8("QPushButton#mkfileexplorerButton {\n"
"            background: #194759;\n"
"            border: 1px outset;\n"
"            border-color: #0F2D40;\n"
"            text-decoration: none;\n"
"            background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 #194759, stop:1 #225E75);\n"
"            }\n"
"\n"
"QPushButton#mkfileexplorerButton:pressed {\n"
"            background: #194759;\n"
"            border: 1px outset;\n"
"            border-color: #0F2D40;\n"
"            background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 #112F3B, stop:1 #1B4C5E);\n"
"            }"))
        self.mkfileexplorerButton.setText(_fromUtf8(""))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/assets/new_file.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mkfileexplorerButton.setIcon(icon6)
        self.mkfileexplorerButton.setIconSize(QtCore.QSize(20, 20))
        self.mkfileexplorerButton.setObjectName(_fromUtf8("mkfileexplorerButton"))
        self.gridLayout_6.addWidget(self.mkfileexplorerButton, 0, 3, 1, 1)
        self.mkdirexplorerButton = QtGui.QPushButton(self.explorerTab)
        self.mkdirexplorerButton.setMinimumSize(QtCore.QSize(32, 32))
        self.mkdirexplorerButton.setMaximumSize(QtCore.QSize(32, 32))
        self.mkdirexplorerButton.setStyleSheet(_fromUtf8("QPushButton#mkdirexplorerButton {\n"
"            background: #194759;\n"
"            border: 1px outset;\n"
"            border-color: #0F2D40;\n"
"            text-decoration: none;\n"
"            background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 #194759, stop:1 #225E75);\n"
"            }\n"
"\n"
"QPushButton#mkdirexplorerButton:pressed {\n"
"            background: #194759;\n"
"            border: 1px outset;\n"
"            border-color: #0F2D40;\n"
"            background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 #112F3B, stop:1 #1B4C5E);\n"
"            }"))
        self.mkdirexplorerButton.setText(_fromUtf8(""))
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/assets/new_folder.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mkdirexplorerButton.setIcon(icon7)
        self.mkdirexplorerButton.setIconSize(QtCore.QSize(20, 20))
        self.mkdirexplorerButton.setObjectName(_fromUtf8("mkdirexplorerButton"))
        self.gridLayout_6.addWidget(self.mkdirexplorerButton, 0, 4, 1, 1)
        self.removeexplorerButton = QtGui.QPushButton(self.explorerTab)
        self.removeexplorerButton.setMinimumSize(QtCore.QSize(32, 32))
        self.removeexplorerButton.setMaximumSize(QtCore.QSize(32, 32))
        self.removeexplorerButton.setStyleSheet(_fromUtf8("QPushButton#removeexplorerButton {\n"
"            background: #194759;\n"
"            border: 1px outset;\n"
"            border-color: #0F2D40;\n"
"            text-decoration: none;\n"
"            background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 #194759, stop:1 #225E75);\n"
"            }\n"
"\n"
"QPushButton#removeexplorerButton:pressed {\n"
"            background: #194759;\n"
"            border: 1px outset;\n"
"            border-color: #0F2D40;\n"
"            background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 #112F3B, stop:1 #1B4C5E);\n"
"            }"))
        self.removeexplorerButton.setText(_fromUtf8(""))
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/assets/remove.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.removeexplorerButton.setIcon(icon8)
        self.removeexplorerButton.setIconSize(QtCore.QSize(20, 20))
        self.removeexplorerButton.setObjectName(_fromUtf8("removeexplorerButton"))
        self.gridLayout_6.addWidget(self.removeexplorerButton, 0, 5, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(220, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem1, 0, 6, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_3 = QtGui.QLabel(self.explorerTab)
        self.label_3.setStyleSheet(_fromUtf8("color: rgb(155, 89, 182)"))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_2.addWidget(self.label_3)
        self.label_2 = QtGui.QLabel(self.explorerTab)
        self.label_2.setStyleSheet(_fromUtf8("color: rgb(0, 255, 255)"))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.label_4 = QtGui.QLabel(self.explorerTab)
        self.label_4.setStyleSheet(_fromUtf8("color: rgb(201, 101, 101)"))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_2.addWidget(self.label_4)
        self.label_5 = QtGui.QLabel(self.explorerTab)
        self.label_5.setStyleSheet(_fromUtf8("color: rgb(235, 235, 235)"))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_2.addWidget(self.label_5)
        self.label_6 = QtGui.QLabel(self.explorerTab)
        self.label_6.setStyleSheet(_fromUtf8("color: #2ecc71;"))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_2.addWidget(self.label_6)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.explorerContentLabel = QtGui.QLabel(self.explorerTab)
        self.explorerContentLabel.setText(_fromUtf8(""))
        self.explorerContentLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.explorerContentLabel.setObjectName(_fromUtf8("explorerContentLabel"))
        self.horizontalLayout_2.addWidget(self.explorerContentLabel)
        self.gridLayout_6.addLayout(self.horizontalLayout_2, 3, 0, 1, 7)
        self.explorerTable = QtGui.QTableWidget(self.explorerTab)
        self.explorerTable.setStyleSheet(_fromUtf8("QHeaderView::section {\n"
"    background-color: #194759;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QTableWidget#explorerTable {\n"
"    background-position: center;\n"
"    border: 1px outset;\n"
"    border-color: #0F2D40;\n"
"    border-radius: 2px;\n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 #061014, stop:1 #050C0F);\n"
"}\n"
"\n"
"QTableWidget#explorerTable:item:selected {\n"
"background-color: #194759;\n"
"height: 50px;\n"
"color: #2ecc71;\n"
"border: none;\n"
"}"))
        self.explorerTable.setFrameShape(QtGui.QFrame.StyledPanel)
        self.explorerTable.setFrameShadow(QtGui.QFrame.Plain)
        self.explorerTable.setLineWidth(1)
        self.explorerTable.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.explorerTable.setProperty("showDropIndicator", False)
        self.explorerTable.setDragDropOverwriteMode(False)
        self.explorerTable.setAlternatingRowColors(False)
        self.explorerTable.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.explorerTable.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.explorerTable.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.explorerTable.setShowGrid(False)
        self.explorerTable.setGridStyle(QtCore.Qt.DotLine)
        self.explorerTable.setWordWrap(False)
        self.explorerTable.setCornerButtonEnabled(True)
        self.explorerTable.setObjectName(_fromUtf8("explorerTable"))
        self.explorerTable.setColumnCount(4)
        self.explorerTable.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.explorerTable.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.explorerTable.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.explorerTable.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.explorerTable.setHorizontalHeaderItem(3, item)
        self.explorerTable.horizontalHeader().setVisible(False)
        self.explorerTable.horizontalHeader().setCascadingSectionResizes(True)
        self.explorerTable.horizontalHeader().setDefaultSectionSize(50)
        self.explorerTable.horizontalHeader().setHighlightSections(True)
        self.explorerTable.horizontalHeader().setSortIndicatorShown(False)
        self.explorerTable.horizontalHeader().setStretchLastSection(False)
        self.explorerTable.verticalHeader().setVisible(False)
        self.explorerTable.verticalHeader().setCascadingSectionResizes(False)
        self.gridLayout_6.addWidget(self.explorerTable, 2, 0, 1, 7)
        self.explorerPathEntry = QtGui.QLineEdit(self.explorerTab)
        self.explorerPathEntry.setMinimumSize(QtCore.QSize(0, 28))
        self.explorerPathEntry.setStyleSheet(_fromUtf8("border: 1px ridge;\n"
"border-color: #0F2D40;\n"
"border-radius: none;\n"
"height: 15px;\n"
"font-size: 12px;\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 #194759, stop:1 #225E75);\n"
"padding-left: 5px;"))
        self.explorerPathEntry.setText(_fromUtf8(""))
        self.explorerPathEntry.setObjectName(_fromUtf8("explorerPathEntry"))
        self.gridLayout_6.addWidget(self.explorerPathEntry, 1, 0, 1, 7)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/assets/file_manager.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.explorerTab, icon9, _fromUtf8(""))
        self.logTab = QtGui.QWidget()
        self.logTab.setObjectName(_fromUtf8("logTab"))
        self.gridLayout_3 = QtGui.QGridLayout(self.logTab)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.statusConsoleText = QtGui.QTextEdit(self.logTab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statusConsoleText.sizePolicy().hasHeightForWidth())
        self.statusConsoleText.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Shell Dlg 2"))
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.statusConsoleText.setFont(font)
        self.statusConsoleText.setAutoFillBackground(True)
        self.statusConsoleText.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 #061014, stop:1 #050C0F);\n"
"background-position: center;\n"
"border: 1px ridge;\n"
"border-color: #0F2D40;\n"
"border-radius: 2px;"))
        self.statusConsoleText.setFrameShape(QtGui.QFrame.StyledPanel)
        self.statusConsoleText.setFrameShadow(QtGui.QFrame.Plain)
        self.statusConsoleText.setLineWidth(1)
        self.statusConsoleText.setUndoRedoEnabled(False)
        self.statusConsoleText.setReadOnly(True)
        self.statusConsoleText.setCursorWidth(5)
        self.statusConsoleText.setObjectName(_fromUtf8("statusConsoleText"))
        self.gridLayout_3.addWidget(self.statusConsoleText, 0, 0, 1, 1)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/assets/log.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.logTab, icon10, _fromUtf8(""))
        self.clientsGroup = QtGui.QGroupBox(self.splitter_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clientsGroup.sizePolicy().hasHeightForWidth())
        self.clientsGroup.setSizePolicy(sizePolicy)
        self.clientsGroup.setMinimumSize(QtCore.QSize(220, 50))
        self.clientsGroup.setMaximumSize(QtCore.QSize(270, 16777215))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Shell Dlg 2"))
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.clientsGroup.setFont(font)
        self.clientsGroup.setStyleSheet(_fromUtf8("border-radius: 3px;\n"
"background: #194759;"))
        self.clientsGroup.setTitle(_fromUtf8(""))
        self.clientsGroup.setFlat(False)
        self.clientsGroup.setCheckable(False)
        self.clientsGroup.setObjectName(_fromUtf8("clientsGroup"))
        self.gridLayout_5 = QtGui.QGridLayout(self.clientsGroup)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.socketsList = QtGui.QListWidget(self.clientsGroup)
        self.socketsList.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.socketsList.sizePolicy().hasHeightForWidth())
        self.socketsList.setSizePolicy(sizePolicy)
        self.socketsList.setMinimumSize(QtCore.QSize(0, 0))
        self.socketsList.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Shell Dlg 2"))
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.socketsList.setFont(font)
        self.socketsList.setStyleSheet(_fromUtf8("QListWidget#socketsList {\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 #061014, stop:1 #050C0F);\n"
"padding: 5px;\n"
"}\n"
"QListWidget#socketsList:item:selected {\n"
"background-color: #194759;\n"
"height: 50px;\n"
"color: #2ecc71;\n"
"border: none;\n"
"}\n"
"QListWidget#socketsList:item:hover {\n"
"background-color: #0F2D40;\n"
"height: 50px;\n"
"color: #2ecc71;\n"
"}"))
        self.socketsList.setObjectName(_fromUtf8("socketsList"))
        self.gridLayout_5.addWidget(self.socketsList, 2, 0, 1, 2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.clientsLabel = QtGui.QLabel(self.clientsGroup)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Shell Dlg 2"))
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.clientsLabel.setFont(font)
        self.clientsLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.clientsLabel.setStyleSheet(_fromUtf8("background-color: #0F2D40;"))
        self.clientsLabel.setTextFormat(QtCore.Qt.PlainText)
        self.clientsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.clientsLabel.setObjectName(_fromUtf8("clientsLabel"))
        self.horizontalLayout.addWidget(self.clientsLabel)
        self.clientscountLabel = QtGui.QLabel(self.clientsGroup)
        self.clientscountLabel.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Shell Dlg 2"))
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.clientscountLabel.setFont(font)
        self.clientscountLabel.setStyleSheet(_fromUtf8("background: #0F2D40;"))
        self.clientscountLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.clientscountLabel.setObjectName(_fromUtf8("clientscountLabel"))
        self.horizontalLayout.addWidget(self.clientscountLabel)
        self.gridLayout_5.addLayout(self.horizontalLayout, 1, 0, 1, 2)
        self.serverconfigGroup = QtGui.QGroupBox(self.clientsGroup)
        self.serverconfigGroup.setMinimumSize(QtCore.QSize(0, 80))
        self.serverconfigGroup.setMaximumSize(QtCore.QSize(16777215, 150))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Shell Dlg 2"))
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.serverconfigGroup.setFont(font)
        self.serverconfigGroup.setStyleSheet(_fromUtf8("background: #0F2D40;\n"
"border: 1px solid #f07e01;"))
        self.serverconfigGroup.setTitle(_fromUtf8(""))
        self.serverconfigGroup.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.serverconfigGroup.setFlat(False)
        self.serverconfigGroup.setObjectName(_fromUtf8("serverconfigGroup"))
        self.gridLayout_7 = QtGui.QGridLayout(self.serverconfigGroup)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.ipaddressLabel = QtGui.QLabel(self.serverconfigGroup)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Shell Dlg 2"))
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.ipaddressLabel.setFont(font)
        self.ipaddressLabel.setStyleSheet(_fromUtf8("border: none;"))
        self.ipaddressLabel.setObjectName(_fromUtf8("ipaddressLabel"))
        self.gridLayout_7.addWidget(self.ipaddressLabel, 1, 0, 1, 1)
        self.portLabel = QtGui.QLabel(self.serverconfigGroup)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Shell Dlg 2"))
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.portLabel.setFont(font)
        self.portLabel.setStyleSheet(_fromUtf8("border: none;"))
        self.portLabel.setObjectName(_fromUtf8("portLabel"))
        self.gridLayout_7.addWidget(self.portLabel, 2, 0, 1, 1)
        self.portLine = QtGui.QLineEdit(self.serverconfigGroup)
        self.portLine.setMinimumSize(QtCore.QSize(0, 28))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Shell Dlg 2"))
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.portLine.setFont(font)
        self.portLine.setStyleSheet(_fromUtf8("background-color:#194759;\n"
"border: none;\n"
"padding-left: 5px;"))
        self.portLine.setObjectName(_fromUtf8("portLine"))
        self.gridLayout_7.addWidget(self.portLine, 2, 1, 1, 1)
        self.ipaddressLine = QtGui.QLineEdit(self.serverconfigGroup)
        self.ipaddressLine.setMinimumSize(QtCore.QSize(0, 28))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Shell Dlg 2"))
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.ipaddressLine.setFont(font)
        self.ipaddressLine.setStyleSheet(_fromUtf8("background-color:#194759;\n"
"border: none;\n"
"padding-left: 5px;"))
        self.ipaddressLine.setObjectName(_fromUtf8("ipaddressLine"))
        self.gridLayout_7.addWidget(self.ipaddressLine, 1, 1, 1, 1)
        self.splitter_3 = QtGui.QSplitter(self.serverconfigGroup)
        self.splitter_3.setMinimumSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Shell Dlg 2"))
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.splitter_3.setFont(font)
        self.splitter_3.setStyleSheet(_fromUtf8("border: none;"))
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setHandleWidth(1)
        self.splitter_3.setObjectName(_fromUtf8("splitter_3"))
        self.runserverButton = QtGui.QPushButton(self.splitter_3)
        self.runserverButton.setMinimumSize(QtCore.QSize(117, 24))
        self.runserverButton.setMaximumSize(QtCore.QSize(117, 24))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Shell Dlg 2"))
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.runserverButton.setFont(font)
        self.runserverButton.setStyleSheet(_fromUtf8("QPushButton#runserverButton {\n"
"            background: #194759;\n"
"            font-size: 12px;\n"
"            border: 1px outset;\n"
"            border-color: #0F2D40;\n"
"            text-decoration: none;\n"
"            background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 #194759, stop:1 #225E75);\n"
"            }\n"
"\n"
"QPushButton#runserverButton:checked {\n"
"            background: #1f5a70;\n"
"            background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 #1c1d28, stop:1 #1c1d28);\n"
"            color: grey;\n"
"            }"))
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/assets/start.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.runserverButton.setIcon(icon11)
        self.runserverButton.setCheckable(True)
        self.runserverButton.setAutoExclusive(False)
        self.runserverButton.setObjectName(_fromUtf8("runserverButton"))
        self.stopserverButton = QtGui.QPushButton(self.splitter_3)
        self.stopserverButton.setMinimumSize(QtCore.QSize(114, 24))
        self.stopserverButton.setMaximumSize(QtCore.QSize(114, 24))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Shell Dlg 2"))
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.stopserverButton.setFont(font)
        self.stopserverButton.setStyleSheet(_fromUtf8("QPushButton#stopserverButton {\n"
"            background: #194759;\n"
"            font-size: 12px;\n"
"            border: 1px outset;\n"
"            border-color: #0F2D40;\n"
"            text-decoration: none;\n"
"            background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 #194759, stop:1 #225E75);\n"
"            }\n"
"\n"
"QPushButton#stopserverButton:checked {\n"
"            background: #1f5a70;\n"
"            background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 #1c1d28, stop:1 #1c1d28);\n"
"            color: grey;\n"
"            }"))
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/assets/stop.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stopserverButton.setIcon(icon12)
        self.stopserverButton.setCheckable(True)
        self.stopserverButton.setChecked(True)
        self.stopserverButton.setAutoExclusive(False)
        self.stopserverButton.setObjectName(_fromUtf8("stopserverButton"))
        self.gridLayout_7.addWidget(self.splitter_3, 3, 0, 1, 2)
        self.label = QtGui.QLabel(self.serverconfigGroup)
        self.label.setStyleSheet(_fromUtf8("background-color:#194759;\n"
"border: none;"))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_7.addWidget(self.label, 0, 0, 1, 2)
        self.gridLayout_5.addWidget(self.serverconfigGroup, 0, 0, 1, 2)
        self.verticalLayout_3.addWidget(self.splitter_7)
        self.byLabel = QtGui.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Shell Dlg 2"))
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.byLabel.setFont(font)
        self.byLabel.setStyleSheet(_fromUtf8("color: rgb(230, 230, 230);\n"
"background: none;\n"
""))
        self.byLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.byLabel.setObjectName(_fromUtf8("byLabel"))
        self.verticalLayout_3.addWidget(self.byLabel)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Mirakuru Client", None))
        self.remoteScriptLabel.setText(_translate("Form", "Remote Script", None))
        self.localScriptLabel.setText(_translate("Form", "Local Script", None))
        self.label_3.setText(_translate("Form", "FIle", None))
        self.label_2.setText(_translate("Form", "Directory", None))
        self.label_4.setText(_translate("Form", "Hidden Directory", None))
        self.label_5.setText(_translate("Form", "Hidden File", None))
        self.label_6.setText(_translate("Form", "Date Modified", None))
        self.explorerTable.setSortingEnabled(False)
        item = self.explorerTable.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Type", None))
        item = self.explorerTable.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Name", None))
        item = self.explorerTable.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Date Modified", None))
        item = self.explorerTable.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Size", None))
        self.clientsLabel.setText(_translate("Form", "Servers", None))
        self.clientscountLabel.setText(_translate("Form", "0", None))
        self.ipaddressLabel.setText(_translate("Form", "Ip address", None))
        self.portLabel.setText(_translate("Form", "Port", None))
        self.portLine.setText(_translate("Form", "4434", None))
        self.ipaddressLine.setText(_translate("Form", "0.0.0.0", None))
        self.runserverButton.setText(_translate("Form", "Start", None))
        self.stopserverButton.setText(_translate("Form", "Stop", None))
        self.label.setText(_translate("Form", "Client Configuration", None))
        self.byLabel.setText(_translate("Form", "Coded by Uri Patton 2014", None))

import res
