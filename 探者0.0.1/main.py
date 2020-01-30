import sys,pygame
from pygame.locals import *
from Game import Game

def main():
    game = Game()
    game.initMainPage()
    # block = Game.MapBlock()
    # game.addSprite(block)
    
    while True:
        game.clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            # 选择菜单项目
            for i in game.buttonList.sprites():
                flag = i.render(game.screen)
                if flag and event.type == MOUSEBUTTONDOWN:
                    if i.name == '开始游戏':
                        
                        print('开始游戏')
                    elif i.name == '继续游戏':
                        print('继续游戏')
                    elif i.name == '成就':
                        print('成就')
                    elif i.name == '设置':
                        print('设置')
            # 选择完成
        game.update()
        game.render()


if __name__ == "__main__":
    main()