# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\Program-Project\DreamingLight-Launcher\UIs\FormsPage.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FormsPage(object):
    def setupUi(self, FormsPage):
        FormsPage.setObjectName("FormsPage")
        FormsPage.resize(860, 500)
        FormsPage.setMinimumSize(QtCore.QSize(860, 500))
        FormsPage.setMaximumSize(QtCore.QSize(860, 500))
        self.gridLayoutWidget = QtWidgets.QWidget(FormsPage)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 20, 296, 451))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.PassPortGird = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.PassPortGird.setContentsMargins(0, 0, 0, 0)
        self.PassPortGird.setObjectName("PassPortGird")
        self.PassPortCard = ElevatedCardWidget(self.gridLayoutWidget)
        self.PassPortCard.setObjectName("PassPortCard")
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
        self.PassPortButton = PrimaryPushButton(self.PassPortCard)
        self.PassPortButton.setGeometry(QtCore.QRect(55, 400, 186, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.PassPortButton.setFont(font)
        icon = QtGui.QIcon.fromTheme("FluentIcon.SHARE")
        self.PassPortButton.setIcon(icon)
        self.PassPortButton.setProperty("hasIcon", True)
        self.PassPortButton.setObjectName("PassPortButton")
        self.gridLayoutWidget_5 = QtWidgets.QWidget(self.PassPortCard)
        self.gridLayoutWidget_5.setGeometry(QtCore.QRect(20, 55, 251, 326))
        self.gridLayoutWidget_5.setObjectName("gridLayoutWidget_5")
        self.PassPortQRCode_Grid = QtWidgets.QGridLayout(self.gridLayoutWidget_5)
        self.PassPortQRCode_Grid.setContentsMargins(0, 0, 0, 0)
        self.PassPortQRCode_Grid.setObjectName("PassPortQRCode_Grid")
        self.QRcode_PassPort = PixmapLabel(self.gridLayoutWidget_5)
        self.QRcode_PassPort.setPixmap(QtGui.QPixmap(":/IMG/src/PassPort-Application-Qrcode.png"))
        self.QRcode_PassPort.setScaledContents(True)
        self.QRcode_PassPort.setObjectName("QRcode_PassPort")
        self.PassPortQRCode_Grid.addWidget(self.QRcode_PassPort, 0, 0, 1, 1)
        self.PassPortGird.addWidget(self.PassPortCard, 0, 0, 1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(FormsPage)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(330, 20, 501, 121))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.ReportGird = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.ReportGird.setContentsMargins(0, 0, 0, 0)
        self.ReportGird.setObjectName("ReportGird")
        self.ReportCard = ElevatedCardWidget(self.gridLayoutWidget_2)
        self.ReportCard.setObjectName("ReportCard")
        self.Report = TitleLabel(self.ReportCard)
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
        self.ReportLink = HyperlinkLabel(self.ReportCard)
        self.ReportLink.setGeometry(QtCore.QRect(120, 60, 361, 26))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(12)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.ReportLink.setFont(font)
        self.ReportLink.setUrl(QtCore.QUrl("https://docs.qq.com/form/page/DTWVTUmxpZkVveWJN"))
        self.ReportLink.setUnderlineVisible(True)
        self.ReportLink.setProperty("underline", True)
        self.ReportLink.setObjectName("ReportLink")
        self.ReportLinkButton = PrimaryToolButton(self.ReportCard)
        self.ReportLinkButton.setGeometry(QtCore.QRect(35, 55, 76, 36))
        self.ReportLinkButton.setObjectName("ReportLinkButton")
        self.ReportGird.addWidget(self.ReportCard, 0, 0, 1, 1)
        self.gridLayoutWidget_3 = QtWidgets.QWidget(FormsPage)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(330, 155, 241, 316))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.MoreInfoGird = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.MoreInfoGird.setContentsMargins(0, 0, 0, 0)
        self.MoreInfoGird.setObjectName("MoreInfoGird")
        self.MoreInfoCard = ElevatedCardWidget(self.gridLayoutWidget_3)
        self.MoreInfoCard.setObjectName("MoreInfoCard")
        self.MoreInfo = TitleLabel(self.MoreInfoCard)
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
        self.MoreInfoButton = PrimaryPushButton(self.MoreInfoCard)
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
        self.gridLayoutWidget_6 = QtWidgets.QWidget(self.MoreInfoCard)
        self.gridLayoutWidget_6.setGeometry(QtCore.QRect(20, 55, 201, 181))
        self.gridLayoutWidget_6.setObjectName("gridLayoutWidget_6")
        self.MoreInfoQRCode_Gird = QtWidgets.QGridLayout(self.gridLayoutWidget_6)
        self.MoreInfoQRCode_Gird.setContentsMargins(0, 0, 0, 0)
        self.MoreInfoQRCode_Gird.setObjectName("MoreInfoQRCode_Gird")
        self.MoreInfo_QRcode = PixmapLabel(self.gridLayoutWidget_6)
        self.MoreInfo_QRcode.setPixmap(QtGui.QPixmap(":/IMG/src/MoreInfoQRcode.png"))
        self.MoreInfo_QRcode.setScaledContents(True)
        self.MoreInfo_QRcode.setObjectName("MoreInfo_QRcode")
        self.MoreInfoQRCode_Gird.addWidget(self.MoreInfo_QRcode, 0, 0, 1, 1)
        self.MoreInfoGird.addWidget(self.MoreInfoCard, 0, 0, 1, 1)
        self.gridLayoutWidget_4 = QtWidgets.QWidget(FormsPage)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(590, 155, 241, 316))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.AboutGird = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.AboutGird.setContentsMargins(0, 0, 0, 0)
        self.AboutGird.setObjectName("AboutGird")
        self.AboutLauncherCard = ElevatedCardWidget(self.gridLayoutWidget_4)
        self.AboutLauncherCard.setObjectName("AboutLauncherCard")
        self.AboutLanucher = TitleLabel(self.AboutLauncherCard)
        self.AboutLanucher.setGeometry(QtCore.QRect(50, 5, 146, 38))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.AboutLanucher.setFont(font)
        self.AboutLanucher.setTextFormat(QtCore.Qt.PlainText)
        self.AboutLanucher.setAlignment(QtCore.Qt.AlignCenter)
        self.AboutLanucher.setObjectName("AboutLanucher")
        self.GithubButton = PrimaryPushButton(self.AboutLauncherCard)
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
        self.GitHub_Gird = IconWidget(self.AboutLauncherCard)
        self.GitHub_Gird.setGeometry(QtCore.QRect(45, 60, 161, 161))
        self.GitHub_Gird.setObjectName("GitHub_Gird")
        self.AboutGird.addWidget(self.AboutLauncherCard, 0, 0, 1, 1)

        self.retranslateUi(FormsPage)
        QtCore.QMetaObject.connectSlotsByName(FormsPage)

    def retranslateUi(self, FormsPage):
        _translate = QtCore.QCoreApplication.translate
        FormsPage.setWindowTitle(_translate("FormsPage", "Form"))
        self.PassPortTitle.setText(_translate("FormsPage", "通行证申请"))
        self.PassPortButton.setText(_translate("FormsPage", "填写申请表"))
        self.Report.setText(_translate("FormsPage", "BUG/更新 意见与反馈"))
        self.ReportLink.setText(_translate("FormsPage", "【腾讯文档】月梦初晓MC 反馈&bug报告"))
        self.MoreInfo.setText(_translate("FormsPage", "更多信息"))
        self.MoreInfoButton.setText(_translate("FormsPage", "跳转外部文档"))
        self.AboutLanucher.setText(_translate("FormsPage", "关于启动器"))
        self.GithubButton.setText(_translate("FormsPage", "跳转Github"))
from qfluentwidgets import ElevatedCardWidget, HyperlinkLabel, IconWidget, PixmapLabel, PrimaryPushButton, PrimaryToolButton, TitleLabel
import UIs.FromsPage_rc
