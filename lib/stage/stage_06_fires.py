__author__ = 'marcman'

from stage import Stage
from lib.sprites.fires import Fires
import random


class Stage06Fires(Stage):
    def __init__(self, description):
        Stage.__init__(self, description)
        self.targets = []
        self.targets.append(Fires(random.randint(800, 1500), random.randint(100, 500)) for _ in range(25))

    def get_targets(self):
        return self.targets