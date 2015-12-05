from PyQt4.QtGui import *
from PyQt4.QtCore import *

import main_ui


class mainPopup(QWidget, main_ui.Ui_Form):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)


