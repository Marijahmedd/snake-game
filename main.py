import pygame
import random
pygame.init()
from pygame.locals import *

#DISPLAY

s_width=900
s_height=600
mainwindow = pygame.display.set_mode((s_width, s_height))
pygame.display.set_caption("Snake's Frenzy")
font=pygame.font.Font("Resources/Cactee-Regular.ttf",30)

#colors
white = (255, 255, 255)
red=(255,0,0)
green = (0, 200, 0)
blue = (0, 0, 128)
black = (0,0,0)
grey=(100,100,100)

#Functions
def screen_text(text,color,x,y):
    textscreen= font.render(text,True,color)
    mainwindow.blit(textscreen,(x,y))
def plotsnake(snake,snkbody):
    for x,y in snkbody:
        mainwindow.blit(snake,(x,y))

clock=pygame.time.Clock()

def welcome():
    welcome_screen=pygame.image.load("Resources/welcome.jpg")
    running=True
    while running:
        mainwindow.blit(welcome_screen,(0,0))
        for event in pygame.event.get():
            if event.type== QUIT:
                running=False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    gameloopmap1()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_2:
                    gameloopmap2()
        screen_text(("Press ESC TO return to this menu."),white,20,550)

        pygame.display.update()


def gameloopmap1():

        #Game Items
    with open("Resources/hiscore.txt","r")as f:
        hiscore=f.read()
    snake=pygame.image.load("Resources/block.jpg")
    food=pygame.image.load("Resources/apple.jpg")
    background=pygame.image.load("Resources/background.jpg")
    outro=pygame.image.load("Resources/outro.jpg")

    #Game Settings
    food_x=random.randint(50,s_width-50)
    food_y=random.randint(50,s_height-50)
    food_sens=30
    snake_x=random.randint(100,s_width/2)
    snake_y=random.randint(100,s_width/2)
    fps=60
    score=0
    speed_snake=6
    velocity_x=0
    velocity_y=0
    snkbody=[]
    snklength=5


    #GameLoop

    running=True
    game_over=False

    #KeyMapping
    Lkey=False
    Rkey=False
    Ukey=False
    Dkey=False


    while running:
        if game_over:
            with open("Resources/hiscore.txt", "w") as f:
               f.write(str(hiscore))
            mainwindow.blit(outro,(0,0))
            screen_text((f"Score : {score}" ),black,385,400)



            for event in pygame.event.get():
                if event.type== QUIT:
                    running=False
                if event.type == pygame.KEYDOWN:
                   if event.key == pygame.K_RETURN:
                       gameloopmap1()
        else:
            for event in pygame.event.get():
                if event.type== QUIT:
                    running=False
                if event.type == KEYDOWN:
                    if event.key==K_UP and Dkey==False:
                        Ukey=True
                        Dkey=False
                        Lkey=False
                        Rkey=False
                        velocity_x=0
                        velocity_y=-speed_snake
                    if event.key==K_DOWN and Ukey==False:
                        Ukey=False
                        Dkey=True
                        Lkey=False
                        Rkey=False
                        velocity_x=0
                        velocity_y=speed_snake
                    if event.key==K_RIGHT and Lkey==False:
                        Ukey=False
                        Dkey=False
                        Lkey=False
                        Rkey=True
                        velocity_x=speed_snake
                        velocity_y=0

                    if event.key==K_LEFT and Rkey==False:
                        Ukey=False
                        Dkey=False
                        Lkey=True
                        Rkey=False
                        velocity_x=-speed_snake
                        velocity_y=0
                    if event.key == K_ESCAPE:
                        welcome()



            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y
            if abs(snake_x-food_x)<food_sens and abs(snake_y-food_y)<food_sens:
                score+=1

                food_y=random.randint(20,s_height-20)
                food_x=random.randint(20,s_width-20)
                snklength+=5
            if score>int(hiscore):
                hiscore=score


            if snake_y>s_height:
                snake_y=0
            if snake_y<-20:
                snake_y=s_height
            if snake_x>s_width:
                snake_x=0
            if snake_x<-20:
                snake_x=s_width


            mainwindow.blit(background,(0,0))
            plotsnake(snake,snkbody)
            mainwindow.blit(food,(food_x,food_y))
            screen_text((f"Score : {score}   Hi Score : {hiscore}" ),red,620,5)

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snkbody.append(head)
            if len(snkbody)>snklength:
                del snkbody[0]

            if head in snkbody[:-5]:
                game_over=True




        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    quit()
def gameloopmap2():

        #Game Items
    with open("Resources/hiscore2.txt","r")as f:
        hiscore=f.read()
    snake=pygame.image.load("Resources/block.jpg")
    food=pygame.image.load("Resources/apple.jpg")
    background=pygame.image.load("Resources/background2.jpg")
    outro=pygame.image.load("Resources/outro.jpg")
    spikes=pygame.image.load("Resources/spikes.png")


    #Game Settings
    food_x=random.randrange(100,800)
    food_y=random.randrange(100,600)
    food_sens=30
    snake_x=random.randint(100,s_width/2)
    snake_y=random.randint(100,s_width/2)
    fps=60
    score=0
    speed_snake=5
    velocity_x=0
    velocity_y=0
    snkbody=[]
    snklength=5


    #GameLoop

    running=True
    game_over=False

    #KeyMapping
    Lkey=False
    Rkey=False
    Ukey=False
    Dkey=False


    while running:
        if game_over:
            with open("Resources/hiscore2.txt", "w") as f:
               f.write(str(hiscore))
            mainwindow.blit(outro,(0,0))
            screen_text((f"Score : {score}" ),black,385,400)



            for event in pygame.event.get():
                if event.type== QUIT:
                    running=False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                       gameloopmap2()
                    if event.key == K_ESCAPE:
                        welcome()
        else:
            for event in pygame.event.get():
                if event.type== QUIT:
                    running=False
                if event.type == KEYDOWN:
                    if event.key==K_UP and Dkey==False:
                        Ukey=True
                        Dkey=False
                        Lkey=False
                        Rkey=False
                        velocity_x=0
                        velocity_y=-speed_snake
                    if event.key==K_DOWN and Ukey==False:
                        Ukey=False
                        Dkey=True
                        Lkey=False
                        Rkey=False
                        velocity_x=0
                        velocity_y=speed_snake
                    if event.key==K_RIGHT and Lkey==False:
                        Ukey=False
                        Dkey=False
                        Lkey=False
                        Rkey=True
                        velocity_x=speed_snake
                        velocity_y=0

                    if event.key==K_LEFT and Rkey==False:
                        Ukey=False
                        Dkey=False
                        Lkey=True
                        Rkey=False
                        velocity_x=-speed_snake
                        velocity_y=0
                    if event.key == K_ESCAPE:

                        welcome()



            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y
            if abs(snake_x-food_x)<food_sens and abs(snake_y-food_y)<food_sens:
                score+=1

                food_y=random.randint(50,550)
                food_x=random.randint(50,850)
                snklength+=4
            if score>int(hiscore):
                hiscore=score

            mainwindow.blit(background,(0,0))
            mainwindow.blit(spikes,(-5,-5))

            plotsnake(snake,snkbody)
            mainwindow.blit(food,(food_x,food_y))
            screen_text((f"Score : {score}   Hi Score : {hiscore}" ),white,620,20)

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snkbody.append(head)
            if len(snkbody)>snklength:
                del snkbody[0]

            if head in snkbody[:-5]:
                game_over=True
            if snake_x<15 or (snake_x>s_width-40) or snake_y<15 or snake_y>(s_height-40):
                game_over=True





        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    quit()
welcome()
