from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QVBoxLayout, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView
from Ui_StoryPage import Ui_StoryPage
from qfluentwidgets import MessageBox
from PyQt5.QtGui import QDesktopServices

class StoryPage(QWidget,Ui_StoryPage):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("StoryPage")
        self.setupUi(self)
<<<<<<< HEAD
=======

        # 创建布局
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)  # 去除边距
>>>>>>> c6f3693bedfa3b66b9aed032bea98d8ed5840126
        
        # 创建浏览器控件
        self.browser = QWebEngineView(self.gridLayoutWidget)  # 设置父控件为 gridLayoutWidget
        self.gridLayout.addWidget(self.browser, 0, 0, 1, 1)  # 添加到 gridLayout 的第一行第一列
<<<<<<< HEAD
=======
        self.browser.setStyleSheet('border-radius: 30px;')
>>>>>>> c6f3693bedfa3b66b9aed032bea98d8ed5840126

        # 加载网页（注意URL格式）
        self.browser.load(QUrl("https://docs.qq.com/smartsheet/DZk9WTURpdm5jSVR0?tab=sc_CoDfra&viewId=vA1rZm")) 
        
