#
# @Time         : 2019/9/23 下午2:46
# @Author       : 礼lua
# @Modify Log   : noting
# @todoList     : None
#
import pygame, sys
from pygame.locals import *
from globalValue import GL

class Button:
    def __init__(self, upImage, downImage, position):
        #
        # this is Button's init function
        # input: two picture, a position(center position)
        # output: null
        #
        self.upImage = pygame.image.load(upImage).convert_alpha()
        self.downImage = pygame.image.load(downImage).convert_alpha()
        self.position = position
    def isOver(self):
        #
        # judge the mouse cover or not on the Rectangle
        # return true is cover on
        pX, pY = pygame.mouse.get_pos() # get position of mouse
        x, y = self.position            # get position of rec center
        w, h = self.upImage.get_size()  # get length and width
        # judge by math
        in_x = x - w/2 < pX < x + w/2
        in_y = y - h/2 < pY < y + h/2
        return in_x and in_y            # mouse in rectangle need they both True
    def render(self):                   # if in it, change pic from 'up'to 'down'
        w, h = self.upImage.get_size()
        x, y = self.position
        if self.isOver():
            GL.screen.blit(self.downImage, (x-w/2, y-h/2))
            return True
        else:
            GL.screen.blit(self.upImage, (x-w/2, y-h/2))
            return False
       
if __name__ == "__main__":# 这是一个测试代码，当你单独运行Button.py的时候就会执行，被当作模块导入时不会执行
    screen = pygame.display.set_mode((960, 640))
    button1 = Button("up.png","down.png",(480, 320))
    screen.fill((0,0,0))
    # button1.render()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            flag = button1.render()
            if flag and (event.type == MOUSEBUTTONDOWN):
                print("嘿嘿")
        pygame.display.update()
