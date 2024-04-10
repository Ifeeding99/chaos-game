import pygame
import os
import numpy as np
import math

pygame.init()
red = (230,50,50)
green = (0, 255, 0)
blue = (0, 0, 128)
brown = (127,64,0)
yellow = (255,255,0)
white = (255, 255, 255)
black = (0,0,0)
violet = (127,0,255)
info = pygame.display.Info()

screen = pygame.display.set_mode((int(info.current_w),int(info.current_h)), pygame.NOFRAME)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def draw_triangle():
    global A
    global B
    global C
    A = Point(683,10)
    B = Point(int(683-748*(math.sqrt(3)/4)), 758)
    C = Point(int(683+748*(math.sqrt(3)/4)), 758)
    pygame.draw.circle(screen,red, (A.x, A.y), 1)
    pygame.draw.circle(screen,red, (B.x, B.y), 1)
    pygame.draw.circle(screen,red, (C.x, C.y), 1)


def draw_points(steps):
    spx = np.random.randint(1,1367) #Startintg Point X
    spy = np.random.randint(1,769) #Starting Point Y
    start_point = (spx, spy)
    screen.set_at(start_point,white)
    c_p = Point(spx, spy) #Current Point
    for num in range(steps):
        screen.set_at((c_p.x, c_p.y), white)
        g_t_p = np.random.randint(1,4) #Go To Point
        if g_t_p == 1:
            M = Point(int((A.x + c_p.x)/2),int((A.y + c_p.y)/2))
            c_p.x = M.x
            c_p.y = M.y
            
        if g_t_p == 2:
            M = Point(int((B.x + c_p.x)/2),int((B.y + c_p.y)/2))
            c_p.x = M.x
            c_p.y = M.y

        if g_t_p == 3:
            M = Point(int((C.x + c_p.x)/2),int((C.y + c_p.y)/2))
            c_p.x = M.x
            c_p.y = M.y

    
x = np.random.randint(1,1367)
y = np.random.randint(1,769)
#draw_triangle()
#draw_points(100000)
running = True
while running:
    screen.fill(black) #UNCOMMENT THESE LINES TO GET MULTIPLE SIMULATIONS AT A TIME
    draw_triangle() #LEAVE screen.fill(black) IF U WANT A TRIANGLE THAT FILLS ITSELF
    draw_points(1000)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
            break
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                running = False
                break                
