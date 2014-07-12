__author__ = 'marcman'

from pygame.sprite import *


class Leftmover (Sprite):
    def __init__(self, x_pos, y_pos, alive, dead):
        Sprite.__init__(self)
        self.speed = 3
        self.dead = dead
        self.alive = alive
        self.image = pygame.image.load("./lib/sprites/img/"+alive)
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
        self.image = pygame.image.load("./lib/sprites/img/"+self.dead)
        self.shot = 1
        self.speed = 1

    def get_shotstatus(self):
        return self.shot

