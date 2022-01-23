import pygame   # модули которые пригодятся
import time
import random
#разрешение экрана
w = 800
h = 500

display = pygame.display.set_mode((w,h))
pygame.display.set_caption('chrome://dino')
# игровые обьекты
dino = pygame.image.load('dino.png')
road = pygame.image.load('road.png')
anim = pygame.image.load('anim1.png')
anim2 = pygame.image.load('anim2.png')
dead = pygame.image.load("smert'.png")
# скорость движения кактусов
speed = 1

hi = 60
rx = 0

y = 420

# гравитация
def graviti():
    global y
    if y < 420:
        y += 2
        if y >= 420:
            y = 420



cx = 800

jump = False

pygame.display.update()

start = True
while start:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                    if y < 419:
                        jump = False
                    else:
                        jump = True
    
    cx -= speed
    # прыжок
    if jump == True:
        y -= 150
        display.fill((240,240,240))
        display.blit(dino,(20,y))
        display.blit(cactus,(cx, 420))
        display.blit(road,(rx, 450))
        jump = False
    #основная логика
    if cx <= 0:
        cx = random.randint(800, 1090)
        speed += 0.2
        hi += 10
    if cx >= 20 and y == 420 and cx <= 40: # столкновение с кактусами
        display.fill((240,240,240))
        display.blit(dead,(20,y))
        display.blit(cactus,(cx, 420))
        display.blit(road,(rx, 450))
        pygame.display.update()
        time.sleep(3)
        exit()
    rx -= speed
    if rx <= -400:
        rx = 0
    graviti()
    #отрисовка обьектов
    display.fill((240,240,240))
    display.blit(anim,(20,y))
    display.blit(cactus,(cx, 420))
    display.blit(road,(rx, 450))

    pygame.display.update()
    display.fill((240,240,240))

    display.fill((240,240,240))
    display.blit(anim2,(20, y))

    display.blit(road,(rx, 450))
    display.blit(cactus,(cx, 420))
    pygame.display.update()

    pygame.time.delay(5)
 
