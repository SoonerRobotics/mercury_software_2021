import serial
import struct
import time
import pygame

sObj = serial.Serial("COM5", 9600, timeout=0.05)
pygame.init()
clock = pygame.time.Clock()
pygame.joystick.init()

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


        test_pkt = struct.pack('<cffc', b'\r', -dict["left_y"], -dict["right_y"], b'\n')

        sObj.write(test_pkt)
        returned = sObj.read(64)
