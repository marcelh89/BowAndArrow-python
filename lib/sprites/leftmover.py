__author__ = 'marcman'

from pygame.sprite import *


class Leftmover (Sprite):
    def __init__(self, x_pos, y_pos, alive1, alive2, dead):
        Sprite.__init__(self)
        self.speed = 3
        self.dead = dead
        self.alive1 = alive1
        self.alive2 = alive2
        self.alive = 1
        self.counter = 0
        self.image = pygame.image.load("./lib/sprites/img/"+alive1)
        self.rect = self.image.get_rect()
        self.rect.centerx = x_pos
        self.rect.centery = y_pos
        self.shot = 0
        self.out_of_bounds = 0

    def update(self):

        #check if target is shot
        if not self.shot:

            if self.counter == 20:

                if self.alive == 1:
                    self.image = pygame.image.load("./lib/sprites/img/"+self.alive2)
                    self.alive = 2

                elif self.alive == 2:
                    self.image = pygame.image.load("./lib/sprites/img/"+self.alive1)
                    self.alive = 1

                self.counter = 0

            self.rect.centerx -= self.speed
            self.counter += 1

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
        self.image = pygame.image.load("./lib/sprites/img/"+self.dead)
        self.shot = 1
        self.speed = 1

    def get_shotstatus(self):
        return self.shot

