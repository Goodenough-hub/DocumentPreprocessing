import sys
import os
from PyQt5.QtWidgets import *
import algorithm
import shutil

class File:
    """关于关键文件的定义与操作"""
    def __init__(self, keyFile):
        self.keyFile = keyFile


class MainForm(QWidget):
    def __init__(self, name='MainForm'):
        super(MainForm, self).__init__()
        self.setWindowTitle(name)
        self.cwd = os.getcwd()  # 获取当前程序文件位置
        self.resize(780, 700)  # 设置窗体大小
        # btn 1
        self.btn_chooseDir = QPushButton(self)
        self.btn_chooseDir.setObjectName("btn_chooseDir")
        self.btn_chooseDir.setText("选择文件夹")

        # btn 2
        self.btn_chooseFile = QPushButton(self)
        self.btn_chooseFile.setObjectName("btn_chooseFile")
        self.btn_chooseFile.setText("选取文件")

        # btn 3
        self.btn_chooseMutiFile = QPushButton(self)
        self.btn_chooseMutiFile.setObjectName("btn_chooseMutiFile")
        self.btn_chooseMutiFile.setText("多文件选择")

        # btn 4
        self.btn_saveFile = QPushButton(self)
        self.btn_saveFile.setObjectName("btn_saveFile")
        self.btn_saveFile.setText("文件保存")

        # QPlainTextEdit
        self.pte = QPlainTextEdit(self)
        self.keyPte = QPlainTextEdit(self)

        # btn5 关键字筛取
        self.btn_chooseWord = QPushButton(self)
        self.btn_chooseWord.setObjectName("btn_chooseWord")
        self.btn_chooseWord.setText("筛取关键字（以、分割）")


        # 设置布局
        self.btn_chooseDir.move(350, 80)
        self.btn_chooseDir.setFixedSize(160, 60)

        self.btn_chooseFile.move(350, 160)
        self.btn_chooseFile.setFixedSize(160, 60)

        self.btn_chooseMutiFile.move(350, 240)
        self.btn_chooseMutiFile.setFixedSize(160, 60)

        self.btn_saveFile.move(350, 320)
        self.btn_saveFile.setFixedSize(160, 60)

        self.pte.move(10, 10);
        self.pte.setFixedSize(320, 500)

        self.keyPte.move(350, 400)
        self.keyPte.setFixedSize(160, 60)

        self.btn_chooseWord.move(520, 400)
        self.btn_chooseWord.setFixedSize(280, 60)

        # layout = QVBoxLayout()
        # layout.addWidget(self.btn_chooseDir)
        # layout.addWidget(self.btn_chooseFile)
        # layout.addWidget(self.btn_chooseMutiFile)
        # layout.addWidget(self.btn_saveFile)
        # self.setLayout(layout)

        # 设置信号
        self.btn_chooseDir.clicked.connect(self.slot_btn_chooseDir)
        self.btn_chooseFile.clicked.connect(self.slot_btn_chooseFile)
        self.btn_chooseMutiFile.clicked.connect(self.slot_btn_chooseMutiFile)
        self.btn_saveFile.clicked.connect(self.slot_btn_saveFile)
        self.btn_chooseWord.clicked.connect(self.slot_btn_chooseWord)

    def slot_btn_chooseDir(self):
        dir_choose = QFileDialog.getExistingDirectory(self,
                                    "选取文件夹",
                                    self.cwd) # 起始路径

        if dir_choose == "":
            print("\n取消选择")
            return

        print("\n你选择的文件夹为:")
        print(dir_choose)
        self.pte.setPlainText("你选择的文件夹为:" + dir_choose)

    def slot_btn_chooseFile(self):
        fileName_choose, filetype = QFileDialog.getOpenFileName(self,
                                                                "选取文件",
                                                                self.cwd,  # 起始路径
                                                                "PDF Files (*.pdf);;All Files (*)")  # 设置文件扩展名过滤,用双分号间隔

        if fileName_choose == "":
            print("\n取消选择")
            return

        print("\n你选择的文件为:")
        print(fileName_choose)
        print("文件筛选器类型: ", filetype)
        self.pte.setPlainText("你选择的文件为:" + fileName_choose)
        myfile.keyFile = fileName_choose

    def slot_btn_chooseMutiFile(self):
        files, filetype = QFileDialog.getOpenFileNames(self,
                                                       "多文件选择",
                                                       self.cwd,  # 起始路径
                                                       "PDF Files (*.pdf);;All Files (*)")

        if len(files) == 0:
            print("\n取消选择")
            return

        ptedata = []
        print("\n你选择的文件为:")
        for file in files:
            print(file)
            ptedata.append(file)
        print("文件筛选器类型: ", filetype)

        ptedata = algorithm.drop_repeat(ptedata)  # 去重
        myfile.keyFile = ptedata[0]  # 第一个文件设置为keyFile
        ptedatastr = ""
        for i in ptedata:
            ptedatastr += i + '\n'

        self.pte.setPlainText("你选择的文件为:" + ptedatastr)

    def slot_btn_saveFile(self):
        fileName_choose, filetype = QFileDialog.getSaveFileName(self,
                                                                "文件保存",
                                                                self.cwd,  # 起始路径
                                                                "PDF Files (*.pdf);;All Files (*)")

        if fileName_choose == "":
            print("\n取消选择")
            return

        if myfile.keyFile == ' ':
            print("当前没有选择keyFile，操作失败")
            return

        fileName_choose = fileName_choose.replace(".pdf", '')
        finalFile = fileName_choose + '-' + algorithm.cur_time() + ".pdf"

        print("\n你选择要保存的文件为:")
        print(finalFile)
        print("文件筛选器类型: ", filetype)

        self.pte.setPlainText("你选择要保存的文件为:" + finalFile)

        # 生成保存的文件

        shutil.copy(myfile.keyFile, finalFile)

    def slot_btn_chooseWord(self):
        print("筛取文件")


if __name__ == "__main__":
    myfile = File(' ')
    app = QApplication(sys.argv)
    # Lable = QLabel("初始文本")
    # Lable.show();
    mainForm = MainForm('文档预处理')
    mainForm.show()
    sys.exit(app.exec_())
