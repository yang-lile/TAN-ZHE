import pygame,sys
from pygame.locals import *

if __name__ == "__main__":
    screen = pygame.display.set_mode((1080,960))
    screen.fill((125,125,125))

    upImage = pygame.image.load("up.png").convert_alpha()
    screen.blit(upImage,(0,0))

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                x,y = event.pos
                rectUpImage = upImage.get_rect()
                rectUpImage.center = (x,y)
                screen.blit(upImage,(x,y))
        pygame.display.update()

