###
# "Computer" that the robot "Server" will send camera data to.
# Gotta love stack overflow
###

import cv2, socket, pickle, struct
import numpy as np
import time

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        dataBytes = b''

        # used for finding data size from encoded data
        loadSize = struct.calcsize("Q")

        # normal socket stuff
        s.connect(("127.0.0.1", 25565))
        print("socket ready")

        while True:

            # scraping the data size from encoded socket connection
            while (len(dataBytes) < loadSize):
                dataBytes += s.recv(4096)

            # decoding the data about data size
            dataSize = struct.unpack("Q", dataBytes[:loadSize])[0]

            # disregard dataSize, now ready for encoded data
            dataBytes = dataBytes[loadSize:]

            # keeps on receiving data until it hits the "pre-written" data size
            while (len(dataBytes) < dataSize):
                dataBytes += s.recv(4096)

            # separating encoded data itself from any extra stuff sent over
            frameData = dataBytes[:dataSize]
            dataBytes = dataBytes[dataSize:]

            # extracting frame from compression/encoding
            frame = pickle.loads(frameData)

            # because it would socket crash if function would return anything,
            # could not directly connect the "frame" to the "GUI." As a result,
            # I just had it constantly write the frame to a file, which would be parse
            # by the GUI
            cv2.imwrite("frame.jpg", frame)

            #time.sleep(0.01)
            #return frame

            cv2.imshow("videoFeed", frame)
            cv2.waitKey(1)

if __name__ == "__main__":
      main()