from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
import cv2
import qimage2ndarray
import sys
from multiprocessing import Process

#from CameraFeedNetwork import CamServer


def main():
    print("SHIT")

    def displayFrame():
        ret, frame = cap.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image = qimage2ndarray.array2qimage(frame)
        label.setPixmap(QPixmap.fromImage(image))

    app = QApplication([])
    window = QWidget()

    # OPENCV
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

    # timer for getting frames
    timer = QTimer()
    timer.timeout.connect(displayFrame)
    timer.start(60)
    label = QLabel('No Camera Feed')
    button = QPushButton("Quiter")
    button.clicked.connect(sys.exit) # quiter button
    layout = QVBoxLayout()
    layout.addWidget(button)
    layout.addWidget(label)
    window.setLayout(layout)
    window.show()
    app.exec_()

#if __name__ == "__main__":
#    print(CamServer.main() + "\n NEW LINE \n")
    #main()