__author__ = 'marcman'

import random
from data.stage.stage import Stage
from data.components.balloon import Balloon


class Stage02MoreTraining(Stage):
    def __init__(self, description):
        Stage.__init__(self, description)
        self.targets = []
        self.targets.append(Balloon('RED', random.randint(330, 750), random.randint(600, 800)) for _ in range(15))
        self.targets.append(Balloon('YELLOW', random.randint(330, 750), random.randint(600, 800)) for _ in range(5))

    def get_targets(self):
        return self.targets