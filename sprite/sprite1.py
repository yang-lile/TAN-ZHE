import pygame
import sys
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
    def __init__(self,name,pos,imageAddress):
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        self.image = pygame.image.load(imageAddress).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.pos = pos
    def update(self):# I don't know how to use this function, (other hole)
        print(self.var_x,self.var_y)
        self.pos = (self.pos[0] + self.var_x, self.pos[1] + self.var_y)
        self.rect.center = self.pos
        self.var_x = 0
        self.var_y = 0
        updateDisplay()

def main():
    # reference global value is like our globalValue.py
    global screen, bgSurface
    screen = pygame.display.set_mode((700,700))
    screen.fill((121,232,122))
    # copy a backup to restore screen
    bgSurface = screen.copy()
    pygame.display.update()

    laoZhang = DongDong("zyl",(350,350) ,'dongdongB.png')
    # add to simpleGroup let it presence.
    simpleGroup.add(laoZhang)
    simpleGroup.draw(screen)

    while True:
        for event in pygame.event.get():
            if event.type in (pygame.locals.K_ESCAPE, QUIT):
                pygame.quit()
                sys.exit()
            # listener keybroad to control var,move.
            if event.type == pygame.locals.KEYDOWN:
                if event.key in (K_w, K_UP):
                    laoZhang.var_y = -10
                if event.key in (K_s, K_DOWN):
                    laoZhang.var_y = 10
                if event.key in (K_a, K_LEFT):
                    laoZhang.var_x = -10
                if event.key in (K_d, K_RIGHT):
                    laoZhang.var_x = 10
            # laoZhang.update()
            simpleGroup.update()
        updateDisplay()

if __name__ == "__main__":
    main()