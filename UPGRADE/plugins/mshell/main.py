from PyQt4.QtGui import *
from PyQt4.QtCore import *

import main_ui


class mainPopup(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.setAttribute(Qt.WA_DeleteOnClose)


