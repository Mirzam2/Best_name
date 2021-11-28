import pygame
import math
class main_person:
    def __init__(self, x, y, screen):
        self.x = x
        self.y = y
        self.x_otn = int(self.x // 1)
        self.y_otn = int(self.y // 1)
        if self.x == self.x_otn:
            self.flagx = True
        if self.y == self.y_otn:
            pass  
        self.vy = 0.1
        self.size = 40
        self.screen = screen             
    def move(self, event):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.vx = 0.1
        if keys[pygame.K_a]:
            self.vx = -0.1
        if not(keys[pygame.K_w]):
            self.vy = 0.1
    def control_collision(self, massive_slov):
        pass
        
    def draw(self):
        pygame.draw.rect(self.screen, (225, 0, 0), (self.x * self.size, self.y * self.size, self.size, self.size * 2))
