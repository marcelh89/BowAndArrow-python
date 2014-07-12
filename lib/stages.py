__author__ = 'marcman'

import pygame
from lib.sprites.balloon import Balloon
from stage.stage_01_training import Stage01Training
from stage.stage_02_more_training import Stage02MoreTraining
from stage.stage_03_butterflies import Stage03Butterflies
from stage.stage_04_slimes import Stage04Slimes
from stage.stage_05_bullseye import Stage05Bullseye
from stage.stage_06_fires import Stage06Fires
from stage.stage_07_winds import Stage07Winds

class Stages(object):

    def __init__(self):
        self.targets = pygame.sprite.RenderUpdates()
        self.stagenumber = 4
        self.finished = 1

    def handle_targets(self):
        nr = self.stagenumber

        if nr == 1:
            stage = Stage01Training('Target Practice')
            self.targets.add(stage.get_targets())

        elif nr == 2:
            stage = Stage02MoreTraining('More Target Practise')
            self.targets.add(stage.get_targets())

        elif nr == 3:
            stage = Stage03Butterflies('Bouncing Bubbles')
            self.targets.add(stage.get_targets())
        elif nr == 4:
            stage = Stage04Slimes('Slimed')
            self.targets.add(stage.get_targets())
        elif nr == 5:
            stage = Stage05Bullseye('Bulls Eye')
            #self.target.sadd(stage.get_target())
        elif nr == 6:
            stage = Stage06Fires('Fireballs')
            #self.target.sadd(stage.get_target())
        elif nr == 7:
            stage = Stage07Winds('Whrrrrrrrrr')
            #self.target.sadd(stage.get_target())

        """levels = {1:'Target Practice',2:'More Target Practise',3:'Bouncing Bubbles',4:'Slimed', 5:'Bulls Eye',6: 'Fireballs'
                  ,7:'Unfriedly Skies', 8:'Whrrrrrrrrr'}"""

    def render(self, event, screen, arrows):

        #create monsters
        if self.finished:
            self.finished = 0

            self.handle_targets()

        #check for targets out of range
        for m in self.targets:
            if m.get_y() > 1000 and m.get_shotstatus() == 1:
                self.targets.remove(m)

        #check if level already finished
        if len(self.targets) == 0:
            self.stagenumber += 1
            self.finished = 1

        #check for collides
        for m in self.targets:
            for a in arrows:
                #inaccurate for balloons - subtract 70 see Arrow init
                if pygame.sprite.collide_rect(a, m):
                    #if m.rect.collidepoint(a.get_x, a.get_y):
                    m.set_shot()

        #render all targets
        self.targets.draw(screen)
        self.targets.update()
