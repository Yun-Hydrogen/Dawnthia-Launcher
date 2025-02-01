from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout
from qfluentwidgets import FluentIcon


class NoticePage(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.setObjectName("NoticePage")
