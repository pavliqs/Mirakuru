from PyQt4.QtGui import *
from PyQt4.QtCore import *

import socket

import main_ui
import console

from communicator.messanger import mSend, mReceive

class mainPopup(QWidget, main_ui.Ui_Form):

    def __init__(self, *args):
        QWidget.__init__(self)
        self.setupUi(self)

        self.sock = args[0]['sock']
        self.socket = args[0]['socket']
        self.ipAddress = args[0]['ipAddress']
        self.icon = args[0]['icon']

        self.setWindowTitle('Connected to - %s - Socket #%s' % (self.ipAddress, self.socket))
        self.setWindowIcon(QIcon(self.icon))

        self.console = console.Console()
        self.gridLayout.addWidget(self.console)

        self.connect(self.console, SIGNAL("returnPressed"), self.runCommand)

    # run shell command
    def runCommand(self):
        try:
            command = self.console.command[1:] if self.console.command.startswith(' ') else self.console.command
            mSend(self.sock, command)
            data = mReceive(self.sock)
            while data.startswith('\n'):
                data = data[1:]
            data = data.replace('\n', '<br>')

            self.console.append('<br><font color=#3CFFFF>'+data+'</font>')
            self.console.newPrompt()

        except socket.error:
            # Error with connection
            self.close()
