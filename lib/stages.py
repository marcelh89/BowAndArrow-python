__author__ = 'marcman'

import pygame
from stage.stage import Stage
from stage.stage_01_training import Stage01Training
from stage.stage_02_more_training import Stage02MoreTraining
from stage.stage_03_butterflies import Stage03Butterflies
from stage.stage_04_slimes import Stage04Slimes
from stage.stage_05_bullseye import Stage05Bullseye
from stage.stage_06_fires import Stage06Fires
from stage.stage_07_voltures import Stage07Voltures
from stage.stage_08_winds import Stage08Winds
import math


class Stages(object):

    def __init__(self, player):
        self.targets = pygame.sprite.RenderUpdates()
        self.stagenumber = 1
        self.finished = 1
        self.player = player
        self.currentstage = Stage("Dummy")

    def handle_targets(self):
        nr = self.stagenumber

        if nr == 1:
            self.currentstage = Stage01Training('Target Practice')
            self.targets.add(self.currentstage.get_targets())

        elif nr == 2:
            self.currentstage = Stage02MoreTraining('More Target Practise')
            self.targets.add(self.currentstage.get_targets())

        elif nr == 3:
            self.currentstage = Stage03Butterflies('Bouncing Bubbles')
            self.targets.add(self.currentstage.get_targets())
        elif nr == 4:
            self.currentstage = Stage04Slimes('Slimed')
            self.targets.add(self.currentstage.get_targets())
        elif nr == 5:
            self.currentstage = Stage05Bullseye('Bulls Eye')
            self.targets.add(self.currentstage.get_targets())
        elif nr == 6:
            self.currentstage = Stage06Fires('Fireballs')
            self.targets.add(self.currentstage.get_targets())
        elif nr == 7:
            self.currentstage = Stage07Voltures('Unfriendly Skies')
            self.targets.add(self.currentstage.get_targets())
        elif nr == 8:
            self.currentstage = Stage08Winds('Whrrrrrrrrr')
            self.targets.add(self.currentstage.get_targets())

    def cleanup_targets_and_arrows(self):
        for t in self.targets:
            self.targets.remove(t)
        for a in self.player.arrows:
            self.player.arrows.remove(a)

    def cleanup_all(self):
        self.cleanup_targets_and_arrows()
        self.stagenumber = 1
        self.finished = 1

    def render(self, event, screen, arrows):

        p = self.player

        #create monsters
        if self.finished:
            self.finished = 0
            self.handle_targets()

        #check for targets out of range
        for m in self.targets:
            y = m.get_y()

            if m.get_shotstatus() == 1:
                if y > 1000 or y < -500:
                    self.targets.remove(m)

        #check if level already finished
        if len(self.targets) == 0:
            self.stagenumber += 1
            self.finished = 1
            return 2

        #check for collides
        for m in self.targets:

            #targets <--> player
            if self.stagenumber not in [1, 2, 3]:       # only collide after training and butterfly stages
                if pygame.sprite.collide_rect(m, p):
                    #print "Gameover!"
                    self.cleanup_all()
                    return 1

            #targets <--> arrows
            for a in arrows:

                #special level 5 bullseye
                if self.stagenumber == 5:
                    mr = m.get_rect()
                    ar = a.get_rect()

                    if mr.collidepoint(ar.center):
                        deltay = ar.midright[1]-mr.centery
                        deltay = math.fabs(deltay)
                        a.set_stuck()
                        a.set_downwards(m.get_downwards())

                        if deltay < 4.0:
                            m.set_shot()
                            self.cleanup_targets_and_arrows()

                else:
                    if pygame.sprite.collide_rect(a, m):
                        m.set_shot()

        #render all targets
        self.targets.draw(screen)
        self.targets.update()

        #print len(self.targets)

        return 0