import pygame
import random
import math
 #intialize the pygame
pygame.init()

#create the screen 
screen=pygame.display.set_mode((800,600))

#background image
background=pygame.image.load('background.jpg')

#Title and icon
pygame.display.set_caption("Space Invadors")
icon=pygame.image.load('scare.png')
pygame.display.set_icon(icon)

#Player
playerimg=pygame.image.load('fighter-jet.png')
playerX=370
playerY=480
playerX_change=0

#Enemy
enemy=[]
enemyimg=[]
enemyX=[]
enemyY=[]
enemyX_change=[]
enemyY_change=[]
num_of_series=6
for i in range(num_of_series):
    enemyimg.append(pygame.image.load('brutus.png'))
    enemyX.append(random.randint(0,735))
    enemyY.append(random.randint(50,150))
    enemyX_change.append(0.3)
    enemyY_change.append(40)

#Bullets
#ready ---You can't the see the bullet in the screen
#fire --- the bullet is moving 

bulletimg=pygame.image.load('bullet.png')
bulletX=0
bulletY=480
bulletX_change=0
bulletY_change=10
bullet_state="ready"

#score 
score_value=0
font=pygame.font.Font('freesansbold.ttf',32)

textX=10
textY=10


def show_score(x,y):
    score=font.render("Score :"+str(score_value),True,(255,255,255))
    screen.blit(score,(x,y))
def player(x,y):
    screen.blit(playerimg,(x,y))

def enemy(x,y,i):
    screen.blit(enemyimg[i],(x,y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state="fire"
    screen.blit(bulletimg,(x+16,y+10))
def isCollision(bulletX,bulletY,enemyX,enemyY):
    distance=math.sqrt(math.pow(bulletX-enemyX,2)+math.pow(bulletY-enemyY,2))
    if distance<27:
        return True
    else:
        return False

#Game loop
running =True
while running:

# RGB red, Green Blue
    screen.fill((0,0,0))

#Background Image on the top of
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        
#if key stroke is pressed whether its right or left
        if event.type==pygame.KEYDOWN:
            print("A key stroke is pressed")
            if event.key==pygame.K_LEFT:
                playerX_change=-0.3
            if event.key==pygame.K_RIGHT:
                playerX_change=0.3
            if event.key==pygame.K_SPACE:
                bulletX=playerX
                fire_bullet(playerX,bulletY)
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                playerX_change=0

#checking the boundaries for the spaceship so it dose not go out of bound
    playerX+=playerX_change

#this condition is for boarder 

    if playerX <=0:
        playerX=0
    elif playerX >= 736:
        playerX= 736 

#enemy movement
    for i in range(num_of_series):
        enemyX[i]+=enemyX_change[i]

#this condition is for boarder 
        if enemyX[i] <=0:
            enemyX_change[i]=0.3
            enemyY[i]+=enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i]= -0.3 
            enemyY[i]+=enemyY_change[i]
            
    #collision code
        collision=isCollision(bulletX,bulletY,enemyX[i],enemyY[i])
        if collision:
            bulletY=480
            bullet_state="ready"
            score_value+=1
            enemyX[i]=random.randint(0,735)
            enemyY[i]=random.randint(50,150)
        enemy(enemyX[i],enemyY[i],i)  

    # bullet movement 
    if bulletY<=0:
        bulletY=480
        bullet_state="ready"
    if bullet_state is "fire":
        fire_bullet(playerX,bulletY)   
    bulletY-=bulletY_change
    player(playerX,playerY)
    show_score(textX,textY)
    enemy(enemyX[i],enemyY[i],i)

    pygame.display.update()