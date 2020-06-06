import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class MazeWindow(QWidget):
    def __init__(self):
        super(MazeWindow, self).__init__()

        self.resize(1200, 700)
        self.setWindowTitle("GUI 测试")
        # self.setObjectName("MainWindow")
        # self.setStyleSheet("#MainWindow{background-color: black}")
        # self.setStyleSheet("#MainWindow{border-image:url(./img/5.jpg);}")
        
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap("./img/7.jpg")))
        self.setPalette(palette)

        self.label1 = QLabel(self)
        self.label1.setFixedSize(500, 500)
        self.label1.move(50, 70)

        self.label1.setStyleSheet("QLabel{background:white;}"
                                 "QLabel{color:rgb(0,0,0,120);font-size:25px;font-weight:bold;font-family:宋体;}")
        self.label2 = QLabel(self)
        self.label2.setFixedSize(500, 500)
        self.label2.move(650, 70)

        self.label2.setStyleSheet("QLabel{background:white;}"
                                 "QLabel{color:rgb(0,0,0,120);font-size:25px;font-weight:bold;font-family:宋体;}")

        btn1 = QPushButton(self)
        btn1.setText("导入迷宫图片")
        btn1.move(100, 635)
        btn1.resize(180,45)
        btn1.clicked.connect(self.input_image)

        btn2 = QPushButton(self)
        btn2.setText("执行并显示结果")
        btn2.move(900, 635)
        btn2.resize(180,45)
        btn2.clicked.connect(self.input_image)

        self.show()

    def input_image(self):

        imgName, imgType = QFileDialog.getOpenFileName(self, "浏览", "", "*.jpg;;*.png;;All Files(*)")
        image = QtGui.QPixmap(imgName).scaled(self.label1.width(), self.label1.height())
        self.label1.setPixmap(image)
    
    def closeEvent(self, event):
        
        reply = QMessageBox.question(self, 'Message',
            "确定退出?", QMessageBox.Yes | 
            QMessageBox.No, QMessageBox.No)
 
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()  


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    test = MazeWindow()
    sys.exit(app.exec_())