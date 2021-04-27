import lapReceiving
import lapSending
import pygame

class XboxButtons(Enum):
    A = 0
    B = 1
    X = 2
    Y = 3
    LB = 4
    RB = 5
    BACK = 6
    START = 7
    LJOY = 8
    RJOY = 9

class XboxAxes(Enum):
    LX = 0
    LY = 1
    T = 2 #Analog triggers, right side negative - result is sum of them (-1, 1)
    RX = 3
    RY = 4

def init():
    pygame.init()
    lapSending.init()
    lapReceiving.init()
    # TODO: Set Receiving up so that it will work automatically
    # TODO: Set Sending up so that it will work automatically
    joystick = pygame.joystick.Joystick(0)
    joystick.init()

def readController():
    # TODO: Code to collect the current state of the controller

# TODO: UI Functions

def quit():
    pygame.quit()
    lapSending.quit()
    lapReceiving.quit()

# TODO: Code to actually run things, not just functions