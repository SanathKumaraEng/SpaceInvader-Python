import pygame
import random
import math

# initialize pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# backgroung
background = pygame.image.load('bg.jpg')

# title and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)

# player
playerImg = pygame.image.load('spaceship-1.png')
playerX = 370
platerY = 500
playerX_change = 0
playerY_change = 0

# enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0, 600))
    enemyY.append(random.randint(0, 50))
    enemyX_change.append(4)
    enemyY_change.append(40)


# bullet
# ready - you can see the bullet on the screen
# fire - bullet is currently moving
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 4
bullet_status = "ready"

score = 0


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def fire_bullet(x, y):
    global bullet_status
    bullet_status = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX-bulletX, 2) + math.pow(enemyY-bulletY, 2))
    if distance < 27:
        return True
    else:
        return False


# game loop
running = True
while running:
    # background color
    screen.fill((0,0,0,))

    # background image
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("left arrow is pressed")
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                print("right arrow is pressed")
                playerX_change = 5
            if event.key == pygame.K_SPACE:
                if bullet_status == "ready":
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
                    print("bullet fired")
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                print("keystroke has been released")
                playerX_change = 0

    # checking for boundaries of spaceship
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    if playerX >= 736:
        playerX = 736

    # enemy movement
    for i in range(num_of_enemies):
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 4
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -4
            enemyY[i] += enemyY_change[i]

        # collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bulletY = 480
            bullet_status = "ready"
            score += 1
            print(score)
            enemyX[i] = random.randint(0, 800)
            enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyY[i], i)

    # bullet movement
    if bulletY <= 0:
        bulletY = 480
        bullet_status = "ready"
    elif bullet_status == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change


    player(playerX, platerY)
    pygame.display.update()
