# Python game "Piton"


import pygame, sys, random, time

check_errors = pygame.init()

if check_errors[1] > 0:
    print("Had {0} initializing erros, "
          "exiting".format(check_errors[1]))
    sys.exit(-1)

else:
    print("PyGame successfully initialized!")

# Play surface
playSurface = pygame.display.set_mode((720, 460))
pygame.display.set_caption('Piton')
time.sleep(5)

