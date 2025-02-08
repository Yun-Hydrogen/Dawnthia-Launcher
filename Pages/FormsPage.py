from PyQt5.QtWidgets import QWidget
from  UIs.Ui_FormsPage import  Ui_FormsPage
from qfluentwidgets import FluentIcon
from PyQt5.QtGui import QPixmap, QDesktopServices
from PyQt5.QtCore import QUrl
from qfluentwidgets import MessageBox

class FormsPage(QWidget, Ui_FormsPage):
    def __init__(self,parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.setObjectName("FormsPage")
        
        #设置图标
        self.PassPortButton.setIcon(FluentIcon.LINK)
        self.GithubButton.setIcon(FluentIcon.GITHUB)
        self.GitHub_Gird.setIcon(FluentIcon.GITHUB)
        self.MoreInfoButton.setIcon(FluentIcon.LINK)
        self.ReportLinkButton.setIcon(FluentIcon.LINK)

        #链接函数
        self.ReportLinkButton.clicked.connect(self.ReportLinkButton_Clicked)
        self.GithubButton.clicked.connect(self.GithubButton_Clicked)
        self.PassPortButton.clicked.connect(self.PassPortButton_Clicked)
        self.MoreInfoButton.clicked.connect(self.MoreInfoButton_Clicked)
    
    #链接执行
    def ReportLinkButton_Clicked(self):#反馈按钮
        MB = MessageBox("注意ψ(._. )>", "你正在跳转到第三方网页以进行进一步操作，是否继续？", self.window())
        MB.yesButton.setText("继续")
        MB.cancelButton.setText("取消")
        if MB.exec():
            QDesktopServices.openUrl(QUrl("https://docs.qq.com/form/page/DTWVTUmxpZkVveWJN"))
        else:
            pass
    
    def GithubButton_Clicked(self):#GitHub按钮
        MB = MessageBox("注意ψ(._. )>", "你正在跳转到第三方网页以进行进一步操作，是否继续？", self.window())
        MB.yesButton.setText("继续")
        MB.cancelButton.setText("取消")
        if MB.exec():
            QDesktopServices.openUrl(QUrl("https://github.com/Yun-Hydrogen/DreamingLight-Launcher"))
        else:
            pass
    
    def PassPortButton_Clicked(self):#通行证按钮
        MB = MessageBox("注意ψ(._. )>", "你正在跳转到第三方网页以进行进一步操作，是否继续？", self.window())
        MB.yesButton.setText("继续")
        MB.cancelButton.setText("取消")
        if MB.exec():
            QDesktopServices.openUrl(QUrl("https://docs.qq.com/form/page/DTW5xRXJxYWxrY1Bp"))
        else:
            pass
    
    def MoreInfoButton_Clicked(self):#更多信息按钮
        MB = MessageBox("注意ψ(._. )>", "你正在跳转到第三方网页以进行进一步操作，是否继续？", self.window())
        MB.yesButton.setText("继续")
        MB.cancelButton.setText("取消")
        if MB.exec():
            QDesktopServices.openUrl(QUrl("https://docs.qq.com/smartsheet/DZk9WTURpdm5jSVR0"))
        else:
            pass