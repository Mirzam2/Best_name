import pygame
import math
class Main_person:
    def __init__(self, x, y, screen):
        self.x = x
        self.y = y
        self.x_otn = int(self.x // 1)
        self.y_otn = int(self.y // 1)
        self.flagx = False
        self.flagy = False
        self.move_x = True
        self.move_y= True
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
        if keys[pygame.K_w]:
            self.vy = -0.2
        self.vy += 0.002
    def control_collision(self, massive_slov, types_block):
        self.x_otn_move = int((self.x + self.vx) // 1)
        self.x_otn = int(self.x // 1)
        self.y_otn_move = int((self.y + self.vy) // 1)
        self.y_otn = int(self.y // 1)
        self.move_x = True
        self.move_y= True
        for i in range(0, 3):
            for j in range(0,2):
                if massive_slov[self.x_otn_move + j][self.y_otn + i] != 0:
                    self.move_x = False
                    self.vx = 0
                    break
        for i in range(0, 3):
            for j in range(0,2):
                if massive_slov[self.x_otn + j][self.y_otn_move + i] != 0:
                    self.move_y = False
                    self.vy = 0
                    break
        
    def move(self):
        if self.move_x:
            self.x += self.vx
        if self.move_y:
            self.y += self.vy
    def draw(self):
        pygame.draw.rect(self.screen, (225, 0, 0), (self.x * self.size, self.y * self.size, self.size, self.size * 2))
