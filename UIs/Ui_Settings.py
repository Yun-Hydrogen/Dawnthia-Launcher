# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\Document\Project\Dawnthia-Launcher\UIs\UI\Sub_Ui\Settings.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Settings(object):
    def setupUi(self, Settings):
        Settings.setObjectName("Settings")
        Settings.resize(830, 830)
        Settings.setMinimumSize(QtCore.QSize(830, 830))
        Settings.setMaximumSize(QtCore.QSize(830, 830))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        Settings.setFont(font)
        self.verticalLayoutWidget = QtWidgets.QWidget(Settings)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 381, 71))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.Setting1_Layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.Setting1_Layout.setContentsMargins(0, 0, 0, 0)
        self.Setting1_Layout.setObjectName("Setting1_Layout")
        self.Setting1_CardWidget = CardWidget(self.verticalLayoutWidget)
        self.Setting1_CardWidget.setObjectName("Setting1_CardWidget")
        self.Setting1_TitleLabel = TitleLabel(self.Setting1_CardWidget)
        self.Setting1_TitleLabel.setGeometry(QtCore.QRect(10, 5, 181, 38))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.Setting1_TitleLabel.setFont(font)
        self.Setting1_TitleLabel.setObjectName("Setting1_TitleLabel")
        self.Setting1_BodyLabel = BodyLabel(self.Setting1_CardWidget)
        self.Setting1_BodyLabel.setGeometry(QtCore.QRect(10, 35, 231, 19))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.Setting1_BodyLabel.setFont(font)
        self.Setting1_BodyLabel.setProperty("lightColor", QtGui.QColor(140, 140, 140))
        self.Setting1_BodyLabel.setObjectName("Setting1_BodyLabel")
        self.Setting1_ColorButton = PushButton(self.Setting1_CardWidget)
        self.Setting1_ColorButton.setGeometry(QtCore.QRect(180, 20, 106, 32))
        self.Setting1_ColorButton.setProperty("hasIcon", True)
        self.Setting1_ColorButton.setObjectName("Setting1_ColorButton")
        self.Setting1_ApplyButton = PrimaryPushButton(self.Setting1_CardWidget)
        self.Setting1_ApplyButton.setGeometry(QtCore.QRect(290, 20, 76, 31))
        self.Setting1_ApplyButton.setProperty("hasIcon", True)
        self.Setting1_ApplyButton.setObjectName("Setting1_ApplyButton")
        self.Setting1_Layout.addWidget(self.Setting1_CardWidget)

        self.retranslateUi(Settings)
        QtCore.QMetaObject.connectSlotsByName(Settings)

    def retranslateUi(self, Settings):
        _translate = QtCore.QCoreApplication.translate
        Settings.setWindowTitle(_translate("Settings", "Form"))
        self.Setting1_TitleLabel.setText(_translate("Settings", "设置应用主题色"))
        self.Setting1_BodyLabel.setText(_translate("Settings", "默认是#66CCFF哦~（成分复杂"))
        self.Setting1_ColorButton.setText(_translate("Settings", "选取颜色"))
        self.Setting1_ApplyButton.setText(_translate("Settings", "应用"))
from qfluentwidgets import BodyLabel, CardWidget, PrimaryPushButton, PushButton, TitleLabel
