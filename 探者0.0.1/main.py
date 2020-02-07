import sys,pygame
from pygame.locals import *
from Game import Game

def main():
    game = Game()
    game.initMainPage()
    # block = Game.MapBlock()
    # game.addSprite(block)
    
    pygame.mouse.set_cursor((8, 8), (4, 4), (24, 24, 24, 231, 231, 24, 24, 24), (0, 0, 0, 0, 0, 0, 0, 0))

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
                        game.playGame()
                        print('开始游戏')
                    elif i.name == '没有存档':
                        window = pygame.image.load('./src/image/弹出菜单.png').convert_alpha()
                        screenBackup = game.screen
                        game.screen.blit(window, (160, 105))
                        while True:
                            game.clock.tick(60)
                            f = False
                            for e in pygame.event.get():
                                if event.type == MOUSEBUTTONDOWN:
                                    pX, pY = pygame.mouse.get_pos()
                                    x, y = (795, 110)
                                    w, h = (10,10)
                                    # judge by math
                                    in_x = x - w/2 < pX < x + w/2
                                    in_y = y - h/2 < pY < y + h/2
                                    if in_x and in_y:
                                        f = True
                                        break
                                # 判断其他的事件
                            if f:
                                break
                            pygame.display.update()
                        game.screen = screenBackup
                        pygame.display.update()
                        # 试着做一个弹出的对话框
                        print('没有存档')
                    elif i.name == '继续游戏':
                        # 试着做一个弹出式对话框来读档
                        # game.archiveFile
                        print('继续游戏')
                    elif i.name == '成就':
                        # 跳转成就页
                        print('成就')
                    elif i.name == '设置':
                        # 对话框，设置页
                        print('设置')
            # 选择完成
        game.update()
        game.render()


if __name__ == "__main__":
    main()