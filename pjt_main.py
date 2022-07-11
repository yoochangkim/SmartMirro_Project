import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
#from PyQt5.QtWidgets import QFileDialog, QMainWindow, QAction, QProgressBar, QApplication
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from video import *
from cam import Cam

form_class = uic.loadUiType("test.ui")[0]

class MainWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pixmap = QtGui.QPixmap('face.jpg')
        self.label_pic.setPixmap(self.pixmap)
        self.video = video(self,QSize(640,480))
        self.pushButton_13.setCheckable(True)
        self.pushButton_13.clicked.connect(self.onoffCam)
        
    def recvImage(self, img):
        self.camView.setPixmap(QPixmap.fromImage(img))
    
    def closeEvent(self, e):
        self.video.stopCam()
        
    def onoffCam(self, e):
        if self.pushButton_13.isChecked():
            self.pushButton_13.setText('CAM OFF')
            self.video.startCam()
        else:
            self.pushButton_13.setText('CAM ON')
            self.video.stopCam()


if __name__ == '__main__':
    app = QApplication(sys.argv) # 프로그램 실행 클래스
    myWindow = MainWindow() # 객체 생성
    myWindow.show() # 프로그램 화면 출력
    sys.exit(app.exec_()) # 프로그램 종료