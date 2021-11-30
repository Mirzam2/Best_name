import pygame
import math
def point_collision_x(x, y, vx, massive_slov):
    if massive_slov[int(y // 1)][int((x + vx) // 1)] != 0:
        move_x = False
    else:
        move_x = True
    return move_x
def point_collision_y(x, y, vy, massive_slov):
    if massive_slov[int((y + vy) // 1)][int(x // 1)] != 0:
        move_y = False
    else:
        move_y = True
    return move_y
class Main_person:
    def __init__(self, x, y, screen):
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.size = 48
        self.screen = screen
    def input(self, event):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.vx = 0.05
        elif keys[pygame.K_a]:
            self.vx = -0.05
        else:
            self.vx = 0
        if keys[pygame.K_w] and self.vy == 0:
            self.vy = -0.1
        self.vy += 0.002
    def control_collision(self, massive_slov):
        for i in self.x + 10 ** (-10), self.x + 1 - 10 ** (-10):
            for j in self.y + 10 ** (-10), self.y + 1, self.y + 2 - 10 ** (-10):
                if not(point_collision_x(i, j, self.vx, massive_slov)):
                    self.vx = 0
                    self.x = round(self.x)
                    break
        for i in self.x + 10 ** (-10), self.x + 1 - 10 ** (-10):
            for j in self.y + 10 ** (-10), self.y + 1, self.y + 2 - 10 ** (-10):
                if not(point_collision_y(i, j, self.vy, massive_slov)):
                    self.vy = 0
                    self.y = round(self.y)
                    break
        
    def move(self):
        self.x += self.vx
        self.y += self.vy
    def draw(self):
        pygame.draw.rect(self.screen, (225, 0, 0), (self.x * 48, self.y * 48, self.size, self.size * 2))
