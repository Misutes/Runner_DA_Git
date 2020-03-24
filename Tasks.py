import random
import Character
import Enemy


# Определение попадания в цель
def quest(x1, x2, y1, y2):
    if abs(x1 - x2) <= 76 and abs(y1 - y2) <= 101:
        return 1


# Счетчик очков
count = 0


def counter(x, y):
    global count
    if quest(Character.x_p, Enemy.x_t, Character.y_p, Enemy.y_t):
        count += 1
        Character.x_p = random.uniform(0, x - Character.player_width)
        Character.y_p = random.uniform(0, y - Character.player_height)



