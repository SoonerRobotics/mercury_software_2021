###
# "Computer" that the robot "Server" will send camera data to.
# Integrated with GUI.
# Gotta love stack overflow
###

import cv2, socket, pickle, struct
import pygame
import json
import keyboard
import numpy as np
import time

#frame = cv2.imread("frame.png")

pygame.init()
clock = pygame.time.Clock()
pygame.joystick.init()

def filter(dict):
    for direction in dict:
        #print(direction)
        if (abs(dict[direction]) < 0.1):
            dict[direction] = 0

        #removed left_y
        if (direction == "right_y"):
            dict[direction] = -1 * dict[direction]

    return dict

def getControllerInput():
    dict = {}

    done = False

    count = 0

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.JOYBUTTONDOWN:
                print("Joystick button pressed.")
            elif event.type == pygame.JOYBUTTONUP:
                print("Joystick button released.")

        joystick_count = pygame.joystick.get_count()
        for i in range(joystick_count):
            joystick = pygame.joystick.Joystick(i)
            joystick.init()

            # Joysticks
            axes = joystick.get_numaxes()
            axis = []
            for i in range(axes):
                axis.append(float('%.3f' % (joystick.get_axis(i))))
            # print(axis)

            dict = {"left_x": axis[0],
                    "left_y": axis[1],
                    "right_x": axis[2],
                    "right_y": axis[3]}

            # Buttons
            buttons = joystick.get_numbuttons()
            button = []
            for i in range(buttons):
                button.append(joystick.get_button(i))
            # print(button)

            # Hats
            hats = joystick.get_numhats()
            hat = []
            for i in range(hats):
                hat.append(joystick.get_hat(i))
            # print(hat)

            #print(dict)

        clock.tick(150)

        #with open("sample.json", "w") as outfile:
        #    json.dump(dict, outfile)

        count = count + 1

        if count == 2:
            return dict



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
            # will read from .dib file
            cv2.imwrite("frame.dib", frame)

            #time.sleep(0.01)
            #return frame

            cv2.imshow("videoFeed", frame)
            cv2.waitKey(1)

            # parses the controller input and sends it to the robot (server)
            controllerInput = getControllerInput()
            data = pickle.dumps(filter(controllerInput))

            s.sendall(data)

if __name__ == "__main__":
      main()
