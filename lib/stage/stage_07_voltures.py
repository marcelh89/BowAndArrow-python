__author__ = 'marcman'

from stage import Stage
from lib.sprites.volture import Volture
import random


class Stage07Voltures(Stage):

    def __init__(self, description):
        Stage.__init__(self, description)
        self.targets = []
        self.targets.append(Volture(random.randint(800, 1500), random.randint(100, 500)) for _ in range(25))

    def get_targets(self):
        return self.targets