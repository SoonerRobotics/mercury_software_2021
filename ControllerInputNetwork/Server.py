import socket
import json
import struct
import pickle
from multiprocessing import Process
import os

import time


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

                time.sleep(2)


if __name__ == "__main__":
    controllerServer()