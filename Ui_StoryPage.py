# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\Program-Project\DreamingLight-Launcher\UIs\StoryPage.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_StoryPage(object):
    def setupUi(self, StoryPage):
        StoryPage.setObjectName("StoryPage")
        StoryPage.resize(860, 500)
        StoryPage.setMinimumSize(QtCore.QSize(860, 500))
        StoryPage.setMaximumSize(QtCore.QSize(860, 500))
        self.IndeterminateProgressRing = IndeterminateProgressRing(StoryPage)
        self.IndeterminateProgressRing.setGeometry(QtCore.QRect(410, 205, 80, 80))
        self.IndeterminateProgressRing.setObjectName("IndeterminateProgressRing")
        self.CaptionLabel = CaptionLabel(StoryPage)
        self.CaptionLabel.setGeometry(QtCore.QRect(415, 290, 76, 21))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.CaptionLabel.setFont(font)
        self.CaptionLabel.setObjectName("CaptionLabel")
        self.gridLayoutWidget = QtWidgets.QWidget(StoryPage)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(15, 10, 826, 476))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.CaptionLabel.raise_()
        self.IndeterminateProgressRing.raise_()
        self.gridLayoutWidget.raise_()

        self.retranslateUi(StoryPage)
        QtCore.QMetaObject.connectSlotsByName(StoryPage)

    def retranslateUi(self, StoryPage):
        _translate = QtCore.QCoreApplication.translate
        StoryPage.setWindowTitle(_translate("StoryPage", "Form"))
        self.CaptionLabel.setText(_translate("StoryPage", "网页加载"))
from qfluentwidgets import CaptionLabel, IndeterminateProgressRing
