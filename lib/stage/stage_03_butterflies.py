from lib.sprites.butterfly import Butterfly

__author__ = 'marcman'

from stage import Stage
import random


class Stage03Butterflies(Stage):
    def __init__(self, description):
        Stage.__init__(self, description)
        self.targets = []
        self.targets.append(Butterfly(random.randint(330, 750), random.randint(400, 1000)) for _ in range(20))

    def get_targets(self):
        return self.targets