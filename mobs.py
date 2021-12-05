import pygame
import math

from constans import GRAVITAION, JUMP_SPEED, SIZE_BLOCK, SPEED_Player, DELITA
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
        self.size = SIZE_BLOCK
        self.real_size = 42 
        # реальный размер, меньше 37 пикселей не надо жеательно больше 40
        self.otn = self.real_size / self.size
        self.screen = screen
    def input(self, event):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.vx = SPEED_Player
        elif keys[pygame.K_a]:
            self.vx = -SPEED_Player
        else:
            self.vx = 0
        if keys[pygame.K_w] and self.vy == 0:
            self.vy = -JUMP_SPEED
        self.vy += GRAVITAION
    def control_collision(self, massive_slov):
        for i in self.x + DELITA, self.x + 1 * self.otn - DELITA:
            for j in self.y + DELITA, self.y + 1 * self.otn, self.y + 2 * self.otn - DELITA:
                if not(point_collision_x(i, j, self.vx, massive_slov)):
                    if self.vx > 0:
                        self.x = round(self.x) + 1 - self.otn
                    else:
                        self.x = round(self.x)
                    self.vx = 0
                    break
        for i in self.x + DELITA, self.x + 1 * self.otn - DELITA:
            for j in self.y + DELITA, self.y + 1 * self.otn, self.y + 2 * self.otn - DELITA:
                if not(point_collision_y(i, j, self.vy, massive_slov)):
                    if self.vy < 0:
                        self.y = round(self.y)
                        self.vy = 0.002
                    else:
                        self.y = round(self.y) + 2 * (1 - self.otn)
                        self.vy = 0
                    break
        
    def move(self):
        self.x += self.vx
        self.y += self.vy
    def draw(self):
        pygame.draw.rect(self.screen, (225, 0, 0), (self.x * self.size, self.y * self.size, self.real_size, self.real_size * 2))
