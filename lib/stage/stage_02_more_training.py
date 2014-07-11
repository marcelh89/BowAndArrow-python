__author__ = 'marcman'

import random
from stage import Stage
from lib.sprites.balloon import Balloon


class Stage02MoreTraining(Stage):

    def __init__(self, description):
        Stage.__init__(self, description)
        self.targets = []
        self.targets.append(Balloon('RED', x * 30 + 300, random.randint(600, 800)) for x in range(15))
        self.targets.append(Balloon('YELLOW', x * 30 * 3 + 300, random.randint(600, 800)) for x in range(5))

    def get_targets(self):
        return self.targets


