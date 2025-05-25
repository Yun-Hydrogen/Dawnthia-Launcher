from PyQt5.QtWidgets import QWidget, QVBoxLayout, QSizePolicy
from UIs.Ui_ToolsPage import Ui_ToolsPage
from Pages.ToolsPage_Sub.Tools import Tools
from PyQt5.QtCore import Qt
from qfluentwidgets import InfoBar, InfoBarPosition


class ToolsPage(QWidget, Ui_ToolsPage):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setObjectName("ToolsPage")
        self.setupUi(self)
        
        # 创建滚动区域
        self.SmoothScrollArea.setWidget(Tools(self))
        self.SmoothScrollArea.setWidgetResizable(True)
        self.SmoothScrollArea.enableTransparentBackground()

        
        # 信息提示
        InfoBar.error("注意注意！","在使用任何工具前，请确保你已知晓其工作原理，开发者不对使用工具造成的任何后果负责！",Qt.Horizontal,False,2000,InfoBarPosition.TOP,self)