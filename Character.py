import pygame


class Transfer_sepcifications():

    def __init__(self, count, barriers):
        self.count = count
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
x = 0
y = 382
isLevel = False
isJump = False
AnimationCounterPlayer = 0
Level = Transfer_sepcifications(25, -9)
Jump = Transfer_sepcifications(10, -9)
character_down_level = 382
character_up_level = 93


def drawing(x):
    global AnimationCounterPlayer
    player.blit(x[AnimationCounterPlayer], (0, 0))
    AnimationCounterPlayer += 1
    if AnimationCounterPlayer >= 7:
        AnimationCounterPlayer = 0


# Прыжок по кнопке Space
def jump(qualifier):
    global y, isLevel, isJump
    if qualifier.count > qualifier.barriers:
        y -= qualifier.count
        qualifier.count -= 1
    else:
        isLevel = False
        isJump = False


# Перемещение игрока
def character_move(keys, window_width):
    global x, y, isLevel, isJump, Level, Jump
    # Движение по горизонтали
    if keys[pygame.K_a] and x > 0:
        x -= 2
        drawing(img_p_l)
    elif keys[pygame.K_d] and x < (window_width - player_width):
        x += 2
        drawing(img_p_r)
    else:
        pass

    # Создаем переменные для прыжка
    if not isLevel and y == 93 and keys[pygame.K_s]:
        Level = Transfer_sepcifications(8, -26)
    if not isLevel and y == 382 and keys[pygame.K_w]:
        Level = Transfer_sepcifications(25, -9)
    if keys[pygame.K_SPACE] and (not isJump):
        Jump = Transfer_sepcifications(14, -15)

    # Прыжок
    if y == 382:
        if keys[pygame.K_w]:
            isLevel = True
        if isLevel:
            jump(Level)
    else:
        if keys[pygame.K_s]:
            isLevel = True
        if isLevel:
            jump(Level)

    if keys[pygame.K_SPACE]:
        isJump = True
    if not isLevel and isJump:
        jump(Jump)
