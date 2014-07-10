__author__ = 'marcman'

from lib.sprites.player import Player
import pygame

class Tilemap(object):
    def __init__(self):
        # Player-Objekt erstellen.
        self.__player = Player()

    def render(self, event, screen):
        #tileset render

        self.__player.render(event, screen)

    def handle_input(self,event):
        self.__player.handle_input(event)
