import sys,qfluentwidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication
from qfluentwidgets import FluentIcon, SplitFluentWindow
from  PyQt5.QtCore import Qt
from FormsPage import FormsPage

class DLLauncher(SplitFluentWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("月梦初晓MC 启动器")
        self.setWindowIcon(QIcon("src/ICO.png"))
        qfluentwidgets.setThemeColor("#66ccff")
        
        #添加子页面
        self.FormsPage = FormsPage(self)
        self.addSubInterface(self.FormsPage, FluentIcon.FEEDBACK, "表单中心")


if __name__ == "__main__":
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    app = QApplication(sys.argv)
    w = DLLauncher()
    w.show()
    app.exec_()