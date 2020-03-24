import pygame


import Tasks
import Character
import Enemy


pygame.init()

# Создаем окно игры и заголовок
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
img_screen = pygame.image.load('Picture/Background.png')
pygame.display.set_caption('Simple Game')

# Частота кадров игры
clock = pygame.time.Clock()

# Создаем переменную выхода
Finish = False


# Основной цикл игры
while not Finish:
    # Выход по крестику
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Finish = True
    # Отображение статичного игрока
    Character.player.blit(Character.img_p_r[0], (0, 0))

    # Перемещение игрока
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and Character.x_p > 0:
        Character.x_p -= 2
        Character.drawing(Character.img_p_l)
    elif keys[pygame.K_d] and Character.x_p < (window_width - Character.player_width):
        Character.x_p += 2
        Character.drawing(Character.img_p_r)
    else:
        pass

    # Прыжок
    if Character.UpCounter != 1:
        if keys[pygame.K_SPACE] and keys[pygame.K_w]:
            Character.isJump = True
        if Character.isJump:
            Character.jump(20, -7.8, 0.3)
    else:
        Character.isJump = True
        if keys[pygame.K_SPACE] and keys[pygame.K_s]:
            Character.UpCounter = 0
            Character.jump()

    # Движение цели
    #Enemy.moving()
    # Прыжки цели
    #Enemy.targerjump()
    # Счетчик очков
    #Tasks.counter(window_width, window_height)
    # Создаем шрифт счетчика
    myf = pygame.font.SysFont("Arial", 35, italic=True)
    string = myf.render('Очков:' + str(Tasks.count), 0, (0, 165, 80))

    # Генерируем задний фон
    window.blit(img_screen, (0, 0))
    Enemy.rotation()
    # Генерируем элементы
    window.blit(string, (315, 0))
    window.blit(Character.player, (int(Character.x_p), int(Character.y_p)))
    #window.blit(Enemy.target, (int(Enemy.x_t), int(Enemy.y_t)))
    # Обновляем дисплей
    pygame.display.update()
    clock.tick(60)

pygame.quit()