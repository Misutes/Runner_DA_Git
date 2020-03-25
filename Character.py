import pygame


class Jump_sepcifications():

    def __init__(self, jumpcount, barriers):
        self.jumpcount = jumpcount
        self.barriers = barriers


# Создаем игрока
player_width = 76
player_height = 101
player = pygame.Surface((player_width, player_height))

# Загружаем картинки
img_p_r = [pygame.image.load('Picture/1r.png'), pygame.image.load('Picture/2r.png'),
           pygame.image.load('Picture/3r.png'),
           pygame.image.load('Picture/4r.png'), pygame.image.load('Picture/5r.png'),
           pygame.image.load('Picture/6r.png'),
           pygame.image.load('Picture/7r.png')]
img_p_l = [pygame.image.load('Picture/1l.png'), pygame.image.load('Picture/2l.png'),
           pygame.image.load('Picture/3l.png'),
           pygame.image.load('Picture/4l.png'), pygame.image.load('Picture/5l.png'),
           pygame.image.load('Picture/6l.png'),
           pygame.image.load('Picture/7l.png')]
# Удалаем фон
player.set_colorkey((0, 0, 0))

# Задаем стартовые ко-ты игрока
x_p = 0
y_p = 382 # 382 and 87


# Рисуем анимацию бега
AnimationCounterPlayer = 0


def drawing(x):
    global AnimationCounterPlayer
    player.blit(x[AnimationCounterPlayer], (0, 0))
    AnimationCounterPlayer += 1
    if AnimationCounterPlayer >= 7:
        AnimationCounterPlayer = 0


# Прыжок по кнопке Space
isJump = False

def jump():
    global y_p, isJump, Jump
    if Jump.jumpcount > Jump.barriers:
        y_p -= Jump.jumpcount
        Jump.jumpcount -= 1
    else:
        isJump = False