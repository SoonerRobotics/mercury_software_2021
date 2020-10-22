###
# "Robot" sending data to computer "Server"
# Integrated with GUI.
###

import cv2, socket, pickle, struct
import numpy as np

def main():
    # Webcam on
    videoFeed = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

        # setting up the socket
        s.bind(("0.0.0.0", 25565))
        s.listen()

        connection, address = s.accept()

        while True:
            # camera feed
            _, frame = videoFeed.read()
            frame = cv2.resize(frame, (640, 480))

            # encoding/compressing numpy array from "frame"
            data = pickle.dumps(frame)

            dataSize = len(data)

            # encodes the size of the data
            encodedSize = struct.pack("Q", dataSize)

            # sends size of data and data itself over the socket
            connection.sendall(encodedSize + data)

if __name__ == "__main__":
    main()