from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout


class HomePage(QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("HomePage")

        # 原有布局代码
        self.label = QLabel("欢迎页内容", self)
        layout = QVBoxLayout(self)
        layout.addWidget(self.label)