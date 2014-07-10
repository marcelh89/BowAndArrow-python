__author__ = 'marcman'

from lib.sprites.player import Player
from lib.stages import Stages


class Tilemap(object):

    def __init__(self):

        self.__player = Player()
        self.stages = Stages()

    def render(self, event, screen):

        #render player
        arrows = self.__player.render(event, screen)

        #render stage
        self.stages.render(event, screen, arrows)

    def handle_input(self, event):
        self.__player.handle_input(event)