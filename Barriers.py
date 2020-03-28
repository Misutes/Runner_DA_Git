import pygame


class Barriers():

    def __init__(self, barriers_x, barriers_y, barriers_width, barriers_height, barriers_speed):
        self.barriers_x = barriers_x
        self.barriers_y = barriers_y
        self.barriers_width = barriers_width
        self.barriers_height = barriers_height
        self.barriers_speed = barriers_speed

    def move(self, surface, window_width):
        if self.barriers_x >= -self.barriers_width:
            pygame.draw.rect(surface, (0, 0, 0),
                             (self.barriers_x, self.barriers_y, self.barriers_width, self.barriers_height))
            self.barriers_x -= self.barriers_speed
        else:
            self.barriers_x = window_width


cactus = Barriers(600, 422, 30, 60, 4)


