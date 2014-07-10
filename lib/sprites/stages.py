__author__ = 'marcman'

from lib.sprites.targets import Targets


class Stages(object):

    def __init__(self):
        self.targets = Targets()
        self.stagenumber = 1
        self.finished = 0

    def render(self, event, screen):

        if self.stagenumber == 1:
            self.targets.render(event, screen)
        elif self.stagenumber == 2:
            self.targets.render(event, screen)


        self.targets.render(event, screen)
