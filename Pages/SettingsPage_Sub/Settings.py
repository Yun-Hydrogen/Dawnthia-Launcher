from PyQt5.QtWidgets import QWidget
from UIs.Ui_Settings import Ui_Settings
from qfluentwidgets import FluentIcon

class Settings(QWidget, Ui_Settings):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("Tools")
        self.setupUi(self)

        #设置图标
        self.Setting1_ColorButton.setIcon(FluentIcon.RIGHT_ARROW)
        self.Setting1_ColorButton.setIcon                                                                                                                                                                                                                                                                                   )

