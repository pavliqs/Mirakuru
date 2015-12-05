from PyQt4.QtGui import *
from PyQt4.QtCore import *

import main_ui
import console


class mainPopup(QWidget, main_ui.Ui_Form):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)

        self.console = console.Console()
        self.summaryBoxTopLayout = QHBoxLayout()
        self.summaryBoxTopLayout.addWidget(self.console)
        self.setLayout(self.summaryBoxTopLayout)


