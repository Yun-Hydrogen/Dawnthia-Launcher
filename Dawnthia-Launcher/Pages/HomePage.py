from PyQt5.QtWidgets import QWidget
from  UIs.Ui_HomePage import Ui_HomePage

class HomePage(QWidget, Ui_HomePage):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        
        #自动加载版本号
        from Config import launcher_version
        self.VersionLabel.setText(launcher_version)

        