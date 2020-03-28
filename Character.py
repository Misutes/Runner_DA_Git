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

# Задаем стартовые переменные игрока
x_p = 0
y_p = 382
isJump = False
is_min_Jump = False
AnimationCounterPlayer = 0
Jump = Jump_sepcifications(25, -9)


def drawing(x):
    global AnimationCounterPlayer
    player.blit(x[AnimationCounterPlayer], (0, 0))
    AnimationCounterPlayer += 1
    if AnimationCounterPlayer >= 7:
        AnimationCounterPlayer = 0


# Прыжок по кнопке Space
def jump():
    global y_p, isJump, is_min_Jump, isJump
    if Jump.jumpcount > Jump.barriers:
        y_p -= Jump.jumpcount
        Jump.jumpcount -= 1
    else:
        isJump = False
        is_min_Jump = False


# Перемещение игрока
def character_move(keys, window_width):
    global x_p, y_p, isJump, is_min_Jump, Jump
    # Движение по горизонтали
    if keys[pygame.K_a] and x_p > 0:
        x_p -= 2
        drawing(img_p_l)
    elif keys[pygame.K_d] and x_p < (window_width - player_width):
        x_p += 2
        drawing(img_p_r)
    else:
        pass

    # Прыжок
    if y_p == 382:
        if keys[pygame.K_SPACE] and keys[pygame.K_w]:
            isJump = True
        if isJump:
            jump()
    else:
        if keys[pygame.K_SPACE] and keys[pygame.K_s]:
            isJump = True
        if isJump:
            jump()

    if not isJump and y_p == 93 and keys[pygame.K_s]:
        Jump = Jump_sepcifications(8, -26)
    if not isJump and y_p == 382 and keys[pygame.K_w]:
        Jump = Jump_sepcifications(25, -9)