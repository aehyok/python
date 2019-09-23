## 导入相关模块
import random
import pygame
import sys
import os

from pygame.locals import *

windows_width = 800
windows_height = 600 #游戏窗口的大小
cell_size = 20       #贪吃蛇身体方块大小,注意身体大小必须能被窗口长宽整除

''' 初始化区
有大小尺寸的, 因此地图的尺寸而言的
'''
map_width = int(windows_width / cell_size)
map_height = int(windows_height / cell_size)

sourceData = ['a','b','c','d','e','f','g','h','i','j','k','l','m']

keyBoardData={65:'a',66:'b',67:'c',68:'d',69:'e',70:'f',71:'g',72:'h'}
# 颜色定义
white = (255, 255, 255)
black = (0, 0, 0)
gray = (230, 230, 230)
dark_gray = (40, 40, 40)
DARKGreen = (0, 155, 0)
Green = (0, 255, 0)
Red = (255, 0, 0)
blue = (0, 0, 255)
dark_blue =(0,0, 139)


#游戏背景颜色
BG_COLOR = black 


def main():

    pygame.init() # 模块初始化
    clocker=pygame.time.Clock() # 创建Pygame时钟对象
    screen = pygame.display.set_mode((windows_width, windows_height)) #居中实现难度比较大
    screen.fill(black)
    pygame.display.set_caption("2019-09-23-字母数字小游戏") #设置标题

    show_start_info(screen)
    print('游戏开始了哟')
    while True:
        running_game(screen,clocker)

#开始页显示信息
def show_start_info(screen):
    
    
    font = pygame.font.Font('myfont.ttf', 40)
    tip = font.render('按任意键开始游戏~~~', True, (65, 105, 225))
    gamestart = pygame.image.load('gamestart.png')
    screen.blit(gamestart, (140, 30))
    screen.blit(tip, (240, 550))
    pygame.display.update()

    while True:  #键盘监听事件
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()   #终止程序
            elif event.type ==KEYDOWN:
                if(event.key ==K_ESCAPE):
                    terminate()  #终止程序
                else:
                    return     #结束此函数


#游戏主体运行
def running_game(screen,clocker):
    coords=[]
    while True:  #键盘监听事件
        screen.fill(BG_COLOR)  # 屏幕填充黑色
        
        startx = random.randint(10, windows_width - 10)
        starty = 1
    
        index=random.randint(0,10)
        coords.insert(0,{'x': startx, 'y': starty,'value':sourceData[index]})

        font = pygame.font.Font('myfont.ttf', 30)


        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()   #终止程序
            elif event.type ==KEYDOWN:
                if(event.key ==K_ESCAPE):
                    terminate()  #终止程序
                else:
                    i=0
                    value= keyBoardData[event.key]
                    
                    
                    for coord in coords:

                        if(coord['value'] ==value):
                            coords.remove(coord)
                            break
                        i=i+1    
        clocker.tick(0.3) #控制fps
        newCoords=[]
        #数据下移
        for coord in coords:
            coord['y']=coord['y']+50
        screen.fill(BG_COLOR)  # 屏幕填充黑色
        for coord in coords:  
            scoreSurf = font.render('%s' % coord['value'], True, Green)
            scoreRect = scoreSurf.get_rect()
            scoreRect.topleft = (coord['x'], coord['y'])
            screen.blit(scoreSurf, scoreRect)
                    
        pygame.display.update()


        
#程序终止
def terminate():
    pygame.quit()
    os._exit(1) 

main()