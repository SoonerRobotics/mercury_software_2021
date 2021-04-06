import socket
import json
import struct
import pickle
from multiprocessing import Process
from ControllerInputNetwork import Client


def controllerServer():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        dataBytes = b''

        s.bind(("0.0.0.0", 25565))
        s.listen(1000)

        connection, address = s.accept()

        with connection:
            print("client connected. ip is: ", address)

            while True:

                dataBytes += connection.recv(1024)
                dict = pickle.loads(dataBytes)

                print(dict)

                if len(dataBytes) == 0:
                    break


if __name__ == "__main__":
    print("test")
    controllerServer()
