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
        frame = cv2.imread("frame.dib", cv2.IMREAD_UNCHANGED)

        try:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        except (TypeError, ValueError, cv2.error) as e:
            # Note: there is this really annoying ValueError that
            # I can't catch with try-except??
            # "raise ValueError("array2qimage can only convert 2D or 3D arrays (got %d dimensions)" % _np.ndim(array))"
            pass

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

