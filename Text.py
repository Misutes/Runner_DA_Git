import pygame


# Создаем функцию вывода текста
def print_text(surface, message, x, y, font_color, font_type, font_size):
    font = pygame.font.SysFont(font_type, font_size)
    text = font.render(message, True, font_color)
    surface.blit(text, (x, y))

# Постоянные для меню паузы
pause = 'Pleas, press Enter to continue'
x = 200
y = 200
font_color = (0, 0, 0)
font_type = 'Arial'
font_size = 30