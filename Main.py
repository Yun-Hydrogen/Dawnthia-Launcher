import qfluentwidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication
from qfluentwidgets import FluentIcon, MSFluentWindow, NavigationItemPosition
from  PyQt5.QtCore import Qt
import sys
sys.dont_write_bytecode = True
#导入子页面============================
from Pages.FormsPage import FormsPage
from Pages.HomePage import HomePage
from Pages.StoryPage import StoryPage
from Pages.SettingsPage import SettingsPage
from Pages.ToolsPage import ToolsPage
from Pages.HelpPage import HelpPage

class DawnthiaLauncher(MSFluentWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("月梦初晓|Dawnthia 中心")
        self.setWindowIcon(QIcon("UIs/src/ICO.png"))
        self.setFixedSize(920, 540)
        self.setMicaEffectEnabled(False)
        from Config import color_theme
        qfluentwidgets.setThemeColor(color_theme)
        del color_theme

        #添加子页面
        self.HomePage = HomePage(self)
        self.addSubInterface(self.HomePage, FluentIcon.HOME, "主页")
        self.FormsPage = FormsPage(self)
        self.addSubInterface(self.FormsPage, FluentIcon.LABEL, "表单")
        self.StoryPage = StoryPage(self)
        self.addSubInterface(self.StoryPage, FluentIcon.BOOK_SHELF, "剧情")
        self.HelpPage = HelpPage(self)
        self.addSubInterface(self.HelpPage, FluentIcon.HELP, "帮助")
        self.ToolsPage = ToolsPage(self)
        self.addSubInterface(self.ToolsPage, FluentIcon.DEVELOPER_TOOLS, "工具")
        self.SettingsPage = SettingsPage(self)
        self.addSubInterface(self.SettingsPage, FluentIcon.SETTING,"设置", position=NavigationItemPosition.BOTTOM)

if __name__ == "__main__":
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    # noinspection PyTypeChecker
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    # noinspection PyTypeChecker
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)
    app = QApplication(sys.argv)
    w = DawnthiaLauncher()
    w.show()
    app.exec_()


