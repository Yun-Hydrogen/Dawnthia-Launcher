from PyQt5.QtWidgets import QWidget
from UIs.Ui_Tools import Ui_Tools
from qfluentwidgets import FluentIcon, TeachingTip, InfoBarIcon, MessageBox,PrimaryPushButton, PopupTeachingTip,TeachingTipView, TeachingTipTailPosition
import subprocess
from PyQt5.QtCore import Qt

class Tools(QWidget, Ui_Tools):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("Tools")
        self.setupUi(self)

        # 设置图标
        self.TransparentToolButton_1.setIcon(FluentIcon.INFO)
        self.PrimaryPushButton_1.setIcon(FluentIcon.VPN)
        self.PushButton_1.setIcon(FluentIcon.CANCEL)

        # 按键绑定
        self.TransparentToolButton_1.clicked.connect(self.TransparentToolButton_1_Clicked)
        self.PrimaryPushButton_1.clicked.connect(self.PrimaryPushButton_1_Clicked)
        self.PushButton_1.clicked.connect(self.PushButton_1_Clicked)

    # 按键绑定函数(悬浮窗事件)
    def TransparentToolButton_1_Clicked(self):
        TeachingTip.create(self.TransparentToolButton_1,
                           "工作原理",
                           "在HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\Dwm\n"
                           "新增一个 OverlayTestMode 的DWORD 项，值为 5\n\
                            可能与多平面覆盖（MPO）有关，若要卸载将键值删除即可",
                           isClosable=True,
                           duration=-1,
                           icon=InfoBarIcon.INFORMATION)

    # 按键绑定函数(操作事件)
    def PrimaryPushButton_1_Clicked(self):
        reg = r'reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\Dwm" /v OverlayTestMode /t REG_DWORD /d 5 /f'
        powershell = f'powershell -Command "Start-Process cmd -ArgumentList \'/c {reg}\' -Verb RunAs"'
        try:
            result = subprocess.run(powershell, shell=True, check=True, capture_output=True, text=True)
            mb = MessageBox("操作已完成o((>ω< ))o","已成功向注册表添加键值\n请重新启动已应用更改。",self.window())
            mb.yesButton.setText("现在重启")
            mb.cancelButton.setText("稍后重启")
            if mb.exec():
                subprocess.run("shutdown -r -t 60")
            else:
                pass
        except subprocess.CalledProcessError as e:
            mb = MessageBox("操作未完成`(*>﹏<*)′",f"发生了错误：{e.stderr.strip()}",self.window())
            mb.yesButton.setText("这应该是我的问题ψ(._. )>")
            mb.cancelButton.setText("这是萌萌氢的问题，我要惩罚萌萌氢（不要啊~ヽ(*。>Д<)o゜")
            mb.exec()
        
    def PushButton_1_Clicked(self):
        ConfirmButton = PrimaryPushButton("确定")
        ConfirmButton.setFixedWidth(70)
        view = TeachingTipView(title="撤销更改",
                          content="确定要撤销更改吗？",
                          isClosable=False)
        view.addWidget(ConfirmButton)
        PopupTeachingTip.make(
            target = self.PushButton_1,
            view = view,
            duration = -1,
            tailPosition = TeachingTipTailPosition.LEFT,
            parent=self
        )
        ConfirmButton.clicked.connect(self.ConfirmButton_Clicked)
    
    def ConfirmButton_Clicked(self):
        reg = r'reg delete "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\Dwm" /v OverlayTestMode /f'
        powershell = f'powershell -Command "Start-Process cmd -ArgumentList \'/c {reg}\' -Verb RunAs"'
        try:
            result = subprocess.run(powershell, shell=True, check=True, capture_output=True, text=True)
            mb = MessageBox("操作已完成o((>ω< ))o", "已成功从注册表删除键值\n请重新启动以应用更改。", self.window())
            mb.yesButton.setText("现在重启")
            mb.cancelButton.setText("稍后重启")
            if mb.exec():
                subprocess.run("shutdown -r -t 60")
            else:
                pass
        except subprocess.CalledProcessError as e:
            mb = MessageBox("操作未完成`(*>﹏<*)′", f"发生了错误：{e.stderr.strip()}", self.window())
            mb.yesButton.setText("这应该是我的问题ψ(._. )>")
            mb.cancelButton.setText("这是萌萌氢的问题，我要惩罚萌萌氢（不要啊~ヽ(*。>Д<)o゜")
            mb.exec()