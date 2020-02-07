import os,fnmatch,glob
import pygame
import mapBlock

class Game:
    __width = 960
    __height = 640
    # 测试使用的精灵
    spriteList = pygame.sprite.Group()
    # 字体模块的初始化
    __fontAddress = "./src/font/OPPOSans-L.ttf"
    pygame.font.init()
    gameFont = pygame.font.Font(__fontAddress,40)
    # 判断是否有存档，默认为否
    archive = False
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

    # 初始化的时候需要做的事情
    def __init__(self):
        pygame.init()
        # 读档，并设置archive为True
        self.archiveFile = glob.glob('userData/game_*_backup.data')
        if self.archiveFile:
            self.archive = True
        self.screen = pygame.display.set_mode((self.__width,self.__height))
        pygame.display.set_caption("探者")
        self.clock = pygame.time.Clock()
    
    # 初始化游戏主页面
    def initMainPage(self):
        # 背景绘制
        self.buttonList = pygame.sprite.Group()
        bgImage = pygame.image.load("./src/image/background.png")
        self.screen.blit(bgImage,(0,0))

        # 菜单绘制
        names = ["开始游戏","继续游戏","成就","设置"]
        if self.archive == False:
            names[1] = "没有存档"
        for i in range(0,4):
            button = Button(names[i],(744,158+i*108))
            self.buttonList.add(button)
        self.buttonList.draw(self.screen)

        pygame.display.flip()
    
    # 初始化游戏地图，传入地图参数，人物精灵组
    # 只绘制
    def initMap(self,mapNum):# 第一张地图传入数据"牢房1"
        # 绘制地图到备份底图
        self.__screenMap = self.screen
        # 初始化色块管理器
        MB = ManagerBlock()
        for i in range(0,16):
            for j in range(0,24):
                block = MB.findBlock2Create(self.__GameMap['牢房1']['地图'][i][j])((j,i))
            block.render(self.__screenMap)
        # 绘制人物
        for people in self.__GameMap[mapNum]['人物']:
            people.render(self.__screenMap)
        # 大绘制反转更新
        self.screen.flip()
    
    # 开始游戏
    def playGame(self, flag = False):
        # 读取游戏存档
        if flag:
            archiveList = []
            for f_name in os.listdir("./userData"):
                if fnmatch.fnmatch(f_name,"game_*_backup.data"):
                    archiveList.append(f_name)
        # 数据读取到了之后加载出来
        self.initMap("牢房1")
        while True:
            self.clock.Clock(60)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                self.screen
    
    # 对整个游戏进行渲染
    def render(self):
        # 在进行下面的操作之前，先初始化地图
        self.spriteList.draw(self.screen)
        pygame.display.flip()

    # 对整个游戏进行更新
    def update(self):
        self.spriteList.update()
        pygame.display.update()
    
    # 当用户调整游戏窗口大小的时候调用
    # def resize(self,size):
    #     self.canvasSize = size
    #     self.canvas = pygame.display.set_mode(size)
    
    def addSprite(self,sprite):
        self.spriteList.add(sprite)
        self.update()
        self.render()

# 按钮类
class Button(pygame.sprite.Sprite):
    def __init__(self,name,location):
        # 初始化的时候需要先调用父类的初始化函数
        pygame.sprite.Sprite.__init__(self)
        self.imageUp = pygame.image.load("./src/image/buttonUp.png")
        self.imageDown = pygame.image.load("./src/image/buttonDown.png")
        self.image = self.imageUp
        self.rect = self.imageUp.get_rect()
        self.rect.center = location
        self.name = name

    def update(self):
        pass
    
    # 判断鼠标是否在按钮上
    def isOver(self):
        pX, pY = pygame.mouse.get_pos()
        x, y = self.rect.center
        w, h = self.imageUp.get_size()
        # judge by math
        in_x = x - w/2 < pX < x + w/2
        in_y = y - h/2 < pY < y + h/2
        return in_x and in_y

    def render(self,screen):
        w, h = self.imageUp.get_size()
        x, y = self.rect.center

        Game.gameFont.set_bold(True)
        itemName = Game.gameFont.render(self.name, True, (0,0,0))
        i, j = Game.gameFont.size(self.name)
        pos = (x-i/2, y-j/2)
        if self.isOver():
            screen.blit(self.imageDown, (x-w/2, y-h/2))
            screen.blit(itemName, pos)
            return True
        else:
            screen.blit(self.imageUp, (x-w/2, y-h/2))
            screen.blit(itemName, pos)
            return False
