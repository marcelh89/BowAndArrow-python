__author__ = 'marcman'

from lib.stages.stage_01_training import Stage01Training
from lib.stages.stage_02_more_training import Stage02MoreTraining
from lib.stages.stage_03_butterflies import Stage03Butterflies
from lib.stages.stage_04_slimes import Stage04Slimes
from lib.stages.stage_05_bullseye import Stage05Bullseye
from lib.stages.stage_06_fires import Stage06Fires
from lib.stages.stage_07_winds import Stage07Winds


def stages_start(lv):

    if lv == 1:
        stage = Stage01Training('Target Practice')
    elif lv == 2:
        stage = Stage02MoreTraining('More Target Practise')
    elif lv == 3:
        stage = Stage03Butterflies('Bouncing Bubbles')
    elif lv == 4:
        stage = Stage04Slimes('Slimed')
    elif lv == 5:
        stage = Stage05Bullseye('Bulls Eye')
    elif lv == 6:
        stage = Stage06Fires('Fireballs')
    elif lv == 7:
        stage = Stage07Winds('Whrrrrrrrrr')

    return stage