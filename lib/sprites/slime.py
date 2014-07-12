__author__ = 'marcman'

# !/usr/bin/python
"""
Created on Wed May  9 12:32:20 2012

@author: marcel
"""

from pygame.sprite import *


class Slime(Sprite):
    def __init__(self, x_pos, y_pos):
        Sprite.__init__(self)
        #red_balloon
        self.speed = 3
        self.image = pygame.image.load("./lib/sprites/img/slime.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = x_pos
        self.rect.centery = y_pos
        self.shot = 0
        self.out_of_bounds = 0

    def update(self):

        #check if target is shot
        if not self.shot:
            self.rect.centerx -= self.speed

            if self.rect.centerx < - 100:
                self.shot = 1

        else:
            self.rect.centery += self.speed * 3
            if self.rect.centery > 800:
                self.out_of_bounds = 1

    def get_rect(self):
        return self.rect

    def get_y(self):
        return self.rect.centery

    def set_shot(self):
        self.image = pygame.image.load("./lib/sprites/img/slime_dead.png")
        self.shot = 1
        self.speed = 1

    def get_shotstatus(self):
        return self.shot

