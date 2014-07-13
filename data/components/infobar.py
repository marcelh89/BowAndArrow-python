__author__ = 'marcman'

from pygame.sprite import *


class Infobar(Sprite):
    def __init__(self, score, stage, stagetext, arrowcount):
        Sprite.__init__(self)
        self.image = pygame.image.load("./resources/graphics/infobar.png")
        self.image = pygame.transform.scale(self.image, (800, 30))
        self.rect = self.image.get_rect()
        self.infobararrow = pygame.image.load("./resources/graphics/infobar_arrow.png")
        self.score = score
        self.stage = stage
        self.stagetext = stagetext
        self.infosprite = pygame.sprite.RenderUpdates()
        self.infosprite.add(self)
        self.font = pygame.font.Font(None, 25)

    def render(self, screen, scoreR, stageR, stagetextR, arrowcountR):
        score = self.font.render(str(scoreR), 1, (10, 10, 10))
        stage = self.font.render("Stage " + str(stageR), 1, (10, 10, 10))
        stagetext = self.font.render(stagetextR, 1, (10, 10, 10))

        self.infosprite.draw(screen)
        self.infosprite.update()
        screen.blit(score, (100, 10))
        screen.blit(stage, (300, 10))
        screen.blit(stagetext, (400, 10))

        for x in range(arrowcountR):
            screen.blit(self.infobararrow, (600 + x * 5, 10))