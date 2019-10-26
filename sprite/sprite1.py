import pygame
import sys
from pygame.locals import *
from pygame.sprite import *

screen = ""
bgSurface = ""
simpleGroup = pygame.sprite.OrderedUpdates()

def updateDisplay():
    simpleGroup.draw(screen)
    pygame.display.update()
    simpleGroup.clear(screen,bgSurface)

class DongDong(pygame.sprite.Sprite):
    var_x = 0
    var_y = 0
    def __init__(self,name,pos,imageAddress):
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        self.image = pygame.image.load(imageAddress).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.pos = pos
    def update(self):
        print(self.var_x,self.var_y)
        self.pos = (self.pos[0] + self.var_x, self.pos[1] + self.var_y)
        self.rect.center = self.pos
        self.var_x = 0
        self.var_y = 0
        updateDisplay()

def main():
    global screen, bgSurface
    screen = pygame.display.set_mode((700,700))
    screen.fill((121,232,122))
    bgSurface = screen.copy()
    pygame.display.update()

    laoZhang = DongDong("zyl",(350,350) ,'dongdongB.png')
    
    simpleGroup.add(laoZhang)
    simpleGroup.draw(screen)
    while True:
        for event in pygame.event.get():
            if event.type in (pygame.locals.K_ESCAPE, QUIT):
                pygame.quit()
                sys.exit()
            if event.type == pygame.locals.KEYDOWN:
                if event.key in (K_w, K_UP):
                    laoZhang.var_y = -10
                if event.key in (K_s, K_DOWN):
                    laoZhang.var_y = 10
                if event.key in (K_a, K_LEFT):
                    laoZhang.var_x = -10
                if event.key in (K_d, K_RIGHT):
                    laoZhang.var_x = 10
            laoZhang.update()
        updateDisplay()

if __name__ == "__main__":
    main()