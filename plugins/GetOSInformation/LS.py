# Start Popup Dialog
class PopupDialog(QDialog):
    def __init__(self, parent=None, data=None):
        QWidget.__init__(self, parent)
        layout = QGridLayout(self)
        label = QLabel(data)
        layout.addWidget(label)

dialog = PopupDialog(data=data)
dialog.exec_()
# End Popup Dialog
