import pygame
# fontAddress = "./src/font/ziti.ttf"
# gameFont = pygame.font.Font(fontAddress,70)

class Game:
    __width = 960
    __height = 640
    spriteList = pygame.sprite.Group()
    fontAddress = "./src/font/ziti.ttf"
    pygame.font.init()
    gameFont = pygame.font.Font(fontAddress,40)

    # 初始化的时候需要做的事情
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.__width,self.__height))
        pygame.display.set_caption("探者")
        self.clock = pygame.time.Clock()
    
    # 初始化游戏主页面
    def initMainPage(self):
        # 背景绘制
        self.buttonList = pygame.sprite.Group()
        bgImage = pygame.image.load("./src/background.png")
        self.screen.blit(bgImage,(0,0))

        # 菜单绘制
        names = ['开始游戏','继续游戏','成就','设置']
        for i in range(0,4):
            button = Button(names[i],(744,158+i*108))
            self.buttonList.add(button)
        print(self.buttonList.sprites())
        self.buttonList.draw(self.screen)

        pygame.display.flip()
    
    # 

    # def __call__(self):
    #     pass

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

# 地图块类
class MapBlock(pygame.sprite.Sprite):
    
    def __init__(self):
        # 初始化的时候需要先调用父类的初始化函数
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("./src/up.png")
        self.rect = self.image.get_rect()
        self.rect.center = (320,33)
    
    def update(self):
        pass

# 按钮类
class Button(pygame.sprite.Sprite):
    def __init__(self,name,location):
        # 初始化的时候需要先调用父类的初始化函数
        pygame.sprite.Sprite.__init__(self)
        self.imageUp = pygame.image.load("./src/buttonUp.png")
        self.imageDown = pygame.image.load("./src/buttonDown.png")
        self.image = self.imageUp
        self.rect = self.imageUp.get_rect()
        # self.rect.center = 
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

        itemName = Game.gameFont.render(self.name, True, (0,0,0))
        i,j = Game.gameFont.size(self.name)
        pos = (x-i/2, y-j/2)
        if self.isOver():
            screen.blit(self.imageDown, (x-w/2, y-h/2))
            screen.blit(itemName, pos)
            return True
        else:
            screen.blit(self.imageUp, (x-w/2, y-h/2))
            screen.blit(itemName, pos)
            return False


# 开始游戏
# 继续游戏
#     存档
# 成就
# 设置
