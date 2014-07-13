__author__ = 'marcman'

# !/usr/bin/python
"""
Created on Wed May  9 12:32:20 2012

@author: marcel
"""

from data.components.leftmover import Leftmover


class Slime(Leftmover):
    def __init__(self, x_pos, y_pos):
        Leftmover.__init__(self, x_pos, y_pos, "slime.png", "slime.png", "slime_dead.png")