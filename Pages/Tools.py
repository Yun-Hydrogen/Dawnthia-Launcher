from PyQt5.QtWidgets import QWidget
from UIs.Ui_Tools import Ui_Tools

class Tools(QWidget, Ui_Tools):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("Tools")
        self.setupUi(self)
        