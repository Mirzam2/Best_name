import pygame
import math
class main_person:
    def __init__(self, x, y, screen):
        self.x = x
        self.y = y
        self.x_otn = int(self.x // 1)
        self.y_otn = int(self.y // 1)
        self.vx = 0.1
        self.vy = 0.1
        self.size = 40
        self.screen = screen
    def move_y(self, event, massive_slov):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                self.y -= self.vy
    def move_x(self, event, massive_slov):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.x += self.vx
        elif keys[pygame.K_a]:
            self.x -= self.vx
    def draw(self):
        pygame.draw.rect(self.screen, (225, 0, 0), (self.x * self.size, self.y * self.size, self.size, self.size * 2))
