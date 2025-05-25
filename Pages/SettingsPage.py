from PyQt5.QtWidgets import QWidget
from  UIs.Ui_SettingsPage import Ui_SettingsPage
from Pages.SettingsPage_Sub.Settings import Settings

class SettingsPage(QWidget, Ui_SettingsPage):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        
        # 创建滚动区域
        self.SmoothScrollArea.setWidget(Settings(self))
        self.SmoothScrollArea.setWidgetResizable(True)
        self.SmoothScrollArea.enableTransparentBackground()