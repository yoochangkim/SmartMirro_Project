import sys
from PyQt5.QtWidgets import *
from video import *
from PyQt5 import QtWidgets, QtGui, QtCore


QtWidgets.QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)

QSize
class CWidget(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        size = QSize(1080, 600)
        self.initUI(size)
        #self.video = video(self, QSize(self.frm.width(), self.frm.height()))
        self.video = video(self, QSize(640,480))

    def initUI(self, size):
        vbox = QVBoxLayout()

        # cam on, off button
        #self.btn = QPushButton('Camera ON', self)
        #self.btn.setCheckable(True)
        #self.btn.clicked.connect(self.onoffCam)
        #vbox.addWidget(self.btn)

        # kind of detection
        txt = ['full body', 'upper body', 'lower body', 'face', 'eye', 'eye glass', 'smile']
        #self.grp = QtWidgets.QButtonGroup(self)
        self.grp = QtWidgets.QButtonGroup(self)
        for i in range(len(txt)):
            btn = QCheckBox(txt[i], self)
            self.grp.addButton(btn, i)
            vbox.addWidget(btn)
        vbox.addStretch(1)
        self.grp.setExclusive(False)
        self.grp.buttonClicked[int].connect(self.detectOption)
        self.bDetect = [False for i in range(len(txt))]

        self.pushButton = QPushButton('CAM ON', self)
        #self.pushButton.setGeometry(QtCore.QRect(110, 520, 80, 40))
        self.pushButton.setCheckable(True)
        self.pushButton.clicked.connect(self.onoffCam)
        vbox.addWidget(self.pushButton)
        #self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(self)
        #self.pushButton_2.setGeometry(QtCore.QRect(200, 520, 80, 40))
        vbox.addWidget(self.pushButton_2)
        #self.pushButton_2.setObjectName("pushButton_2")

        # video area
        self.frm = QLabel(self)
        self.frm.setFrameShape(QFrame.Panel)

        hbox = QHBoxLayout()
        hbox.addLayout(vbox)
        hbox.addWidget(self.frm, 1)
        self.setLayout(hbox)

        #self.setFixedSize(size)
        #self.move(100, 100)
        self.setWindowTitle('TEST')
        self.show()

    def onoffCam(self, e):
        if self.pushButton.isChecked():
            self.pushButton.setText('Camera Off')
            self.video.startCam()
        else:
            self.pushButton.setText('Camera On')
            self.video.stopCam()

    def detectOption(self, id):
        if self.grp.button(id).isChecked():
            self.bDetect[id] = True
        else:
            self.bDetect[id] = False
        # print(self.bDetect)
        self.video.setOption(self.bDetect)

    def recvImage(self, img):
        self.frm.setPixmap(QPixmap.fromImage(img))

    def closeEvent(self, e):
        self.video.stopCam()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = CWidget()
    sys.exit(app.exec_())