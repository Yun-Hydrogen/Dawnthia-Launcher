from PyQt5.QtWidgets import QWidget
from  Ui_FormsPage import  Ui_FormsPage
from qfluentwidgets import FluentIcon
from PyQt5.QtGui import QPixmap, QDesktopServices
from PyQt5.QtCore import QUrl
from qfluentwidgets import MessageBox

class FormsPage(QWidget, Ui_FormsPage):
    def __init__(self,parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        
        #设置图标
        self.PassPortButton.setIcon(FluentIcon.LINK)
        self.GithubButton.setIcon(FluentIcon.GITHUB)
        self.GitHub_Gird.setIcon(FluentIcon.GITHUB)
        self.MoreInfoButton.setIcon(FluentIcon.LINK)
        self.ReportLinkButton.setIcon(FluentIcon.LINK)

        #设置图片
        self.QRcode_PassPort.setPixmap(QPixmap("src/PassPort-Application-Qrcode.png"))
        self.MoreInfo_QRcode.setPixmap(QPixmap("src/MoreInfoQRcode.png"))

        #链接函数
        self.ReportLinkButton.clicked.connect(self.ReportLinkButton_Clicked)
    
    #链接执行
    def ReportLinkButton_Clicked(self):
        #设置对话框
        MB = MessageBox("注意ψ(._. )>", "你正在跳转到第三方网页以进行进一步操作，是否继续？", self.window())
        MB.yesButton.setText("继续")
        MB.cancelButton.setText("取消")
        if MB.exec():
            QDesktopServices.openUrl(QUrl("https://docs.qq.com/form/page/DTWVTUmxpZkVveWJN"))
        else:
            pass