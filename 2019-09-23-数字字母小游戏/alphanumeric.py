## 导入相关模块
import random
import pygame
import sys
import os

from pygame.locals import *

windows_width = 800
windows_height = 600 #游戏窗口的大小
cell_size = 20       #贪吃蛇身体方块大小,注意身体大小必须能被窗口长宽整除

sourceData = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

keyBoardData={48:'0',49:'1',50:'2',51:'3',52:'4',53:'5',54:'6',55:'7',56:'8',57:'9',
                97:'a',98:'b',99:'c',100:'d',101:'e',102:'f',103:'g',104:'h',105:'i',106:'j',
                107:'k',108:'l',109:'m',110:'n',111:'o',112:'p',113:'q',114:'r',115:'s',116:'t',
                117:'u',118:'v',119:'w',120:'x',121:'y',122:'z'}

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

successTimes=0
perSuccessScore=5
failTimes=0
perFailScore=5

#游戏背景颜色
BG_COLOR = black 

def main():
    pygame.init() # 模块初始化
    clocker=pygame.time.Clock() # 创建Pygame时钟对象
    screen = pygame.display.set_mode((windows_width, windows_height)) #居中实现难度比较大
    screen.fill(black)
    pygame.display.set_caption("2019-09-23-字母数字小游戏") #设置标题

    show_start_info(screen)
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
        pygame.draw.line(screen, white, (100, 0), (100, 600), 1) 
        pygame.draw.line(screen, white, (700, 0), (700, 600), 1)    
        startx = random.randint(100, windows_width - 100)
        starty = 1 
        index=random.randint(0,35)
        coords.insert(0,{'x': startx, 'y': starty,'value':sourceData[index]})
        font = pygame.font.Font('myfont.ttf', 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()   #终止程序
            elif event.type ==KEYDOWN:
                if(event.key ==K_ESCAPE):
                    terminate()  #终止程序
                else:
                    global successTimes
                    global failTimes
                    #判断按键是否与显示值匹配，并计算成绩
                    index=0
                    delBool=False
                    if(event.key>=48 and event.key<=57) or (event.key>=97 and event.key<=122):
                        value= keyBoardData[event.key]
                        for coord in coords:
                            if(coord['value'] ==value):
                                coords.remove(coord)
                                successTimes+=1
                                delBool=True
                                #show_result_info(screen,"+")   #匹配加分
                                break
                        if(delBool==False):
                            failTimes+=1

                    else:
                        failTimes+=1
                    #show_result_info(screen,"-")   #没有匹配减分
        clocker.tick(1) #每秒钟一次刷新
        newCoords=[]
        #数据下移
        for coord in coords:
            coord['y']=coord['y']+16
        for coord in coords:  
            scoreSurf = font.render('%s' % coord['value'], True, Green)
            scoreRect = scoreSurf.get_rect()
            scoreRect.topleft = (coord['x'], coord['y'])
            screen.blit(scoreSurf, scoreRect)    

        show_result_info(screen)            
        pygame.display.update()

#成绩输出
def show_result_info(screen):
    score=perSuccessScore*successTimes-perFailScore*failTimes
    font = pygame.font.Font('myfont.ttf', 20)
    scoreSurf = font.render('总分数%s' %score, True, Red)
    scoreRect = scoreSurf.get_rect()
    scoreRect.topleft = (702, 50)
    screen.blit(scoreSurf, scoreRect)

    succeSurf=font.render('成功次数：%s' %successTimes,True,Red)
    succeRect=succeSurf.get_rect()
    succeRect.topleft = (702, 80)
    screen.blit(succeSurf, succeRect)    

    failSurf=font.render('失败次数：%s' %failTimes,True,Red)
    failRect=succeSurf.get_rect()
    failRect.topleft = (702, 120)
    screen.blit(failSurf, failRect)  

#程序终止
def terminate():
    pygame.quit()
    os._exit(1) 

main()