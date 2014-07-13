from lib.sprites.slime import Slime

__author__ = 'marcman'

from stage import Stage
import random


class Stage04Slimes(Stage):
    def __init__(self, description):
        Stage.__init__(self, description)
        self.targets = []
        self.targets.append(Slime(random.randint(800, 1500), random.randint(100, 500)) for _ in range(25))

    def get_targets(self):
        return self.targets