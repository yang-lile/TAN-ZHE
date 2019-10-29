import pygame
import sys, time
from pygame.locals import *
from pygame.sprite import *

# global value define.
screen = ""
bgSurface = ""
# this is a group of sprite, but name is different.
simpleGroup = pygame.sprite.OrderedUpdates()

# it is a key function
# function: repack update(), make it update sprite.
def updateDisplay():
    # this is a low inefficient ((((algorithm))))mark down this word to learn it.
    simpleGroup.update()
    # every update will all do. but it is waste for the program.
    # so we should update at a specific time.

    # draw now status on screen(there are two status on the screen)
    simpleGroup.draw(screen)
    # update it to the screen
    pygame.display.update()
    # clear different pixel by bgSurface
    simpleGroup.clear(screen,bgSurface)

# a class named DongDong inherit Sprite
class DongDong(pygame.sprite.Sprite):
    # var is variety. When the key down, change var.
    # but one key one move...(a hole waiting to fill)
    var_x = 0
    var_y = 0
    status_UP   = False
    status_DOWN = False
    status_LEFT = False
    status_RIGHT= False
    
    def __init__(self,name,pos,imageAddress):
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        self.image = pygame.image.load(imageAddress).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.pos = pos
    def update(self):# I don't know how to use this function, (other hole)
        # print(self.var_x,self.var_y)
        self.pos = (self.pos[0] + self.var_x, self.pos[1] + self.var_y)
        self.rect.center = self.pos
        self.var_x = 0
        self.var_y = 0
        # updateDisplay()

def main():
    # reference global value is like our globalValue.py
    global screen, bgSurface
    pygame.display.set_caption("探者")
    screen = pygame.display.set_mode((700,700))
    screen.fill((121,232,122))
    # copy a backup to restore screen
    bgSurface = screen.copy()
    pygame.display.update()

    laoZhang = DongDong("zyl",(350,350) ,'dongdongB.png')
    # add to simpleGroup let it presence.
    simpleGroup.add(laoZhang)
    simpleGroup.draw(screen)

    
    # print(pygame.key.get_repeat())
    while True:
        # time.sleep(0.05)
        pygame.key.set_repeat(0, 50)
        for event in pygame.event.get():
            if event.type in (pygame.locals.K_ESCAPE, QUIT):
                pygame.quit()
                sys.exit()
            
            # click on the status
            elif event.type == pygame.locals.KEYDOWN:
                if event.key in (K_w, K_UP):
                    laoZhang.status_UP = True
                if event.key in (K_s, K_DOWN):
                    laoZhang.status_DOWN = True
                if event.key in (K_a, K_LEFT):
                    laoZhang.status_LEFT = True
                if event.key in (K_d, K_RIGHT):
                    laoZhang.status_RIGHT = True
            # click off the status
            elif event.type == pygame.locals.KEYUP:
                print("积分而非")
                if event.key in (K_w, K_UP):
                    laoZhang.status_UP = False
                if event.key in (K_s, K_DOWN):
                    laoZhang.status_DOWN = False
                if event.key in (K_a, K_LEFT):
                    laoZhang.status_LEFT = False
                if event.key in (K_d, K_RIGHT):
                    laoZhang.status_RIGHT = False
            # move it
            if laoZhang.status_UP:
                laoZhang.var_y = -10
            if laoZhang.status_DOWN:
                laoZhang.var_y = 10
            if laoZhang.status_LEFT:
                laoZhang.var_x = -10
            if laoZhang.status_RIGHT:
                laoZhang.var_x = 10
            # laoZhang.update()
            # simpleGroup.update()
        updateDisplay()
        # time.sleep()



if __name__ == "__main__":
    main()