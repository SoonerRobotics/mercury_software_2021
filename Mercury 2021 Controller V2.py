#Version 2.0

import math
import pygame

pygame.init()
clock = pygame.time.Clock()
pygame.joystick.init()

DEAD_ZONE_Y = 0.15

done = False
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

        #Joysticks
        axes = joystick.get_numaxes()
        axis = []
        for i in range(axes):
            axis.append(float('%.3f'% (joystick.get_axis(i))))
            if abs(axis[i]) < DEAD_ZONE_Y:
                axis[i] = 0
        #print(axis)
          
        #Buttons
        buttons = joystick.get_numbuttons()
        button = []
        for i in range(buttons):
            button.append(joystick.get_button(i))
        print(button)
            
        #Hats
        hats = joystick.get_numhats()
        hat = []
        for i in range(hats):
            hat.append(joystick.get_hat(i))
        #print(hat)
        
        if (joystick.get_button(7) == 1):
            done = True
            pygame.quit()
            break
        

    clock.tick(20)

print("program done")
