from UIs.Ui_Settings import Ui_Settings
import qfluentwidgets, os, PyQt5

class Settings(PyQt5.QtWidgets.QWidget, Ui_Settings):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("Tools")
        self.setupUi(self)

        #设置图标
        self.Setting1_ColorButton.setIcon(qfluentwidgets.FluentIcon.EDIT)
        self.Setting1_ApplyButton.setIcon(qfluentwidgets.FluentIcon.ACCEPT)
        
        #信号连接
        self.Setting1_ColorButton.clicked.connect(self.choose_theme_color)

    # 信号执行
    def choose_theme_color(self):   #主题色选取
        color_panel = qfluentwidgets.ColorDialog(PyQt5.QtGui.QColor("#66CCFF"),"选择主题色",self.window(),enableAlpha=False)
        color_panel.colorChanged.connect(self.update_theme_color)
        if color_panel.exec():
            print("[Debug|Info]用户选择的主题色:", self.theme_color.name())
        else:
            print("[Debug|Info]用户取消了主题色选择")

    def update_theme_color(self,color:PyQt5.QtGui.QColor):    #更新主题色
        self.theme_color = color
        print("[Debug|Info]当前应用的主题色:", self.theme_color.name())
        qfluentwidgets.setThemeColor(self.theme_color.name())
        self.save_theme_color_to_config(self.theme_color.name())

    def save_theme_color_to_config(self, color_str: str):   #写入配置文件
        current_dir = os.path.dirname(os.path.abspath(__file__))
        print("[Debug|Info]程序当前运行目录:",current_dir)
        config_path = os.path.join(current_dir, '../..', 'Config.py')
        print("[Debug|Info]Config配置文件目录:",config_path)
        config_path = os.path.normpath(config_path)