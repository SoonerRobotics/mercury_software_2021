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

            tankMode = False

            while True:

                dataBytes = connection.recv(4096)

                if len(dataBytes) == 0:
                    break

                dict = pickle.loads(dataBytes)
                print(dict)

                if (dict["tank"] == 1 and tankMode):
                    print("NOT TANK TIME :(")
                    tankMode = False
                    time.sleep(0.5)

                elif (dict["tank"] == 1 and not tankMode):
                    print("TANK TIME :)")
                    tankMode = True
                    time.sleep(0.5)

                if (tankMode):
                    leftPower = -filter(dict["left_y"])
                    rightPower = -filter(dict["right_y"])
                else:
                    leftPower = (filter(dict["left_y"]) - filter(dict["left_x"]))
                    rightPower = (filter(dict["left_y"]) + filter(dict["left_x"]))

                # test_pkt = struct.pack('<cffc', b'\r', dict["left_y"], dict["right_y"], b'\n')
                test_pkt = struct.pack('<cffc', b'\r', leftPower, rightPower, b'\n')


                sObj.write(test_pkt)


                returned = sObj.read(64)

                #time.sleep(0.25)


if __name__ == "__main__":
    controllerServer()