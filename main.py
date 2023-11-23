from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.uic import loadUi
import fileprocess


# from mainwindow import Ui_MainWindow

class MyMainWindow(QMainWindow):
    def __init__(self):
        super(MyMainWindow, self).__init__()

        # Load the UI file
        loadUi('mainwindow.ui', self)

        # Connect button signals to slots
        self.shuru.clicked.connect(self.choose_folder)
        self.shucu.clicked.connect(self.manage_output)
        self.zhuan.clicked.connect(self.convert)
        self.shanchu.clicked.connect(self.sc)
        self.lujin.clicked.connect(self.choose_folder)


    def choose_folder(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.folder_path = QFileDialog.getExistingDirectory(self, "Choose Folder", options=options)

        if self.folder_path:
            print("输入:", self.folder_path)

    def manage_output(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.output_path = QFileDialog.getExistingDirectory(self, "Choose Folder", options=options)

        if self.output_path:
            print("输出:", self.output_path)

    def convert(self):
        # 获取文本框的内容
        text_content = self.txt.text()
        print("Text Content:", text_content)
        a = fileprocess.lujin(self.folder_path)
        # print(a)
        fileprocess.zhuanhuan(a[0], a[1], self.output_path, text_content)

    def sc(self):
        text_content = self.txt.text()
        print("删除中")
        a = fileprocess.lujin(self.folder_path)
        fileprocess.shanchu(a[0], text_content)


if __name__ == '__main__':
    app = QApplication([])
    window = MyMainWindow()
    window.show()
    app.exec_()
