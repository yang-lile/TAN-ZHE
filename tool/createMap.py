import pygame,sys
from pygame.locals import *
import mapBlock

# screen = mapBlock.GL.screen
# ...
# 一个用来画地图的程序，主要是懒。。。
# 其次，这也是个大坑啊。。。

def updateMap(i,j):
    if initMap[i][j] == 1:
        block = mapBlock.BlockGreen((j*40+20,i*40+20))
    elif initMap[i][j] == 2:
        block = mapBlock.BlockBlue((j*40+20,i*40+20))
    elif initMap[i][j] == 3:
        block = mapBlock.BlockPurple((j*40+20,i*40+20))
    elif initMap[i][j] == 4:
        block = mapBlock.BlockRed((j*40+20,i*40+20))
    elif initMap[i][j] == 5:
        block = mapBlock.BlockYellow((j*40+20,i*40+20))
    elif initMap[i][j] == 6:
        block = mapBlock.BlockGray((j*40+20,i*40+20))
    elif initMap[i][j] == 7:
        block = mapBlock.BlockPeople((j*40+20,i*40+20))
    else:
        print("反正出bug了我也不会修")
    block.render(screen)

def printMap():
    print('地图：')
    print('[')
    for i in range(0,16):
        print('[',end='')
        for j in range(0,24):
            print(str(initMap[i][j])+', ',end='')
        print('],')
    print(']')

def changeBlock(x,y,flag):
    b = x//40
    if b >= 24:
        a = (y-10)//60
        if a == 0:
            printMap()
        else:
            flag = a
    else:
        a = y//40
        initMap[a][b] = flag
        print(initMap[a][b])
        updateMap()

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((1080,640))

    screen.fill((0,0,0))
    # initMap = [
    #     [1,]*24
    # ]*16
    initMap = [
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    ]
    for i in range(0,16):
        for j in range(0,24):
            updateMap(i,j)

    # use to found a block named 'save'
    block = mapBlock.BlockSave((1020,40))
    block.render(screen)
    # color block
    block = mapBlock.BlockGreen((1020,100))
    block.render(screen)
    block = mapBlock.BlockBlue((1020,160))
    block.render(screen)
    block = mapBlock.BlockPurple((1020,220))
    block.render(screen)
    block = mapBlock.BlockRed((1020,280))
    block.render(screen)
    block = mapBlock.BlockYellow((1020,340))
    block.render(screen)
    block = mapBlock.BlockGray((1020,400))
    block.render(screen)
    block = mapBlock.BlockPeople((1020,460))
    block.render(screen)

    pygame.display.update()

    clock = pygame.time.Clock()     # use to set flash speed
    flag = 1        # use to save color
    isMove = False
    while True:
        clock.tick(60)      # 60帧
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                keys = pygame.key.get_pressed()
                if keys[K_s] and keys[K_LCTRL]:
                    printMap()
            # mouse motion
            if event.type == MOUSEBUTTONDOWN:
                x,y = event.pos
                # changeBlock
                b = x//40
                if b >= 24:
                    a = (y-10)//60
                    if a == 0:
                        printMap()
                    else:
                        flag = a
                else:
                    isMove = True
                    a = y//40
                    initMap[a][b] = flag
                    print(initMap[a][b])
                    updateMap(a,b)
                # changBlock finish
            if event.type == MOUSEBUTTONUP:
                isMove = False
            if event.type == MOUSEMOTION:
                if isMove:
                    x,y = event.pos
                    # changeBlock
                    b = x//40
                    if b >= 24:
                        print("憨憨，这都能移出去")
                    else:
                        a = y//40
                        initMap[a][b] = flag
                        print(initMap[a][b])
                        updateMap(a,b)
                    # changBlock finish
                    
        pygame.display.update()
