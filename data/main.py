# !/usr/bin/python
"""
Created on Thu Apr 4 08:37 2013

@author: marcel
"""

import pygame as pg
from pygame.locals import *
from data.tilemap import Tilemap


def main():

    pg.init()
    screen = pg.display.set_mode((800, 600))

    pg.display.set_caption('Bow & Arrows')
    pg.mouse.set_visible(1)
    clock = pg.time.Clock()

    tile = Tilemap()

    loop = True
    while loop:

        clock.tick(60)

        screen.fill((0, 128, 1))

        for event in pg.event.get():
            if event.type == QUIT:
                loop = False
                break
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    loop = False
                    break

            tile.handle_input(event)

        tile.render(event, screen)

        pg.display.flip()