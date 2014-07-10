__author__ = 'marcman'

from lib.sprites.balloon import Balloon
import pygame

class Targets(object):
    def __init__(self):
        self.monsters = pygame.sprite.RenderUpdates()
        self.level = 1
        self.level_finished = 1

    def render(self, event, screen):
        #render monsters
        self.monsters.draw(screen)
        self.monsters.update()

        #check for outdate monsters
        for m in self.monsters:
            if m.get_y() > 1000 and m.get_shotstatus() == 1:
                self.monsters.remove(m)

        if len(self.monsters) == 0:
            #level+=1
            self.level_finished = 1

        #create monsters
        if self.level_finished:

            self.level_finished = 0

            #stages_start(level)

            if self.level == 1:
                #15 red balloons
                self.monsters.add(Balloon('RED', x * 30 + 300, 600) for x in range(15))
            elif self.level == 2:
                pass