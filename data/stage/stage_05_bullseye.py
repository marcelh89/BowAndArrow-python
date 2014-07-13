__author__ = 'marcman'

from data.stage.stage import Stage
from data.components.bullseye import Bullseye
import random


class Stage05Bullseye(Stage):
    def __init__(self, description):
        Stage.__init__(self, description)
        self.targets = []
        self.targets.append(Bullseye(700, random.randint(100, 500)))

    def get_targets(self):
        return self.targets