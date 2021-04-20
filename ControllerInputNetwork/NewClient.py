import socket
import pickle
import json
import os

#https://www.chiefdelphi.com/t/control-all-driving-with-one-joystick/88500/7

import pygame

def filter(dict):
    for direction in dict:
        #print(direction)
        if (abs(dict[direction]) < 0.1):
            dict[direction] = 0

        #removed left_y
        if (direction == "right_y" or direction == "left_y"):
            dict[direction] = -1 * dict[direction]

    return dict

def controllerClient():
    pygame.init()
    clock = pygame.time.Clock()
    pygame.joystick.init()

    done = False

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(("192.168.1.59", 25565))

        while True:

            dict = {}

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
                #print(axis)

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

                dict = {"tank" : button[4],
                        "left_x": axis[0],
                        "left_y": axis[1],
                        "right_x": axis[2],
                        "right_y": axis[3]}

            clock.tick(15)

            data = pickle.dumps(filter(dict))

            s.sendall(data)



if __name__ == "__main__":
    controllerClient()