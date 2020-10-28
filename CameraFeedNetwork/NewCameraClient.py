###
# "Computer" that the robot "Server" will send camera data to.
# Integrated with GUI.
# Gotta love stack overflow
###

import cv2, socket, pickle, struct
import keyboard
import numpy as np
import time

#frame = cv2.imread("frame.png")

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        dataBytes = b''

        # used for finding data size from encoded data
        loadSize = struct.calcsize("Q")

        # normal socket stuff
        s.connect(("127.0.0.1", 25565))
        print("socket ready")

        while True:

            #s.sendall(str(keyboard.read_key()).encode())

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
            #global frame
            frame = pickle.loads(frameData)

            # In GUI, I have multi-processing for making GUI and receiving camera data. Because
            # they are separate processes, having the camera-data-frame be a global would not work.
            # As a result, camera data will be written to a .dib file (so it doesn't stutter) and GUI
            # will read from GUI file
            cv2.imwrite("frame.dib", frame)

            #time.sleep(0.01)
            #return frame

            cv2.imshow("videoFeed", frame)
            cv2.waitKey(1)

if __name__ == "__main__":
      main()