# !/usr/bin/python
"""
Created on Wed May  9 12:32:20 2012

@author: marcel
"""

from pygame.sprite import *


class Bullseye(Sprite):
    def __init__(self, x_pos, y_pos):
        Sprite.__init__(self)
        #red_balloon
        self.speed = 1
        self.image = pygame.image.load("./resources/graphics/bulls_eye.png")
        self.downwards = 0

        self.rect = self.image.get_rect()
        self.rect.centerx = x_pos
        self.rect.centery = y_pos
        self.shot = 0
        self.out_of_bounds = 0

    def update(self):

        #check if target is shot
        if not self.shot:

            #set lower bound
            if self.rect.centery >= 550:

                self.rect.centery -= self.speed
                self.downwards = 0

            #set upper bound
            elif self.rect.centery <= 50:

                self.rect.centery += self.speed
                self.downwards = 1

            #set space for movement
            elif self.rect.centery in range(51, 550):

                if self.downwards:
                    self.rect.centery += self.speed
                else:
                    self.rect.centery -= self.speed

        else:
            self.rect.centery -= self.speed * 3
            self.rect.centerx -= self.speed * 2
            if self.rect.centery < -100:
                self.out_of_bounds = 1

    def get_rect(self):
        return self.rect

    def get_y(self):
        return self.rect.centery

    def get_x(self):
        return self.rect.centerx

    def set_shot(self):
        self.image = pygame.image.load("./resources/graphics/butterfly.png")
        self.shot = 1
        self.speed = 1

    def get_shotstatus(self):
        return self.shot

    def get_downwards(self):
        return self.downwards
