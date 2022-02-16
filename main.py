#Importing libraries and modules
import pygame
from pygame.locals import *
import sys

#Constants
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

#Classes and functions



#Main function
def main():
    pygame.init()
    #Creating the window and setting the title
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Ping!Pong!")

    #Main loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

if __name__ == "__main__":
    main()