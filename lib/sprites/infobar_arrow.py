# !/usr/bin/python
"""
Created on Wed May  9 12:32:20 2012

@author: marcel
"""
from pygame.sprite import *


class InfobarArrow(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.image = pygame.image.load("./lib/sprites/img/infobar_arrow.gif")
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y

    def get_x(self):
        return self.rect.centerx

    def get_rect(self):
        return self.rect

    def get_y(self):
        return self.rect.centery

    def set_x(self, x):
        self.rect.centerx = x

    def set_y(self, y):
        self.rect.centerx = y

    def set_stuck(self, ):
        self.stuck = 1
        self.speed = 0

    def set_downwards(self, downwards):
        self.downwards = downwards