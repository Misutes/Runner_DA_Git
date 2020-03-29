import pygame
import Text


# Создаем функцию паузы
def pause(surface, message, x, y, font_color, font_type, font_size):
    paused = False
    while not paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        Text.print_text(surface, message, x, y, font_color, font_type, font_size)
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RETURN]:
            paused = True

        pygame.display.update()