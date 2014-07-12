__author__ = 'marcman'

from lib.sprites.player import Player
from lib.stages import Stages


class Tilemap(object):

    def __init__(self):

        self.player = Player()
        self.stages = Stages(self.player)
        self.status = 0

    def render(self, event, screen):

        if self.status == 1:
            print "render gameover"
        elif self.status == 2:
            print "render stagecomplete"
        else:
            #render player
            arrows = self.player.render(event, screen)

            #render stage
            self.status = self.stages.render(event, screen, arrows)

    def handle_input(self, event):
        self.player.handle_input(event)