import socket
import json
import struct
import pickle
import serial
from multiprocessing import Process
import os

import time


sObj = serial.Serial("COM5", 9600, timeout=0.05)

def controllerServer():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        dataBytes = b''

        s.bind(("0.0.0.0", 25565))
        s.listen()

        connection, address = s.accept()

        print("testing")

        with connection:
            print("client connected. ip is: ", address)

            while True:

                dataBytes = connection.recv(4096)

                if len(dataBytes) == 0:
                    break

                dict = pickle.loads(dataBytes)
                print(dict)

                test_pkt = struct.pack('<cffc', b'\r', dict["left_y"], dict["right_y"], b'\n')

                sObj.write(test_pkt)


                returned = sObj.read(64)

                #time.sleep(0.25)


if __name__ == "__main__":
    controllerServer()