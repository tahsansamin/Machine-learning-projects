import pygame
from pygame.locals import *
import time
pygame.init()
import random
screen = pygame.display.set_mode((500,500))
import os
import sys
import threading
file = 'D:/sample_game.py'
red = (255,0,0)
game_over = False
player_speed = 40
x = 210
y = 400
fps = 60
enemy_speed = 5
space_shuttle = pygame.image.load('D:/DOCUMENTS/Downloads/transport.png')
myfont = pygame.font.SysFont('Comic Sans MS',50)
newfont = pygame.font.SysFont('bahaus 93',30)
player_sprite = pygame.image.load('D:/DOCUMENTS/Downloads/space-shuttle.png')
#five enemies
x1 = random.randint(0,500)
e_y = 0
e2_y = 0
e3_y = 0
e4_y = 0
e5_y = 0
x2 = random.randint(0,500-5)
x3 = random.randint(0,500-5)
x4 = random.randint(0,500-5)
x5 = random.randint(0,500-5)

color = (163,144,106)
size = 100


screen.fill((255,255,255))
textsurface = myfont.render('Space Dodgers',False,(0,255,0))
instruct_text = newfont.render('Press space to start',False,(255,50,20))
screen.blit(instruct_text,(150,200))
screen.blit(textsurface,(100,130))
screen.blit(space_shuttle,(100,250))
                
pygame.display.flip()

clock = pygame.time.Clock()


def increase_difficulty():
    global enemy_speed
    while True:
        time.sleep(10)
        enemy_speed += 2


def restart(sc,enemy_y,player_x):
    print(sc)
    retry = input('GAME OVER DO YOU WANT TO RETRY[YES,NO]')
    if retry == 'Yes':
        enemy_y = 0
        player_x = 210
        sc = 0
        game_loop()
    sys.exit
        
def game_loop():
    start_incrdiff = threading.Thread(target=increase_difficulty)
    start_incrdiff.start()
    global x1
    global y
    global e_y
    global e2_y
    global e3_y
    global e4_y
    global e5_y
    global color
    global size
    
    global x
    global x2
    global x3
    global x4
    global x5

    score = 0
    game_f = True    
    
    while game_f:
        e_y += enemy_speed
        current_score = 'Score:' + str(score)
        score_text = newfont.render(current_score,False,(136,85,95))
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    x -= player_speed
                if event.key == K_RIGHT:
                    x += player_speed
            if x >= 500-59 or x < 0:
                print(score)
                retry=input('GAME OVER DO YOU WANT TO RETRY[Yes,No]')
                if retry == 'No':
                    sys.exit()
                if retry == 'Yes':
                    x = 210
                    e_y = 0
                    score = 0
                    game_loop()
        if x > x1 and x<x1+50 and y>e_y and y < e_y+50 or x1 > x and x1 < x+50 and e_y > y and e_y < y+50:
            print(score)
            retry=input('GAME OVER DO YOU WANT TO RETRY[Yes,No]')
            if retry == 'No':
                sys.exit()
            if retry == 'Yes':
                x = 210
                e_y = 0
                score = 0
                game_loop()
        if x > x2 and x<x2+50 and y>e_y and y < e_y+50 or x2 > x and x2 < x+50 and e_y > y and e_y < y+50:
            

            print(score)
            retry=input('GAME OVER DO YOU WANT TO RETRY[Yes,No]')
            if retry == 'No':
                sys.exit()
            if retry == 'Yes':
                x = 210
                e_y = 0
                score = 0
                game_loop()
        if x > x3 and x<x3+50 and y>e_y and y < e_y+50 or x3 > x and x3 < x+50 and e_y > y and e_y < y+50:

            print(score)
            retry=input('GAME OVER DO YOU WANT TO RETRY[Yes,No]')
            if retry == 'No':
                sys.exit()
            if retry == 'Yes':
                x = 210
                e_y = 0
                score = 0
                game_loop()
        if x > x4 and x<x4+50 and y>e_y and y < e_y+50 or x4 > x and x4 < x+50 and e_y > y and e_y < y+50:
            print(score)
            retry=input('GAME OVER DO YOU WANT TO RETRY[Yes,No]')
            if retry == 'No':
                sys.exit()
            if retry == 'Yes':
                x = 210
                e_y = 0
                score = 0
                game_loop()
        if x > x5 and x<x5+50 and y>e_y and y < e_y+50 or x5 > x and x5 < x+50 and e_y > y and e_y < y+50:
            print(score)
            retry=input('GAME OVER DO YOU WANT TO RETRY[Yes,No]')
            if retry == 'No':
                sys.exit()
            if retry == 'Yes':
                x = 210
                e_y = 0
                score = 0
                game_loop()
        
        if e_y > y:
            score+=1
                
                
        clock.tick(fps)
        screen.fill((255,255,255))
        pygame.draw.rect(screen,color,(x1,e_y,50,50))
        pygame.draw.rect(screen,color,(x2,e_y,50,50))
        pygame.draw.rect(screen,color,(x3,e_y,50,50))
        pygame.draw.rect(screen,color,(x4,e_y,50,50))
        pygame.draw.rect(screen,color,(x5,e_y,50,50))
        if e_y >= 500:
            e_y = 0
            x1 = random.randint(0,500)
            x2 = random.randint(0,500-5)
            x3 = random.randint(0,500-5)
            x4 = random.randint(0,500-5)
            x5 = random.randint(0,500-5)
        screen.blit(score_text,(350,2))
        pygame.draw.rect(screen,(255,0,00),(x,y,50,50))
        pygame.display.flip()
        pygame.display.update()
       
while  True:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                print(event.key)
                
                
                game_loop()
    pygame.display.flip()
        
                
                
    





                
