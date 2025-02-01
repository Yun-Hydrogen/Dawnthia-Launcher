#=====================模块导入===================
import sys,os
from PyQt5.QtGui import QIcon
#[from PyQt5.QtCore import QCoreApplication,Qt]
from PyQt5.QtWidgets import QApplication
from qfluentwidgets import FluentIcon, SplitFluentWindow, NavigationItemPosition
#=====================模块导入===================END

#=====================环境变量===================
os.environ["QT_ENABLE_HIGHDPI_SCALING"] = "1"
os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
os.environ["QT_SCALE_FACTOR_ROUNDING_POLICY"] = "PassThrough"
#=====================环境变量===================END

#=====================窗口导入===================
from Home import HomePage
from Notice import  NoticePage
from Story import StoryPage
from Settings import SettingsPage
#=====================窗口导入===================END

class Main(SplitFluentWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("月梦初晓MC 启动器")
        self.setWindowIcon(QIcon("src/1.png"))
        self.dpi_scale = self.logicalDpiX() / 96.0
        self.setFixedSize(int(960 * self.dpi_scale), int(640 * self.dpi_scale))
        # 创建子页面
        self.HomePage = HomePage()
        self.NoticePage = NoticePage()
        self.StoryPage = StoryPage()
        self.SettingsPage = SettingsPage()

        self.init_navigation()        # 初始化导航栏
        self.navigationInterface.setExpandWidth(280)  # 设置导航栏宽度
        self.navigationInterface.setAcrylicEnabled(True)  # 启用亚克力效果

    #设置子页面跳转按钮
    def init_navigation(self):
        self.addSubInterface(self.HomePage, FluentIcon.HOME, "首页")
        self.addSubInterface(self.NoticePage, FluentIcon.QUICK_NOTE, "公告")
        self.addSubInterface(self.StoryPage, FluentIcon.BOOK_SHELF, "剧情")
        self.addSubInterface(self.SettingsPage, FluentIcon.SETTING, "设置",NavigationItemPosition.BOTTOM)

    def adjust_font(self):
        """动态调整字体大小"""
        font = self.font()
        font.setPixelSize(int(12 * self.dpi_scale))
        self.setFont(font)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())