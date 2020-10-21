import cv2, socket, pickle, struct
import numpy as np


videoFeed = cv2.VideoCapture(0, cv2.CAP_DSHOW)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(("127.0.0.1", 25565))

    while True:
        _, frame = videoFeed.read()

        # encoding numpy array from "frame"
        data = pickle.dumps(frame)

        dataSize = len(data)

        # encodes the size of the data
        encodedSize = struct.pack("Q", dataSize)

        # sends size of data and data itself over the socket
        s.sendall(encodedSize + data)


#https://stackoverflow.com/questions/30988033/sending-live-video-frame-over-network-in-python-opencv