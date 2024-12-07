import pygame

#ширина и высота игрового поля
W, H = 800, 600

#в играх в TITLE пишем название игры
TITLE = "Основа игры"

#время для clock
TICK = 60

#цвет фона
bg_color = (0,150,0)

#параметры игрока
player_color = (230,25,0) #цвет
player_size = 50 #размер

#положение по x и y
player_x, player_y = 375, 5

#скорость перемещения
player_speed = 5



pygame.init()
screen = pygame.display.set_mode((W,H))
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()
running = True


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False

    # нажатие на кнопки стрелки
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]: #стрелка влево
        player_x -= player_speed
    if keys[pygame.K_RIGHT]: #стрелка вправо
        player_x += player_speed

    if keys[pygame.K_UP]: #вверх
        player_y -= player_speed
    if keys[pygame.K_DOWN]: #вниз
        player_y += player_speed




    # прорисовка игрового поля и игрока
    screen.fill(bg_color)
    pygame.draw.rect(screen, player_color, (player_x, player_y, player_size, player_size))
    pygame.display.update()
    clock.tick(TICK)

pygame.quit()