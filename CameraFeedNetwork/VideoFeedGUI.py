###
# RUN NewCameraServer.py FIRST.
###

from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
import cv2
import qimage2ndarray
import sys
from multiprocessing import Process
import numpy as np

from CameraFeedNetwork import NewCameraClient
from CameraFeedNetwork import NewCameraServer

def GUI():

    def displayFrame():

        # scrapes frame from file
        imageFrame = cv2.imread("frame.jpg")
        frame = np.ones((480, 640, 3), np.uint8)

        try:
            frame = cv2.cvtColor(imageFrame, cv2.COLOR_BGR2RGB)
        except cv2.error as e:
            # filler function for Except statement
            empty = None

        image = qimage2ndarray.array2qimage(frame)
        label.setPixmap(QPixmap.fromImage(image))

    app = QApplication([])
    window = QWidget()

    # timer for getting frames
    timer = QTimer()
    timer.timeout.connect(displayFrame)
    timer.start(60)
    label = QLabel('No Camera Feed')
    button = QPushButton("Quiter")
    button.clicked.connect(sys.exit)
    layout = QVBoxLayout()
    layout.addWidget(button)
    layout.addWidget(label)
    window.setLayout(layout)
    window.show()
    app.exec_()

if __name__ == "__main__":
    # multi-threading to get the frame information and display it on GUI

    p1 = Process(target=GUI)
    p2 = Process(target=NewCameraClient.main)

    p1.start()
    p2.start()

    p1.join()
    p2.join()

