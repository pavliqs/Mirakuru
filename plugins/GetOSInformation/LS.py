



class PopupDialog(QDialog):
    def __init__(self, parent=None, data=None):
		QWidget.__init__(self, parent)
		layout = QGridLayout(self)
		label = QLabel(data)
		layout.addWidget(label)

self.dialog = PopupDialog(data=data)
# For Modal dialogs
self.dialog.exec_()
