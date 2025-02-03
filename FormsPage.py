from PyQt5.QtWidgets import QWidget
from  Ui_FormsPage import  Ui_FormsPage

class FormsPage(QWidget, Ui_FormsPage):
    def __init__(self,parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)