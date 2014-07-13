# !/usr/bin/python
"""
Created on Wed May  9 12:32:20 2012

@author: marcel
"""
from pygame.sprite import *
from pygame.locals import *
from data.components.arrow import Arrow


class Player(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        #bowman simply standing
        self.image = pygame.image.load("./resources/graphics/hero_without_arrow.png")
        self.rect = self.image.get_rect()
        self.is_arrowed = 0
        self.is_targeting = 0
        self.arrows = pygame.sprite.RenderUpdates()
        self.playersprite = pygame.sprite.RenderUpdates()
        self.playersprite.add(self)
        self.arrowcount = 20

    def update(self):
        x, y = pygame.mouse.get_pos()
        self.rect.centerx = 100

        if y < 100:
            #print "y less than 100"
            self.rect.centery = 100
        elif y > 500:
            #print "y greater than 500"
            self.rect.centery = 500
        else:
            self.rect.centery = y

    def reload(self):
        #bowman is armed
        self.image = pygame.image.load("./resources/graphics/hero_stand.png")
        self.is_arrowed = 1

    def target(self):
        #bowman is targeting
        self.image = pygame.image.load("./resources/graphics/hero_armed.png")
        self.is_targeting = 1

    def shoot(self):
        #bowman after shoot
        self.image = pygame.image.load("./resources/graphics/hero_without_arrow.png")
        self.is_arrowed = 0
        self.is_targeting = 0

    def get_rect(self):
        return self.rect

    def handle_input(self, event):
        """if event.type == MOUSEBUTTONDOWN:
            print 'mousebuttondown'"""

        if event.type == MOUSEBUTTONUP:
            #print 'mousebuttonup'

            if self.is_arrowed and self.is_targeting:
                self.shoot()
                self.arrows.add(Arrow())
                self.arrowcount -= 1

        if pygame.mouse.get_pressed()[0]:
            #print 'leftbutton'
            if self.is_arrowed:
                self.target()

        if pygame.mouse.get_pressed()[2]:
            #print 'rightbutton'
            self.reload()

    def render(self, event, screen):
        self.playersprite.draw(screen)
        self.playersprite.update()

        self.arrows.draw(screen)
        self.arrows.update()

        #arrows out of border deletion
        for i in self.arrows:
            if i.get_x() > 1000:
                #print "remove arrow"
                self.arrows.remove(i)

        return self.arrows

    def get_arrowcount(self):
        return self.arrowcount

    def reset_arrows(self):
        self.arrowcount = 20
