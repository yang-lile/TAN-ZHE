#
# @Time         : 2019/9/23 下午2:43
# @Author       : 礼lua
# @Modify Log   : insert L54-L71
# @todoList     : 1.use manGame.run to run the game
#
import pygame, sys
# import pygame constant
from pygame.locals import *
from globalValue import GL

def main():# 你可能没学过，但不难理解，这是一个主函数，整个程序的入口
    # pygame init
    # it is a start of game
    pygame.init()

    # define size of font
    themeFont = pygame.font.Font(GL.cusFontAddress, 100)
    themeName = themeFont.render("姑姑咕咕", True, GL.BLACK)
    # try centered
    themeRec = themeName.get_rect()
    themeRec.center = (GL.scrLength/2, GL.scrWidth/4)
    
    # define size of item
    # itemFont = pygame.font.Font(cusFontAddress, 30)
    from Button import Button
    btItem = [0]*5       # ???我也不知道怎么办
    btItem[0] = Button("src/itemImage/开始游戏up.png", "src/itemImage/开始游戏down.png", (GL.scrLength/2, 300))
    btItem[1] = Button("src/itemImage/继续游戏up.png", "src/itemImage/继续游戏down.png", (GL.scrLength/2, 370))
    btItem[2] = Button("src/itemImage/帮助up.png", "src/itemImage/帮助down.png", (GL.scrLength/2, 440))
    btItem[3] = Button("src/itemImage/关于up.png", "src/itemImage/关于down.png", (GL.scrLength/2, 510))
    btItem[4] = Button("src/itemImage/退出up.png", "src/itemImage/退出down.png", (GL.scrLength/2, 580))

    # define screen background picture
    bg = pygame.image.load("src/bgpicture.png")
    GL.screen.blit(bg, (0,0))
    # load game name to screen
    GL.screen.blit(themeName, themeRec)
    # load item
    for i in range(0,5):
        btItem[i].render()

    # keep running of program
    while True:
        # monitor events
        for event in pygame.event.get(): 
            # quit event
            if event.type in (QUIT, ):
                # quit the game but I don't know why need two statement
                pygame.quit()
                sys.exit()
            for i in range(0,5):
                flag = btItem[i].render()
                if flag and event.type == MOUSEBUTTONDOWN:
                    if i == 0:
                        from mainGame import run
                        run()
                    elif i == 1:
                        print("读档中。。。")
                        print("继续游戏～")
                    elif i == 2:
                        print("帮助～")
                        print("反正也没人看/")
                    elif i == 3:
                        print("开发人员：")
                        print("孙Sir")
                        print("张Sir")
                        print("杨头子")
                    elif i == 4:
                        pygame.quit()
                        sys.exit()
                    else:
                        print("Bug!!!")

        pygame.display.update()

if __name__ == "__main__":
    # 这是判断是否当前代码为主函数，
    # 即pyhton编译的程序
    # 若不是，则文件内的代码不会执行
    main()
