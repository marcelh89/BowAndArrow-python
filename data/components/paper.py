# !/usr/bin/python
"""
Created on Wed May  9 12:32:20 2012

@author: marcel
"""
from pygame.sprite import *


class Paper(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        #bowman simply standing
        self.image = pygame.image.load("./resources/graphics/paper.png")
        self.image = pygame.transform.scale(self.image, (500, 400))
        self.rect = self.image.get_rect()
        self.rect.centerx += 150
        self.rect.centery += 100
        self.papersprite = pygame.sprite.RenderUpdates()
        self.papersprite.add(self)
        self.font = pygame.font.Font(None, 30)

    def render(self, status, screen):

        description = self.font.render(get_description(status), 1, (10, 10, 10))
        heading = self.font.render(get_heading(status), 1, (10, 10, 10))

        self.papersprite.draw(screen)
        self.papersprite.update()
        screen.blit(heading, (350, 180))
        screen.blit(description, (220, 280))


def get_description(status):
        description = ['', 'Finally, you got killed, oh what a pitty', 'Great Job here!', '... is nothing!']
        return description[status]


def get_heading(status):
        heading = ['', 'GAMEOVER', 'SUCCESS', 'A Bowman without arrows']
        return heading[status]