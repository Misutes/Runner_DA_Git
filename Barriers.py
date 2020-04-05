import pygame
import random


class Barriers:

    def __init__(self, barriers_x, barriers_y, barriers_width, barriers_height):
        self.barriers_x = barriers_x
        self.barriers_y = barriers_y
        self.barriers_width = barriers_width
        self.barriers_height = barriers_height
        self.barriers_speed = random.randint(1, 3)

    def move(self, surface, window_width):
        if self.barriers_x >= -self.barriers_width:
            pygame.draw.rect(surface, (0, 0, 0),
                             (self.barriers_x, self.barriers_y, self.barriers_width, self.barriers_height))
            self.barriers_x -= self.barriers_speed
        else:
            self.barriers_x = window_width
            self.barriers_speed = random.randint(1, 3)


# Генерируем статичные переменные
window_widht = 800
bottom_line = 475
up_line = 183


# Генерируем массив препятствий на нижнем уровне
bottom_cactus_array = []
for counter in range(random.randint(1, 3)):
    width = random.randint(10, 30)
    height = random.randint(10, 28) * (-1)
    barriers = Barriers(window_widht + random.randint(0, 100), bottom_line, width, height)
    bottom_cactus_array.append(barriers)

# Генерируем массив препятствий на верхнем уровне
up_cactus_array = []
for counter in range(random.randint(2, 4)):
    width = random.randint(10, 30)
    height = random.randint(10, 28) * (-1)
    barriers = Barriers(window_widht + random.randint(0, 100), up_line, width, height)
    up_cactus_array.append(barriers)


# Рисуем массивы препятствий
def barriers(window, window_width):
    for element in bottom_cactus_array:
        element.move(window, window_width)
    for element in up_cactus_array:
        element.move(window, window_width)
