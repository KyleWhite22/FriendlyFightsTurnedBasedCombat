import pygame
from pygame.locals import *

# Initialize Pygame
pygame.init()

# Check for connected joysticks
joystick_count = pygame.joystick.get_count()
if joystick_count == 0:
    print("No joysticks found")
    pygame.quit()
    quit()

# Initialize joystick
joystick = pygame.joystick.Joystick(0)  # Assuming the first joystick is the Xbox controller
joystick.init()

try:
    while True:
        # Get joystick events
        for event in pygame.event.get():
            if event.type == JOYAXISMOTION:
                # Read the axis motion (left stick)
                if event.axis == 0:  # X-axis of left stick
                    if event.value > 0.5:
                        print("Left")
                    elif event.value < -0.5:
                        print("Right")
                elif event.axis == 1:  # Y-axis of left stick
                    if event.value > 0.5:
                        print("Down")
                    elif event.value < -0.5:
                        print("Up")

        # Limit the frame rate
        pygame.time.Clock().tick(30)

except KeyboardInterrupt:
    print("Exiting...")
    pygame.quit()
    quit()