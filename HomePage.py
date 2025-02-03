from PyQt5.QtWidgets import QWidget
from  Ui_HomePage import Ui_HomePage
from qfluentwidgets import FluentIcon
from PyQt5.QtGui import QPixmap, QDesktopServices
from PyQt5.QtCore import QUrl
from qfluentwidgets import MessageBox

class HomePage(QWidget, Ui_HomePage):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)