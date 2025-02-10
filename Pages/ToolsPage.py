from PyQt5.QtWidgets import QWidget
from  UIs.Ui_ToolsPage import Ui_ToolsPage
from Pages.FormsPage import FormsPage

class ToolsPage(QWidget, Ui_ToolsPage):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setObjectName("ToolsPage")
        self.setupUi(self)
        self.SmoothScrollArea.setWidgetResizable(True)
        self.SmoothScrollArea.setWidget(FormsPage())
        self.SmoothScrollArea.enableTransparentBackground()
