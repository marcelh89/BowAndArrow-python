__author__ = 'marcman'

from lib.sprites.player import Player
from lib.stages import Stages


class Tilemap(object):

    def __init__(self):

        self.player = Player()
        self.stages = Stages(self.player)

    def render(self, event, screen):

        #render player
        arrows = self.player.render(event, screen)

        #render stage
        self.stages.render(event, screen, arrows)

    def handle_input(self, event):
        self.player.handle_input(event)