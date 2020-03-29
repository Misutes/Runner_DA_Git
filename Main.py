import pygame

import Tasks
import Character
import Barriers
import Text
import Menu



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

    # Считываем клавиши
    keys = pygame.key.get_pressed()

    # Пауза
    if keys[pygame.K_ESCAPE]:
        Menu.pause(window, Text.pause, Text.x, Text.y, Text.font_color, Text.font_type, Text.font_size)

    # Генерируем задний фон
    window.blit(img_screen, (0, 0))

    # Отображение статичного игрока
    Character.player.blit(Character.img_p_r[0], (0, 0))

    # Перемещение игрока
    Character.character_move(keys, window_width)
    window.blit(Character.player, (int(Character.x), int(Character.y)))

    # Препятствия
    Barriers.barriers(window, window_width)

    """
  # Счетчик очков
  Tasks.counter(window_width, window_height)
  # Создаем шрифт счетчика
  myf = pygame.font.SysFont("Arial", 35, italic=True)
  string = myf.render('Очков:' + str(Tasks.count), 0, (0, 165, 80))
  # Генерируем элементы
  window.blit(string, (315, 0))
  """

    # Обновляем дисплей
    pygame.display.update()
    clock.tick(60)

pygame.quit()
