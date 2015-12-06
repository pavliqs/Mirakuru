from PyQt4.QtGui import *
from PyQt4.QtCore import *

import time
import socket

import main_ui
import console

from communicator.messanger import mSend, mReceive

class mainPopup(QWidget, main_ui.Ui_Form):
    def __init__(self, **kwargs):
        QWidget.__init__(self)
        self.setupUi(self)

        self.console = console.Console()
        self.gridLayout.addWidget(self.console)

        self.connect(self.console, SIGNAL("returnPressed"), self.runCommand)

    # run shell command
    def runCommand(self):
        try:
            command = self.console.command
            mSend(command)
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
