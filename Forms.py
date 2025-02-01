from PyQt5 import QtCore, QtGui, QtWidgets
from qfluentwidgets import ElevatedCardWidget, HyperlinkLabel, PixmapLabel, PrimaryPushButton, PrimaryToolButton, TitleLabel

# 原生成的 UI 类
class Ui_FormsPage(object):
    def setupUi(self, FormsPage):
        FormsPage.setObjectName("FormsPage")
        FormsPage.resize(855, 499)
        self.gridLayoutWidget = QtWidgets.QWidget(FormsPage)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 20, 296, 451))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.PassPortCard = ElevatedCardWidget(self.gridLayoutWidget)
        self.PassPortCard.setObjectName("PassPortCard")
        # 修正拼写错误
        self.PassPortTitle = TitleLabel(self.PassPortCard)
        self.PassPortTitle.setGeometry(QtCore.QRect(75, 5, 146, 38))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.PassPortTitle.setFont(font)
        self.PassPortTitle.setTextFormat(QtCore.Qt.PlainText)
        self.PassPortTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.PassPortTitle.setObjectName("PassPortTitle")
        self.PassPortQRcode = PixmapLabel(self.PassPortCard)
        self.PassPortQRcode.setGeometry(QtCore.QRect(5, 50, 286, 391))
        self.PassPortQRcode.setPixmap(QtGui.QPixmap("src/PassPort-Application-Qrcode.png"))
        self.PassPortQRcode.setScaledContents(True)
        self.PassPortQRcode.setWordWrap(False)
        self.PassPortQRcode.setObjectName("PassPortQRcode")
        self.PassPortLinkButton = PrimaryPushButton(self.PassPortCard)
        self.PassPortLinkButton.setGeometry(QtCore.QRect(55, 400, 186, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.PassPortLinkButton.setFont(font)
        icon = QtGui.QIcon.fromTheme("FluentIcon.SHARE")
        self.PassPortLinkButton.setIcon(icon)
        self.PassPortLinkButton.setProperty("hasIcon", True)
        self.PassPortLinkButton.setObjectName("PassPortLinkButton")
        self.PassPortQRcode.raise_()
        self.PassPortTitle.raise_()
        self.PassPortLinkButton.raise_()
        self.gridLayout.addWidget(self.PassPortCard, 0, 0, 1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(FormsPage)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(330, 20, 501, 121))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.ElevatedCardWidget = ElevatedCardWidget(self.gridLayoutWidget_2)
        self.ElevatedCardWidget.setObjectName("ElevatedCardWidget")
        self.Report = TitleLabel(self.ElevatedCardWidget)
        self.Report.setGeometry(QtCore.QRect(10, 10, 256, 38))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Report.setFont(font)
        self.Report.setTextFormat(QtCore.Qt.PlainText)
        self.Report.setAlignment(QtCore.Qt.AlignCenter)
        self.Report.setObjectName("Report")
        self.HyperlinkLabel = HyperlinkLabel(self.ElevatedCardWidget)
        self.HyperlinkLabel.setGeometry(QtCore.QRect(120, 60, 361, 26))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(12)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.HyperlinkLabel.setFont(font)
        self.HyperlinkLabel.setUrl(QtCore.QUrl("https://docs.qq.com/form/page/DTWVTUmxpZkVveWJN"))
        self.HyperlinkLabel.setUnderlineVisible(True)
        self.HyperlinkLabel.setProperty("underline", True)
        self.HyperlinkLabel.setObjectName("HyperlinkLabel")
        self.PrimaryToolButton = PrimaryToolButton(self.ElevatedCardWidget)
        self.PrimaryToolButton.setGeometry(QtCore.QRect(35, 55, 76, 36))
        self.PrimaryToolButton.setObjectName("PrimaryToolButton")
        self.gridLayout_2.addWidget(self.ElevatedCardWidget, 0, 0, 1, 1)
        self.gridLayoutWidget_3 = QtWidgets.QWidget(FormsPage)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(330, 155, 241, 316))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.ElevatedCardWidget_2 = ElevatedCardWidget(self.gridLayoutWidget_3)
        self.ElevatedCardWidget_2.setObjectName("ElevatedCardWidget_2")
        self.MoreInfo = TitleLabel(self.ElevatedCardWidget_2)
        self.MoreInfo.setGeometry(QtCore.QRect(45, 5, 146, 38))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.MoreInfo.setFont(font)
        self.MoreInfo.setTextFormat(QtCore.Qt.PlainText)
        self.MoreInfo.setAlignment(QtCore.Qt.AlignCenter)
        self.MoreInfo.setObjectName("MoreInfo")
        self.PixmapLabel = PixmapLabel(self.ElevatedCardWidget_2)
        self.PixmapLabel.setGeometry(QtCore.QRect(20, 45, 206, 206))
        self.PixmapLabel.setPixmap(QtGui.QPixmap("src/MoreInfoQRcode.png"))
        self.PixmapLabel.setScaledContents(True)
        self.PixmapLabel.setObjectName("PixmapLabel")
        self.MoreInfoButton = PrimaryPushButton(self.ElevatedCardWidget_2)
        self.MoreInfoButton.setGeometry(QtCore.QRect(25, 265, 186, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.MoreInfoButton.setFont(font)
        icon = QtGui.QIcon.fromTheme("FluentIcon.SHARE")
        self.MoreInfoButton.setIcon(icon)
        self.MoreInfoButton.setProperty("hasIcon", True)
        self.MoreInfoButton.setObjectName("MoreInfoButton")
        self.gridLayout_3.addWidget(self.ElevatedCardWidget_2, 0, 0, 1, 1)
        self.gridLayoutWidget_4 = QtWidgets.QWidget(FormsPage)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(590, 155, 241, 316))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.ElevatedCardWidget_3 = ElevatedCardWidget(self.gridLayoutWidget_4)
        self.ElevatedCardWidget_3.setObjectName("ElevatedCardWidget_3")
        # 修正拼写错误
        self.AboutLauncher = TitleLabel(self.ElevatedCardWidget_3)
        self.AboutLauncher.setGeometry(QtCore.QRect(50, 5, 146, 38))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.AboutLauncher.setFont(font)
        self.AboutLauncher.setTextFormat(QtCore.Qt.PlainText)
        self.AboutLauncher.setAlignment(QtCore.Qt.AlignCenter)
        self.AboutLauncher.setObjectName("AboutLauncher")
        self.GithubButton = PrimaryPushButton(self.ElevatedCardWidget_3)
        self.GithubButton.setGeometry(QtCore.QRect(25, 265, 186, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.GithubButton.setFont(font)
        icon = QtGui.QIcon.fromTheme("FluentIcon.SHARE")
        self.GithubButton.setIcon(icon)
        self.GithubButton.setProperty("hasIcon", True)
        self.GithubButton.setObjectName("GithubButton")
        self.PixmapLabel_2 = PixmapLabel(self.ElevatedCardWidget_3)
        self.PixmapLabel_2.setGeometry(QtCore.QRect(50, 75, 141, 126))
        self.PixmapLabel_2.setPixmap(QtGui.QPixmap("src/R-C.png"))
        self.PixmapLabel_2.setScaledContents(True)
        self.PixmapLabel_2.setObjectName("PixmapLabel_2")
        self.gridLayout_4.addWidget(self.ElevatedCardWidget_3, 0, 0, 1, 1)

        self.retranslateUi(FormsPage)
        QtCore.QMetaObject.connectSlotsByName(FormsPage)

        self.PassPortQRcode.update()
        self.PixmapLabel_2.update()
        self.PixmapLabel.update()

    def retranslateUi(self, FormsPage):
        _translate = QtCore.QCoreApplication.translate
        FormsPage.setWindowTitle(_translate("FormsPage", "Form"))
        self.PassPortTitle.setText(_translate("FormsPage", "通行证申请"))
        self.PassPortLinkButton.setText(_translate("FormsPage", "填写申请表"))
        self.Report.setText(_translate("FormsPage", "BUG/更新 意见与反馈"))
        self.HyperlinkLabel.setText(_translate("FormsPage", "【腾讯文档】月梦初晓MC 反馈&bug报告"))
        self.MoreInfo.setText(_translate("FormsPage", "更多信息"))
        self.MoreInfoButton.setText(_translate("FormsPage", "跳转外部文档"))
        self.AboutLauncher.setText(_translate("FormsPage", "关于启动器"))
        self.GithubButton.setText(_translate("FormsPage", "跳转Github"))

# 新的类，继承 QWidget 并使用 Ui_FormsPage 来设置界面
class FormsPage(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_FormsPage()
        self.ui.setupUi(self)
        self.setObjectName("FormsPage")  # 设置对象名，满足 addSubInterface 要求
