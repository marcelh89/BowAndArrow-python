# !/usr/bin/python
"""
Created on Wed May  9 12:32:20 2012

@author: marcel
"""
from pygame.sprite import *


class Arrow(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        #bowman simply standing
        self.image = pygame.image.load("./sprites/arrow.png")
        self.rect = self.image.get_rect()
        self.rect.center = pygame.mouse.get_pos()
        self.rect.centerx += 70
        self.rect.centery -= 10

    def update(self):
        self.rect.centerx += 5

    def get_x(self):
        return self.rect.centerx

    def get_rect(self):
        return self.rect

    def get_y(self):
        return self.rect.centery

    def set_x(self):
        self.rect.centerx += 70