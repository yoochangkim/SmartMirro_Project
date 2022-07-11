import cv2
import threading
import sys
from PyQt5 import QtWidgets, QtGui, QtCore
import pjt_layout


running = False

class Cam():
    def run():
        global running
        cap = cv2.VideoCapture(1)
        #width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        #height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        #label.resize(width,height)
        while running:
            ret,img = cap.read()
            if ret:
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                h,w,c = img.shape
                qImg = QtGui.QImage(img.data, w, h, w*c, QtGui.QImage.Format_RGB888)
                pixmap = QtGui.QPixmap.fromImage(qImg)
                label.setPixmap(pixmap)
            else:
                QtWidgets.QMessageBox.about(win, "Error", "Cannot read frame.")
                print("cannot read frame.")
                break
        cap.release()
        print("Thread end.")


    def stop():
        global running
        running = False
        print("stoped..")

    def start():
        global running
        running = True
        th = threading.Thread(target=run)
        th.start()
        print("started..")

    def onExit():
        print("exit")
        stop()