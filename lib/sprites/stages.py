__author__ = 'marcman'

import pygame
from lib.sprites.balloon import Balloon

class Stages(object):

    def __init__(self):
        self.targets = pygame.sprite.RenderUpdates()
        self.stagenumber = 1
        self.finished = 1

    def render(self, event, screen):

        #create monsters
        if self.finished:
            self.finished = 0

            if self.stagenumber == 1:
                self.targets.add(Balloon('RED', x * 30 + 300, 600) for x in range(15))
            elif self.stagenumber == 2:
                self.targets.add(Balloon('YELLOW', x * 30 + 300, 600) for x in range(15))

        #check for targets out of range
        for m in self.targets:
            if m.get_y() > 1000 and m.get_shotstatus() == 1:
                self.targets.remove(m)

        #check if level already finished
        if len(self.targets) == 0:
            #level+=1
            self.finished = 1

        #render all targets
        self.targets.draw(screen)
        self.targets.update()