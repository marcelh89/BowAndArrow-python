# !/usr/bin/python
"""
Created on Thu Apr 4 08:37 2013

@author: marcel
"""

import pygame as pg
from pygame.locals import *

from data.tilemap import Tilemap


def main():
    # initialize pygame modules and create windows
    pg.init()
    screen = pg.display.set_mode((800, 600))

    pg.display.set_caption('Bow & Arrows')
    pg.mouse.set_visible(1)

    #clock object to set framerate
    clock = pg.time.Clock()

    # create tilemap
    map = Tilemap()

    #gameloop
    keepgoing = True
    while keepgoing:

        clock.tick(60)

        screen.fill((0, 128, 1))

        for event in pg.event.get():
            if event.type == QUIT:
                keepgoing = False
                break
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    keepgoing = False
                    break

            map.handle_input(event)

        map.render(event, screen)

        pg.display.flip()


if __name__ == '__main__':
    main()
