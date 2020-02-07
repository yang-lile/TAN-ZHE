import pygame,sys
from pygame.locals import *

FPS = 60

class mySprite(pygame.sprite.Sprite):
    def __init__(self,pos,image):
        pygame.sprite.Sprite.__init__(self)
        self.pos = pos
        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()
        print(self.rect)
        
    def update(self):
        self.pos = (self.pos[0]+10,self.pos[1])


def main():
    screen = pygame.display.set_mode((940,640))
    fpsClock = pygame.time.Clock()

    dong = mySprite((50,0),"./dongdongB.png")
    g = pygame.sprite.Group()
    g.add(dong)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        
        g.draw(screen)
        pygame.display.update(g.sprites())
        fpsClock.tick(FPS)

if __name__ == "__main__":
    main()