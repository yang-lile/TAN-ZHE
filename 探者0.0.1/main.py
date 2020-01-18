import sys,pygame
from pygame.locals import *
import Game

def main():
    game = Game.Game()
    block = Game.MapBlock()
    game.addSprite(block)
    
    while True:
        game.clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        
        game.update()
        game.render()


if __name__ == "__main__":
    main()