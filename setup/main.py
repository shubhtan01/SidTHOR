import pygame 
import random 
import math
from pygame import mixer


# Initialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800,600))

# background
background = pygame.image.load('background.jpg')
#Background sounds
# mixer.music.load('background.wav')
# mixer.music.play(-1)

# Title and Icon
pygame.display.set_caption("SidTHOR")
# icon = pygame.image.load('ufo1.png')
# pygame.display.set_icon(icon)


# Player 
playerImg = pygame.image.load('sidhant_cutie.png')
playerX = 370
playerY = 480
playerX_change = 0


# enemy
enemyImg = pygame.image.load('humanoid.png')
enemyX = random.randint(0,735)
enemyY = random.randint(50,150)
enemyX_change = 0.5
enemyY_change = 40



# creaitng more number of enemies
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('humanoid.png'))
    enemyX.append(random.randint(0,735))
    enemyY.append(random.randint(50,150))
    enemyX_change.append(0.3)
    enemyY_change.append(50)



# Bullet
# ready state means you cant see the bullet on sccreen and in fire state you can see the bullet
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 1
bullet_state = "ready"

# Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
textY = 10

# Game over text
over_font = pygame.font.Font('freesansbold.ttf', 64)

def show_score(x,y):
    score = font.render("Score :" + str(score_value), True, (255,255,255))
    screen.blit(score, (x,y))

def game_over_text(x,y):
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))

def player(x,y,i):
    screen.blit(playerImg, (x,y))

def enemy(x,y,i):
    screen.blit(enemyImg[i], (x,y))

def fire_bullet(x,y,i):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x+16, y+10))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX-bulletX,2)) + (math.pow(enemyY - bulletY,2)))
    if distance < 27: # we came on the value 27 by trial and error
        return True
    else:
        return False
    



# Game Loop
running = True
while running:
    # RGB - Red, Green, Blue
    screen.fill((0,0,0))

    # background image
    screen.blit(background,(0,0))

    for event in pygame.event.get() :
        if event.type == pygame.QUIT:
            running = False

        # if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    # bullet_Sound = mixer.Sound('laser.wav')
                    # bullet_Sound.play()

                    # get the current x coordinate of spaceship and stores it  
                    bulletX = playerX
                    fire_bullet(bulletX,bulletY,i)

    # Checking for boundaries of spaceship so it doesn't go out of bounds
    playerX += playerX_change      

    if playerX <=0:
        playerX = 0
    elif playerX >= 736 :
        playerX = 736 

    # Enemy movement
    for i in range(num_of_enemies):
        if enemyY[i] > 500:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text(250,200)
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 0.1
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -0.1
            enemyY[i] += enemyY_change[i] 

        # collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            # explosion_Sound = mixer.Sound('Moan_sound.wav')
            # explosion_Sound.play()
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            print(score_value)
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i],enemyY[i],i)
        

    # bullet movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state is "fire":
        fire_bullet(bulletX,bulletY,i)
        bulletY -= bulletY_change

    

    player(playerX,playerY, i)
    #enemy(enemyX,enemyY)
    show_score(textX, textY)
    pygame.display.update() 