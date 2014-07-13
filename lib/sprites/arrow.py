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
        self.speed = 5
        self.stuck = 0
        self.downwards = 0
        self.image = pygame.image.load("./lib/sprites/img/arrow.png")
        self.rect = self.image.get_rect()
        self.rect.center = pygame.mouse.get_pos()
        self.rect.centerx = 150

        if self.rect.centery < 100:
            self.rect.centery = 100
        elif self.rect.centery > 500:
            self.rect.centery = 500

        self.rect.centery -= 11

    def update(self):
        if self.stuck:

            self.speed = 1

            if self.downwards:
                    self.rect.centery += self.speed
            else:
                    self.rect.centery -= self.speed
        else:
            self.rect.centerx += self.speed

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