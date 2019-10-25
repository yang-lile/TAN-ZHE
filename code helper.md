# 常用代码使用说明书

*插播一个学习markdown的地址：https://zhuanlan.zhihu.com/p/56943330*

*再插播一个声明：*
>本使用说明仅使用于python3.7.4环境下的pygame1.9.6，版本更新后内容可能改变，请以实际情况为主，落后版本可能也会有出入，特别是python2。

>## 导入模块

这个比较简单，我随便说说，使用import导入，代码如下：

```python
import pygame
from pygame.locals import *
```

>## 基本代码框架

作为一个游戏，代码框架很固定化，以我的想法，分为：

1. 初始化
   1. 变量
   2. 类定义
   3. 绘图
   4. 等等一类的准备事件
2. 事件处理
   1. 键盘事件
   2. 鼠标事件
3. 逻辑实现
   1. 图像处理的逻辑
   2. 流程控制的逻辑
   3. 细节逻辑

对于我们的代码，我的要求是，**规范化的开发**。

```python
# 导入需要的包
import ...

# 进入主函数（两种写发，我们选用这个）
def main():
    pass    # 主函数

if __name__ == "__main__":
    main()  # 调用主函数
```

```python
# 现在讲讲主函数里的东西
def main():
    # 做一些初始化的行为
    while True:     # 事件处理入口
        for event in pygame.event.get():    # 获取事件
            if event.type == QUIT:
                # 该句代码为必备的用于退出游戏的代码
                # 检测事件类型为QUIT之后
                pygame.quit()   # 退出游戏
                sys.exit()      # 退出程序
                # 必须写，不然无法退出
            # 其他事件处理，例：
            if event.type == KEYDOWN:
                pass
        # 处理完事件后一定要刷新屏幕
        pygame.display.update()
            
```

>## 定义屏幕大小

这里使用的是`screen`，实际我们用的全局变量里的`GL.screen`，而且一次定义终身使用23333，所以这个作为了解。

```python
screen = pygame.display.set_mode((length,width))
# 注意，里面是一个元组类型，没有括号会报错，
# 所以我也在某block文件内的init方法上，使用了这个方法。
```
>## 定义一个字体类型

主要用于我们游戏内的字体格式统一编辑，**但是参数我还没学清楚，对，一个大坑。** 所以这里的演示代码只是其中比较简单的用法。

```python
fontXxx = pygame.font.Font(a,b)
# a是文件名
# b是字体大小
```

a也可以是已经内置的“黑体”，“宋体”，但由于部分系统没有这些预置字体，我们需要使用我们自己的字体，tff格式字体下载好后，以代码中所给的格式写上就可以使用了。

注： fontXxx的意思是：font类型 + Xxx的驼峰变量名（以后不再提示）

>## 生成文字的图片

**因为游戏里的图片渲染速度比单独的文字渲染快** ，所以要把说的话转成图片方便快速刷新地图。

```python
picXxx = fontXxx.render("something", True, fntColor, bgColor)
# 参数分别为：内容，是否抗锯齿，前景色（文字色），背景色（默认为透明）
```

抗锯齿是因为渲染程度深浅所致，你可以自己试试False的样子有多难看（但很像素感哦！！！附议。）

>## 准备界面背景

有两个函数可以实现，我开发的时候没有图片只能自己用单一颜色填充：

```python
screen.fill(Color)
```

这廉价感。。。所以我们使用这个（可以加载图片）：

```python
screen.blit(picXxx, location)
```

凭感觉，location应该还是那个表示坐标的二元组23333,所以设置一张大图就不管太多（使用(0, 0)来作为坐标）

**说实话，这个函数我还没正式了解，坑x2**

>## 使目标居中

原理是获取图片对象的rect属性，然后该属性是一个类，通过修改这个类的center属性的值，使其中心位置位于屏幕的某处

```python
rectXxx = picXxx.get_rect()
rectXxx.center = (坐标)
```

**又一个坑！！！** 算了，有时间再搞它。这个暂时用不了了。

***以上为目前使用的pygame代码，如有缺漏。再说。***

