import pygame

class Game:
    __width = 640
    __height = 480
    spriteList = pygame.sprite.Group()

    # 初始化的时候需要做的事情
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.__width,self.__height))
        pygame.display.set_caption("探者")
        self.clock = pygame.time.Clock()
    
    def initBg(self,screen):
        self.screen = screen

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

class MapBlock(pygame.sprite.Sprite):
    
    def __init__(self):
        # 初始化的时候需要先调用父类的初始化函数
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("./src/loading.gif")
        self.rect = self.image.get_rect()
        self.rect.center = (320,33)
    
    def update(self):
        pass