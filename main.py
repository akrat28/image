import os

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
        # 输入按钮
        self.shuru.clicked.connect(self.choose_folder)
        # 输出按钮
        self.shucu.clicked.connect(self.manage_output)
        # 转换按钮
        self.zhuan.clicked.connect(self.convert)
        # 删除按钮
        self.shanchu.clicked.connect(self.sc)
        # 删除路径按钮
        self.lujin.clicked.connect(self.choose_folder)
        # 修改名称
        self.xiugai_name.clicked.connect(self.name)

    shuchulujin = None

    def choose_folder(self):
        # 路径输出
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.folder_path = QFileDialog.getExistingDirectory(self, "Choose Folder", options=options)

        if self.folder_path:
            print("输入:", self.folder_path)
        global shuchulujin
        shuchulujin = self.folder_path

    def manage_output(self):
        # 路径输出
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.output_path = QFileDialog.getExistingDirectory(self, "Choose Folder", options=options)

        if self.output_path:
            print("输出:", self.output_path)

    def convert(self):
        # 获取文本框的内容
        text_content = self.txt.text()
        print("文本内容:", text_content)
        a = fileprocess.lujin(self.folder_path)
        # print(a)
        # a[0]所有图片的名称 a[1]路径长度
        fileprocess.zhuanhuan(a[0], a[1], self.output_path, text_content)

    def name(self):
        text_content = self.txt.text()
        print("文本内容:", text_content)
        print("文件夹路径："+shuchulujin)
        fileprocess.rename_files_to_numbers(shuchulujin,int(text_content))

    def sc(self):
        # 删除
        text_content = self.txt.text()
        print("删除中")
        a = fileprocess.lujin(self.folder_path)
        fileprocess.shanchu(a[0], text_content)



if __name__ == '__main__':
    app = QApplication([])
    window = MyMainWindow()
    window.show()
    app.exec_()
