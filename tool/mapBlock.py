#
# @Time         : 2019/9/23 下午3:08
# @Author       : 礼lua
# @Modify Log   : add L12-L24
# @todoList     : 1.class mapBlock
#               : 2.maps
#
import pygame, sys
from pygame.locals import *
# from globalValue import GL

class MapBlock:
    def __init__(self, colorImage, position):
        self.colorImage = pygame.image.load(colorImage).convert_alpha()
        self.position = position
    # def render(self):                   # if in it, change pic from 'up'to 'down'
    #     w, h = self.colorImage.get_size()
    #     x, y = self.position
    #     GL.screen.blit(self.colorImage, (x-w/2, y-h/2))
    def render(self, myMap):
        w, h = self.colorImage.get_size()
        x, y = self.position
        myMap.blit(self.colorImage, (x-w/2, y-h/2))

class BlockGreen(MapBlock):# 1
    def __init__(self, position):
        self.position = position
        self.colorImage = pygame.image.load("src/ColorBlock/greenImage.png")
class BlockBlue(MapBlock):#  2
    def __init__(self, position):
        self.position = position
        self.colorImage = pygame.image.load("src/ColorBlock/blueImage.png")
class BlockPurple(MapBlock):# 3
    def __init__(self, position):
        self.position = position
        self.colorImage = pygame.image.load("src/ColorBlock/purpleImage.png")
class BlockRed(MapBlock):# 4
    def __init__(self, position):
        self.position = position
        self.colorImage = pygame.image.load("src/ColorBlock/redImage.png")
class BlockYellow(MapBlock):# 5
    def __init__(self, position):
        self.position = position
        self.colorImage = pygame.image.load("src/ColorBlock/yellowImage.png")
class BlockGray(MapBlock):# 6
    def __init__(self, position):
        self.position = position
        self.colorImage = pygame.image.load("src/ColorBlock/grayImage.png")
class BlockPeople(MapBlock):# 7
    def __init__(self, position):
        self.position = position
        self.colorImage = pygame.image.load("src/ColorBlock/people1Image.png")
# class of creatMap
class BlockSave(MapBlock):
    def __init__(self, position):
        self.position = position
        self.colorImage = pygame.image.load("src/ColorBlock/saveImage.png")

if __name__ == "__main__":
    screen = pygame.display.set_mode((960, 640))
    screen.fill((0,0,0))
    for i in range(0,16):
        for j in range(0,24):
            if GL.Map1[i][j] == 1:
                block = BlockGreen((j*40+20,i*40+20))
            elif GL.Map1[i][j] == 2:
                block = BlockBlue((j*40+20,i*40+20))
            elif GL.Map1[i][j] == 3:
                block = BlockPurple((j*40+20,i*40+20))
            elif GL.Map1[i][j] == 4:
                block = BlockRed((j*40+20,i*40+20))
            elif GL.Map1[i][j] == 5:
                block = BlockYellow((j*40+20,i*40+20))
            elif GL.Map1[i][j] == 6:
                block = BlockGray((j*40+20,i*40+20))
            elif GL.Map1[i][j] == 7:
                block = BlockPeople((j*40+20,i*40+20))
            else:
                print("反正出bug了我也不会修")
            block.render()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
