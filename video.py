import cv2
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from threading import Thread
import time


class video(QObject):
    sendImage = pyqtSignal(QImage)

    def __init__(self, widget, size):
        super().__init__()
        self.widget = widget
        self.size = size
        self.sendImage.connect(self.widget.recvImage)

    def startCam(self):
        try:
            self.cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        except Exception as e:
            print('Cam Error : ', e)
        else:
            self.bThread = True
            self.thread = Thread(target=self.threadFunc)
            self.thread.start()

    def stopCam(self):
        self.bThread = False
        bopen = False
        try:
            bopen = self.cap.isOpened()
        except Exception as e:
            print('Error cam not opened')
        else:
            self.cap.release()

    def threadFunc(self):
        while self.bThread:
            ret, img = self.cap.read()
            if ret:
                # detect image
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                h, w, ch = img.shape
                bytesPerLine = ch * w
                qimg = QImage(img.data, w, h, bytesPerLine, QImage.Format_RGB888)
                #resizedImg = img.scaled(self.size.width(), self.size.height(), Qt.KeepAspectRatio)
                #self.sendImage.emit(resizedImg)
                self.sendImage.emit(qimg)
            else:
                print('cam read errror')

            time.sleep(0.01)

        print('thread finished')