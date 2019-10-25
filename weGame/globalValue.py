#
# @Time         : 2019/9/23 下午2:45
# @Author       : 礼lua
# @Modify Log   : add value: archiveFlag
#               : add note on L9
#

#
# L1-L7 is a fixed line to mark every changes
# "L" + num is line of position
# add is new some code at some line
# remove is delete some code at some line
# change is update some code
#

#
# this is a global value share file
# use to save some Value in multiple file
#
import pygame
# from pygame.locals import *

class GL:
    # define a screen with 960x640
    scrLength = 960
    scrWidth = 640
    screen = pygame.display.set_mode((scrLength, scrWidth))

    # default colors
    WHITE = 255,255,255
    BLUE = 0,0,200
    BLACK = 0,0,0
    # lightGreen = 215, 255, 143

    # cusFontAddress is a custom font
    # python isn't friendly with Chinese
    # so we use custom font
    cusFontAddress = "Chinese/YaoSuiXinShouXieTi-2.ttf"

    # if there is a game archive, value is True.
    archiveFlag = False

    # 梗来源的地图
    Map1 = [
[6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 1, 1, 1, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, ],
[6, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 6, ],
[6, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 6, ],
[6, 1, 1, 1, 4, 4, 4, 4, 1, 1, 1, 2, 2, 2, 1, 1, 5, 5, 5, 5, 1, 1, 1, 6, ],
[6, 1, 1, 1, 4, 4, 4, 4, 1, 1, 1, 2, 1, 2, 1, 1, 5, 5, 5, 5, 1, 1, 1, 6, ],
[6, 1, 1, 1, 4, 4, 4, 4, 1, 3, 3, 3, 3, 3, 3, 1, 5, 5, 5, 5, 1, 1, 1, 6, ],
[1, 1, 1, 1, 4, 4, 4, 4, 1, 1, 1, 2, 1, 2, 3, 1, 5, 5, 5, 5, 1, 1, 1, 1, ],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 2, 1, 2, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, ],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 7, 2, 1, 2, 3, 2, 2, 2, 2, 1, 1, 1, 1, 1, ],
[6, 1, 1, 1, 2, 2, 2, 2, 2, 3, 2, 2, 1, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 6, ],
[6, 1, 1, 1, 1, 1, 1, 3, 3, 3, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 6, ],
[6, 1, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 2, 2, 3, 2, 2, 2, 2, 1, 1, 1, 1, 6, ],
[6, 1, 1, 1, 1, 3, 3, 1, 3, 1, 1, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 1, 1, 6, ],
[6, 1, 1, 1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 3, 3, 3, 1, 1, 1, 1, 1, 1, 1, 6, ],
[6, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 6, ],
[6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 1, 1, 1, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, ],
]

