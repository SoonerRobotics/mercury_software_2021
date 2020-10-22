###
#  Deprecated.
###

import cv2, socket, pickle, struct
import numpy as np

def main():
    videoFeed = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(("127.0.0.1", 25565))

        while True:
            _, frame = videoFeed.read()
            frame = cv2.resize(frame, (640, 480))

            # encoding numpy array from "frame"
            data = pickle.dumps(frame)

            dataSize = len(data)

            # encodes the size of the data
            encodedSize = struct.pack("Q", dataSize)

            # sends size of data and data itself over the socket
            s.sendall(encodedSize + data)

if __name__ == "__main__":
    main()