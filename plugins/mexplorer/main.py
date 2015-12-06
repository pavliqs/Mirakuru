from PyQt4.QtGui import *
from PyQt4.QtCore import *

import socket
from communicator.messanger import mSend, mReceive

class mainPopup(QWidget):

    def __init__(self, *args):
        QWidget.__init__(self)

        self.sock = args[0]['sock']
        self.socket = args[0]['socket']
        self.ipAddress = args[0]['ipAddress']
        self.icon = args[0]['icon']

        self.setWindowTitle('Remote File Explorer on - %s - Socket #%s' % (self.ipAddress, self.socket))
        self.setWindowIcon(QIcon(self.icon))