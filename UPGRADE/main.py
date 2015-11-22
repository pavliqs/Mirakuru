# -*- coding: utf-8 -*-

import sys
import socket
from threading import Thread

from PyQt4.QtGui import *
from PyQt4.QtCore import *

from ui import main_ui, res


class MainDialog(QMainWindow, main_ui.Ui_MainWindow):

    def __init__(self, parent=None):
        super(MainDialog, self).__init__(parent)
        self.setupUi(self)

        # sockets Timeout
        self.timeout = None

        # unlocked servers bank
        self.unlockedSockets = []

        # indexes for servers table
        self.index_of_ipAddress = 0
        self.index_of_location = 1
        self.index_of_socket = 2
        self.index_of_os = 3

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
        while self.acceptthreadState == True:
            try:

                # Try accept connection
                self.sock, self.address = self.c.accept()
            except:

                continue

            if self.acceptthreadState == False:
                return
            if self.sock:

                # Set timeout None
                self.sock.settimeout(self.timeout)

                # Save connected socket
                socketIndex = self.address[1]
                self.socks[socketIndex] = {}
                self.socks[socketIndex]['sock'] = self.sock
                self.socks[socketIndex]['ip_address'] = self.address[0]
                self.socks[socketIndex]['socket'] = self.address[1]
                self.socks[socketIndex]['is_protected'] = True

                self.updateServersTable()

    # Update Servers Table from self.socks
    def updateServersTable(self):
        self.serversTable.setRowCount(len(self.socks))
        for index, obj in enumerate(self.socks):
            item = QTableWidgetItem(self.socks[obj]['ip_address'])
            self.serversTable.setItem(index, self.index_of_ipAddress, item)
            item = QTableWidgetItem('Georgia')
            self.serversTable.setItem(index, self.index_of_location, item)
            item = QTableWidgetItem(str(self.socks[obj]['socket']))
            self.serversTable.setItem(index, self.index_of_socket, item)
            item = QTableWidgetItem('Windows 7 Service pack 3')
            self.serversTable.setItem(index, self.index_of_os, item)


    # Stop Listen for Servers
    def stopListen(self):
        pass


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