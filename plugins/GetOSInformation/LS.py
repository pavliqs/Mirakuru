# Information Gathering Plugin
# Start Popup Dialog
class PopupDialog(QDialog):
    def __init__(self, parent=None, data=None):
        QWidget.__init__(self, parent)
        self.setWindowTitle('Information Gathering Plugin V1.0')
        self.setStyleSheet('background-color: green;color: yellow;')
        layout = QGridLayout(self)
        title = QLabel('Information About System')
        title.setStyleSheet('font-size: 28px;')
        layout.addWidget(title)
        label = QLabel(data)
        layout.addWidget(label)

dialog = PopupDialog(data=data)
dialog.exec_()
# End Popup Dialog
# Plugin END
