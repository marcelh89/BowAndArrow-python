__author__ = 'marcman'

from stage import Stage
from lib.sprites.balloon import Balloon
import random


class Stage01Training(Stage):

    def __init__(self, description):
        Stage.__init__(self, description)
        self.targets = (Balloon('RED', random.randint(330, 750), 600) for _ in range(15))

    def get_targets(self):
        return self.targets