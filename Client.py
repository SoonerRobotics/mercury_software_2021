
import socket
import random
import pickle
import struct
import json

def controllerClient():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(("127.0.0.1", 25565))

        while True:
            dict = {"first": random.randint(0,10), "second": random.randint(0,10), "third": random.randint(0,10)}
            data = pickle.dumps(dict)

            s.sendall(data)

if __name__ == "__main__":
    controllerClient()