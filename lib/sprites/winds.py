__author__ = 'marcman'

# !/usr/bin/python
"""
Created on Wed May  9 12:32:20 2012

@author: marcel
"""

from lib.sprites.leftmover import Leftmover


class Winds(Leftmover):
    def __init__(self, x_pos, y_pos):
        Leftmover.__init__(self, x_pos, y_pos, "wind1.png","wind2.png", "wind_dead.png")