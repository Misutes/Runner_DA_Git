import pygame
import Text


# Создаем функцию паузы
def pause(surface, message, x, y, font_color, font_type, font_size):
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        Text.print_text(surface, message, x, y, font_color, font_type, font_size)
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RETURN]:
            paused = False

        pygame.display.update()


# Создаем функцию "Конца игры"
game_over_massage = "Game over"


def game_over(surface, message, x, y, font_color, font_type, font_size):
    game_over = True
    while game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        Text.print_text(surface, message, x, y, font_color, font_type, font_size)
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RETURN]:
            return True
        if keys[pygame.K_ESCAPE]:
            return False

        pygame.display.update()
