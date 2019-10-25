#
# @Time         : 2019/9/23 下午2:43
# @Author       : 礼lua
# @Modify Log   : add function run
# @todoList     : 1.create a map
#               : 2.resize map
#
import pygame, sys
from pygame.locals import *
from globalValue import GL
import mapBlock
# this is our main of game

def mapInit():
    for i in range(0,16):
        for j in range(0,24):
            if GL.Map1[i][j] == 1:
                block = mapBlock.BlockGreen((j*40+20,i*40+20))
            elif GL.Map1[i][j] == 2:
                block = mapBlock.BlockBlue((j*40+20,i*40+20))
            elif GL.Map1[i][j] == 3:
                block = mapBlock.BlockPurple((j*40+20,i*40+20))
            elif GL.Map1[i][j] == 4:
                block = mapBlock.BlockRed((j*40+20,i*40+20))
            elif GL.Map1[i][j] == 5:
                block = mapBlock.BlockYellow((j*40+20,i*40+20))
            elif GL.Map1[i][j] == 6:
                block = mapBlock.BlockGray((j*40+20,i*40+20))
            elif GL.Map1[i][j] == 7:
                block = mapBlock.BlockPeople((j*40+20,i*40+20))
            else:
                print("反正出bug了我也不会修")
            block.render()

def run():
    GL.screen = pygame.display.set_mode((GL.scrLength,GL.scrWidth))
    GL.screen.fill((0,0,0))
    mapInit()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key in (K_w, ):
                    print("w")

        pygame.display.update()


if __name__ == "__main__":
    run()
