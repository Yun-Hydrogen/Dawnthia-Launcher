# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\Program-Project\DreamingLight-Launcher\UIs\HelpPage.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_HelpPage(object):
    def setupUi(self, HelpPage):
        HelpPage.setObjectName("HelpPage")
        HelpPage.resize(860, 500)
        HelpPage.setMinimumSize(QtCore.QSize(860, 500))
        HelpPage.setMaximumSize(QtCore.QSize(860, 500))
        self.gridLayoutWidget = QtWidgets.QWidget(HelpPage)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(15, 20, 826, 466))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.IndeterminateProgressRing = IndeterminateProgressRing(HelpPage)
        self.IndeterminateProgressRing.setGeometry(QtCore.QRect(380, 205, 80, 80))
        self.IndeterminateProgressRing.setObjectName("IndeterminateProgressRing")
        self.CaptionLabel = CaptionLabel(HelpPage)
        self.CaptionLabel.setGeometry(QtCore.QRect(385, 290, 76, 21))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.CaptionLabel.setFont(font)
        self.CaptionLabel.setObjectName("CaptionLabel")
        self.CaptionLabel.raise_()
        self.IndeterminateProgressRing.raise_()
        self.gridLayoutWidget.raise_()

        self.retranslateUi(HelpPage)
        QtCore.QMetaObject.connectSlotsByName(HelpPage)

    def retranslateUi(self, HelpPage):
        _translate = QtCore.QCoreApplication.translate
        HelpPage.setWindowTitle(_translate("HelpPage", "Form"))
        self.CaptionLabel.setText(_translate("HelpPage", "网页加载"))
from qfluentwidgets import CaptionLabel, IndeterminateProgressRing
