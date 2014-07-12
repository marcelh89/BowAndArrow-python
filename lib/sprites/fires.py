__author__ = 'marcman'

# !/usr/bin/python
"""
Created on Wed May  9 12:32:20 2012

@author: marcel
"""

from lib.sprites.leftmover import Leftmover


class Fires(Leftmover):
    def __init__(self, x_pos, y_pos):
        Leftmover.__init__(self, x_pos, y_pos, "fire1.png", "fire2.png", "fire_dead.png")