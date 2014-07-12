# !/usr/bin/python
"""
Created on Wed May  9 12:32:20 2012

@author: marcel
"""

from pygame.sprite import *


class Balloon(Sprite):
    def __init__(self, color, x_pos, y_pos):
        Sprite.__init__(self)
        self.color = color
        #red_balloon
        if self.color == 'RED':
            self.speed = 1
            self.image = pygame.image.load("./lib/sprites/img/ballon.png")

        #yello_balloon
        if self.color == 'YELLOW':
            self.speed = 1
            self.image = pygame.image.load("./lib/sprites/img/ballon_yellow.png")

        self.rect = self.image.get_rect()
        self.rect.centerx = x_pos
        self.rect.centery = y_pos
        self.shot = 0
        self.out_of_bounds = 0

    def update(self):

        if not self.shot:
            self.rect.centery -= self.speed
            if self.rect.centery <= 0:
                self.rect.centery = 700
        else:
            self.rect.centery += 3
            if self.rect.centery > 800:
                self.out_of_bounds = 1

    def get_rect(self):
        return self.rect

    def get_y(self):
        return self.rect.centery

    def set_shot(self):
        #red_balloon
        if self.color == 'RED':
            self.image = pygame.image.load("./lib/sprites/img/ballon_dead.png")

        #yello_balloon
        if self.color == 'YELLOW':
            self.image = pygame.image.load("./lib/sprites/img/ballon_yellow_dead.png")

        self.shot = 1
        self.speed = 1

    def get_shotstatus(self):
        return self.shot
