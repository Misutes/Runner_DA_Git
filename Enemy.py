import pygame
import math

# Создаем цель
target_width = 40
target_height = 40
target = pygame.Surface((target_width, target_height))

# Загружаем картинки
img_t_r = pygame.image.load('Picture/target_r.png')
img_t_l = pygame.image.load('Picture/target_l.png')
# Удалаем фон
target.set_colorkey((0, 0, 0))

# Стартовые ко-ты цели и переемнные
x_t = 0
y_t = 415
AnimationCounterTarget = 0
TargetSpeed = 1
JumpCountTarget = 0

# Движение цели
Right = True


def moving():
    global Right, AnimationCounterTarget, TargetSpeed, x_t
    if Right:
        x_t += TargetSpeed
        if int(x_t) >= 698:
            Right = False
            AnimationCounterTarget = 1
            TargetSpeed += 0.5
    else:
        x_t -= TargetSpeed
        if int(x_t) <= 0:
            Right = True
            AnimationCounterTarget = 0


# Прыжки цели
def targerjump():
    global JumpCountTarget, y_t
    JumpCountTarget -= 0.1
    y_t = 370 + 30 * math.cos(JumpCountTarget)
    if JumpCountTarget <= -6.3:
        JumpCountTarget = 0


# Анимация поворота
def rotation():
    if AnimationCounterTarget == 0:
        target.blit(img_t_r, (0, 0))
    else:
        target.blit(img_t_l, (0, 0))
