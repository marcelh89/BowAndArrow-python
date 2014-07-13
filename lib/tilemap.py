__author__ = 'marcman'

from lib.sprites.player import Player
from lib.sprites.paper import Paper
from pygame.locals import *
from lib.stages import Stages
from lib.sprites.infobar import Infobar

class Tilemap(object):

    def __init__(self):

        self.player = Player()
        self.paper = Paper()
        self.score = 0
        self.status = 0
        self.stages = Stages(self.player)
        self.infobar = Infobar(self.score, 1, "Training", 20)


    def render(self, event, screen):

        #render infobar
        self.infobar.render(screen, self.score, self.stages.stagenumber)

        #render game
        stat = self.status
        stage = self.stages.stagenumber

        if stat == 1 or stage == 9:
            print "render gameover"
            self.paper.render(stat, screen)

            #check for newgame
            if event.type == MOUSEBUTTONUP:
                self.stages.cleanup_all()
                self.status = 0

        elif stat == 2:
            print "render stagecomplete"
            self.paper.render(stat, screen)

            #check for click mouse to go on
            if event.type == MOUSEBUTTONUP:
                self.status = 0

        else:
            #render player
            arrows = self.player.render(event, screen)

            #render stage
            self.status = self.stages.render(event, screen, arrows)

    def handle_input(self, event):
        self.player.handle_input(event)