import serial
import struct
import time
import pygame

sObj = serial.Serial("COM5", 9600, timeout=0.05)
pygame.init()
clock = pygame.time.Clock()
pygame.joystick.init()
joystick = pygame.joystick.Joystick(0)

isTank = True

def filter(x):
    if abs(x) < 0.1:
        x = 0
    return x

while True:
    leftPower = 0
    rightPower = 0

    if (joystick.get_button(4) == 1 and isTank):
        print("NOT TANK TIME :(")
        isTank = False
        time.sleep(0.5)

    elif (joystick.get_button(4) == 1 and not isTank):
        print("TANK TIME :)")
        isTank = True
        time.sleep(0.5)

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

        #time.sleep(0.25)

        if (isTank):
            leftPower = filter(dict["left_y"])
            rightPower = -filter(dict["right_y"])
        else:
            leftPower = (filter(dict["left_y"]) - filter(dict["left_x"]))
            rightPower = -1 * (filter(dict["left_y"]) + filter(dict["left_x"]))

        #test_pkt = struct.pack('<cffc', b'\r', dict["left_y"], -dict["right_y"], b'\n')
        test_pkt = struct.pack('<cffc', b'\r', leftPower, rightPower, b'\n')

        sObj.write(test_pkt)
        returned = sObj.read(64)