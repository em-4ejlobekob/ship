import pygame
import time
from Ship import Ship

pygame.init()

BattleShip = pygame.display.set_mode((1600, 800))  # name of the window
pygame.display.set_caption("Battles")  # title of the window

x, y = 80, 66

width, height = 38, 38
speed = 38

isJump = False
jumpCount = 10

size = 4
shipz = [1, 2, 3, 4]
ships = []

walkRight = [pygame.image.load('Стоит.png')]
walkLeft = [pygame.image.load('Стоит.png')]
playerStand = [pygame.image.load('Стоит.png')]

bg = pygame.image.load('Russia.jpg')


def draw_window(aa):
    BattleShip.fill((0, 0, 0))
    BattleShip.blit(pygame.image.load('FILD.png'), (30, 30))
    BattleShip.blit(pygame.image.load('FILD.png'), (790, 30))
    for i in aa:
        i.draw()
    pygame.draw.rect(BattleShip, (64, 128, 255), (x, y, 36, 36), 4)  # рисует рамку
    pygame.display.update()  # обновляет дисплей


a = []
flag_ship = 0
flag_size = shipz[0]
counter = 0

sh_m = []

process = True
while process:
    pygame.time.delay(50)  # частота обновлений цикла

    for event in pygame.event.get():  # перебираем события
        if event.type == pygame.QUIT:
            process = False  # Если мы нажали на кнопочку закрыть, то мы выходим из приложения
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("Нажата кнопка: ", event.button)

    keys = pygame.key.get_pressed()  # список кнопок, которые сейчас нажимаются

    if keys[pygame.K_c]:
        flag_ship += 1
        print(flag_ship)
    if keys[pygame.K_SPACE] and flag_size:
        if flag_ship % 2 == 0:
            sh = Ship(size, 'H', x, y, 0)
            sh.project_name = BattleShip
        else:
            sh = Ship(size, 'V', x, y, 0)
            sh.project_name = BattleShip
        sh_m.append(sh)
        a.append(sh)
        flag_size -= 1
        if flag_size == 0 and counter < 3:
            size -= 1
            counter += 1
            flag_size = shipz[counter]

        time.sleep(0.1)
    if keys[pygame.K_r]:
        a.append(((x - 1, y - 1), -1, 0))
    if keys[pygame.K_LEFT] and x >= 60 + speed:
        x -= speed
    if keys[pygame.K_RIGHT] and x <= 460 - width - speed:
        x += speed
    if keys[pygame.K_UP] and y >= speed + 30:
        y -= speed
    if keys[pygame.K_DOWN] and y <= 446 - height - speed:
        y += speed

    draw_window(a)

pygame.quit()  # 100% закрытие программы
