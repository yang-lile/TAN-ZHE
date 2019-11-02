import pygame
import pygame.locals

FPS = 60

def main():
    sceen = pygame.display.set_mode((1080,960))
    sceen.fill((11,11,11))
    fpsClock = pygame.time.Clock()
    pygame.key.set_repeat(10, 10)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.locals.KEYDOWN:
                print("y")
            else:
                print("n")
        pygame.display.update()
        fpsClock.tick(FPS)

if __name__ == "__main__":
    main()