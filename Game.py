# !/usr/bin/python
"""
Created on Thu Apr 4 08:37 2013

@author: marcel
"""

import pygame
from pygame.locals import *

from lib.tilemap import Tilemap


def main():
    # initialize pygame modules and create windows
    pygame.init()
    screen = pygame.display.set_mode((800, 600))

    pygame.display.set_caption('Bow & Arrows')
    pygame.mouse.set_visible(1)

    #clock object to set framerate
    clock = pygame.time.Clock()

    # create tilemap
    map = Tilemap()

    #gameloop
    keepgoing = True
    while keepgoing:

        clock.tick(60)

        screen.fill((0, 128, 1))

        for event in pygame.event.get():
            if event.type == QUIT:
                keepgoing = False
                break
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    keepgoing = False
                    break

            map.handle_input(event)

        map.render(event, screen)

        pygame.display.flip()


if __name__ == '__main__':
    main()
