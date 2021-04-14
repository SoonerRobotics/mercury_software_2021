import socket
import pickle
import json
import os

def controllerClient():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(("127.0.0.1", 25565))

        while True:
            #dict = {"first": random.randint(0,10), "second": random.randint(0,10), "third": random.randint(0,10)}

            with open('axis.json') as axisFile:
                dict = json.load(axisFile)

            #print("file: " + str(dict))

            data = pickle.dumps(dict)

            s.sendall(data)



#if __name__ == "__main__":
#    controllerClient()