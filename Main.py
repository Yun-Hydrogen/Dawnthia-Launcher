import sys,qfluentwidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication
from qfluentwidgets import FluentIcon, MSFluentWindow
from  PyQt5.QtCore import Qt
from FormsPage import FormsPage
from HomePage import HomePage

class DLLauncher(MSFluentWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("月梦初晓MC 启动器")
        self.setWindowIcon(QIcon("src/ICO.png"))
        qfluentwidgets.setThemeColor("#66ccff")
        self.setFixedSize(920, 540)
        
        #添加子页面
        self.HomePage = HomePage(self)
        self.addSubInterface(self.HomePage, FluentIcon.HOME, "主页")
        self.FormsPage = FormsPage(self)
        self.addSubInterface(self.FormsPage, FluentIcon.LABEL, "表单")


if __name__ == "__main__":
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)
    app = QApplication(sys.argv)
    w = DLLauncher()
    w.show()
    app.exec_()