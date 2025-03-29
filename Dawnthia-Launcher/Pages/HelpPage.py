from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QVBoxLayout, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView
from UIs.Ui_HelpPage import Ui_HelpPage
from qfluentwidgets import MessageBox
from PyQt5.QtGui import QDesktopServices

class HelpPage(QWidget,Ui_HelpPage):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("HelpPage")
        self.setupUi(self)

        # 创建布局
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)  # 去除边距

        # 创建浏览器控件
        self.browser = QWebEngineView(self.gridLayoutWidget)  # 设置父控件为 gridLayoutWidget
        self.gridLayout.addWidget(self.browser, 0, 0, 1, 1)  # 添加到 gridLayout 的第一行第一列

        # 加载网页（注意URL格式）
        self.browser.load(QUrl("https://docs.qq.com/smartsheet/DZk9WTURpdm5jSVR0?tab=sc_G4bBde")) 
        
