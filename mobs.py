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
        self.real_size = 45
        self.an = 0
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
    def broke(self, event, x0, y0):
        if event.type == pygame.MOUSEMOTION:
            if event:
                self.an = math.atan2(((event.pos[1] - y0)/self.size-(self.y + self.otn)), ((event.pos[0] - x0) / self.size - (self.x + self.otn / 2)))
            else:
                self.an = 0
    def draw(self):
        pygame.draw.rect(self.screen, (225, 0, 0), (self.x * self.size, self.y * self.size, self.real_size, self.real_size * 2))
        pygame.draw.line(self.screen, (0, 225, 0), ((self.x + self.otn / 2) * self.size, (self.y + self.otn) * self.size), (math.cos(self.an) * 200 + (self.x + self.otn / 2) * self.size, (self.y + self.otn) * self.size + math.sin(self.an) * 200 ), 2)
class Zombie(Main_person):
    def move():
        pass
