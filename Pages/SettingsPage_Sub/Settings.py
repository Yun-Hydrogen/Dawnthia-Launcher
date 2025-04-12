from PyQt5.QtWidgets import QWidget
from UIs.Ui_Settings import Ui_Settings
from qfluentwidgets import FluentIcon
import qfluentwidgets

class Settings(QWidget, Ui_Settings):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("Tools")
        self.setupUi(self)

        #设置图标
        self.Setting1_ColorButton.setIcon(FluentIcon.EDIT)
        self.Setting1_ApplyButton.setIcon(FluentIcon.ACCEPT)

        #信号连接
        self.Setting1_ApplyButton.clicked.connect(self.ApplyColorTheme)
        self.Setting1_ColorButton.clicked.connect(self.ChooseThemeColor)

    def ApplyColorTheme(self):
        print("COLOR CHANGE BUTTON CLICKED")
        from Main import DawnthiaLauncher
        DawnthiaLauncher.changeThemecolor(self)
        del DawnthiaLauncher

    def ChooseThemeColor(self):
        pass