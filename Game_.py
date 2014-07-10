# !/usr/bin/python
"""
Created on Thu Apr 4 08:37 2013

@author: marcel
"""

import pygame
from pygame.locals import *
from lib.sprites.balloon import Balloon
from lib.sprites.tilemap import Tilemap


def main():
    #initialize pygame modules and create windows
    pygame.init()
    screen = pygame.display.set_mode((800, 600))

    pygame.display.set_caption('Bow & Arrows')
    pygame.mouse.set_visible(1)


    #clock object to set framerate
    clock = pygame.time.Clock()

    level = 1
    level_finished = 1

    # create tilemap
    map = Tilemap()

    collides = pygame.sprite.RenderUpdates()

    #arrows = pygame.sprite.RenderUpdates()
    monsters = pygame.sprite.RenderUpdates()


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

            """
            #collisiondetection
            for m in monsters:
                for a in arrows:
                    #inaccurate for balloons - subtract 70 see Arrow init
                    if pygame.sprite.collide_rect(a, m):
                        #if m.rect.collidepoint(a.get_x, a.get_y):
                        m.set_shot()"""

        monsters.draw(screen)
        monsters.update()

        map.render(event, screen)

        pygame.display.flip()

        #monsters out of boarder deletion
        for m in monsters:
            if m.get_y() > 1000 and m.get_shotstatus() == 1:
                monsters.remove(m)

        if len(monsters) == 0:
            #level+=1
            level_finished = 1

        #levelgeneration only once
        if level_finished:

            level_finished = 0

            #stages_start(level)

            if level == 1:
                #15 red balloons
                monsters.add(Balloon('RED', x * 30 + 300, 600) for x in range(15))
            elif level == 2:
                pass
                #3 yellow
                #11 red
            elif level == 3:
                pass
            elif level == 4:
                pass
            elif level == 5:
                pass
            elif level == 6:
                pass
            elif level == 7:
                pass
            elif level == 8:
                pass
            elif level == 9:
                pass


if __name__ == '__main__':
    main()
