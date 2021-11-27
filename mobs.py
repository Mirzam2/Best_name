import pygame
import math
class main_person:
    def __init__(self, x, y, screen):
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.screen = screen
    def move_x(self, vx):
        self.vx = vx
        self.x += self.vx
    def move_y(self):
        pass
        self.vy += 10
        self.y -= self.vy
    def draw(self):
        pygame.draw.rect(self.screen, (225, 0, 0), (self.x, self.y, 40, 80))
