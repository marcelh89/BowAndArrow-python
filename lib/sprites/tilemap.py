__author__ = 'marcman'

from lib.sprites.player import Player
from lib.sprites.targets import Targets


class Tilemap(object):

    def __init__(self):

        self.__player = Player()
        self.__targets = Targets()

    def render(self, event, screen):

        #render player
        self.__player.render(event, screen)

        #render monsters
        self.__targets.render(event, screen)

    def handle_input(self,event):
        self.__player.handle_input(event)
