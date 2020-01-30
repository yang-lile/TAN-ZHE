import pygame, sys
from pygame.locals import *

class Block:
    # 通过id来判断是哪个色块人物物品等
    id = 0
    # position使用的是坐标
    def __init__(self, colorImage, position):
        self.colorImage = pygame.image.load(colorImage).convert_alpha()
        self.position = position
    # 绘制函数不具有绘制到正面的能力，只是现在背面绘制，然后全部绘制完后再翻面
    def render(self, myMap):
        w, h = self.colorImage.get_size()
        x, y = self.position
        myMap.blit(self.colorImage, (x-w/2, y-h/2))

class MapBlock(Block):
    # position使用的是下标
    def __init__(self, position):
        a, b = position
        self.position = (a*40+20, b*40+20)
# 要求人类的色块为40*80的大小，否则重写该函数的render
class PeopleBlock(Block):
    # position使用的是人物脚的下标（下半身中点的下标）
    def __init__(self, position):
        a, b = position
        self.position = (a*40+20, b*40)
    # 特制的绘制函数
    def render(self, myMap):
        w, h = self.colorImage.get_size()
        x, y = self.position
        myMap.blit(self.colorImage, (x-w/2, y-h/2))

# 通过以下类来绘制色块
class BlockGreen(MapBlock):
    id = 1
    def __init__(self, position):
        super(BlockGreen, self).__init__(position)
        self.colorImage = pygame.image.load("src/ColorBlock/greenImage.png")
class BlockBlue(MapBlock):
    id = 2
    def __init__(self, position):
        super(BlockBlue, self).__init__(position)
        self.colorImage = pygame.image.load("src/ColorBlock/blueImage.png")
class BlockPurple(MapBlock):
    id = 3
    def __init__(self, position):
        super(BlockPurple, self).__init__(position)
        self.colorImage = pygame.image.load("src/ColorBlock/purpleImage.png")
class BlockRed(MapBlock):
    id = 4
    def __init__(self, position):
        super(BlockRed, self).__init__(position)
        self.colorImage = pygame.image.load("src/ColorBlock/redImage.png")
class BlockYellow(MapBlock):
    id = 5
    def __init__(self, position):
        super(BlockYellow, self).__init__(position)
        self.colorImage = pygame.image.load("src/ColorBlock/yellowImage.png")
class BlockGray(MapBlock):
    id = 6
    def __init__(self, position):
        super(BlockGray, self).__init__(position)
        self.colorImage = pygame.image.load("src/ColorBlock/grayImage.png")
class BlockPeople(MapBlock):# 这是一个假人40*40的，可以理解为色块人
    id = 7
    def __init__(self, position):
        super(BlockPeople, self).__init__(position)
        self.colorImage = pygame.image.load("src/ColorBlock/people1Image.png")
# 监狱头子的正面图
class BlockYangRenyuFront(PeopleBlock):
    id = 11
    def __init__(self, position):
        super(BlockYangRenyuFront, self).__init__(position)
        self.colorImage = pygame.image.load("src/image/监狱头子.png")

class ManagerBlock:
    blockList = [
        BlockBlue,
        BlockGray,
        BlockGreen,
        BlockPurple,
        BlockRed,
        BlockYellow,
        BlockPeople,
        BlockYangRenyuFront,
    ]

    def findBlock2Create(self, id):
        for i in self.blockList:
            if i.id == id:
                return i

__GameMap = {
    "牢房1":{
        "地图":
            [
                [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, ],
                [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, ],
                [6, 6, 6, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 6, 6, 6, 6, 6, ],
                [6, 6, 6, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 6, 6, 6, 6, 6, ],
                [6, 6, 6, 2, 2, 1, 4, 4, 1, 4, 4, 1, 4, 4, 1, 4, 4, 1, 7, 6, 6, 6, 6, 6, ],
                [6, 6, 6, 2, 2, 1, 4, 4, 1, 4, 4, 1, 4, 4, 1, 4, 4, 1, 7, 6, 6, 6, 6, 6, ],
                [6, 6, 6, 2, 2, 1, 4, 4, 1, 4, 4, 1, 4, 4, 1, 4, 4, 1, 7, 6, 6, 6, 6, 6, ],
                [6, 6, 6, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 7, 6, 6, 6, 6, 6, ],
                [6, 6, 6, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 7, 6, 6, 6, 6, 6, ],
                [6, 6, 6, 2, 2, 4, 4, 1, 4, 4, 1, 4, 4, 1, 4, 4, 1, 1, 7, 6, 6, 6, 6, 6, ],
                [6, 6, 6, 2, 2, 4, 4, 1, 4, 4, 1, 4, 4, 1, 4, 4, 1, 1, 7, 6, 6, 6, 6, 6, ],
                [6, 6, 6, 2, 2, 4, 4, 1, 4, 4, 1, 4, 4, 1, 4, 4, 1, 1, 7, 6, 6, 6, 6, 6, ],
                [6, 6, 6, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 6, 6, 6, 6, 6, ],
                [6, 6, 6, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 6, 6, 6, 6, 6, ],
                [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, ],
                [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, ],
            ],
        "人物":[]
    },
    # 添加其他的地图
}

if __name__ == "__main__":
    screen = pygame.display.set_mode((960, 640))
    screen.fill((0,0,0))
    MB = ManagerBlock()
    for i in range(0,16):
        for j in range(0,24):
            block = MB.findBlock2Create(__GameMap['牢房1']['地图'][i][j])((j,i))
            block.render(screen)
    block = BlockYangRenyuFront((3,4))
    block.render(screen)
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
