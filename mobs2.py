import pygame
import math
class main_person:
    def __init__(self, x, y, screen):
        self.x = x
        self.y = y
        self.x_otn = int(self.x // 1)
        self.y_otn = int(self.y // 1)
        self.flagx = False
        self.flagy = False
        self.move_x_forward = True
        self.move_y_forward= True
        self.move_x_bacward= True
        self.move_y_bacward= True
        self.vx = 0
        self.vy = 0
        self.size = 48
        self.screen = screen
    def input(self, event):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.vx = 0.1
        elif keys[pygame.K_a]:
            self.vx = -0.1
        else:
            self.vx = 0
        if keys[pygame.K_w]:
            self.vy = 0.2
    def control_collision(self, massive_slov, types_block):
        if self.x == self.x_otn:
            self.flagx = True
        else:
            self.flagx = False
        if self.y == self.y_otn:
            self.flagy = True
        else:
            self.flagy = False
        block_lefttop = types_block.get(massive_slov[self.x_otn][self.y_otn], 0)
        block_leftmiddle = types_block.get(massive_slov[self.x_otn][self.y_otn + 1], 0)
        block_leftbottom = types_block.get(massive_slov[self.x_otn][self.y_otn + 2], 0)
        block_righttop = types_block.get(massive_slov[self.x_otn + 1][self.y_otn], 0)
        block_rightmiddle = types_block.get(massive_slov[self.x_otn][self.y_otn + 1], 0)
        block_rightbottom = types_block.get(massive_slov[self.x_otn][self.y_otn + 2], 0)
        if self.flagx and self.flagy:
            
    def move(self):
        pass
    def draw(self):
        pygame.draw.rect(self.screen, (225, 0, 0), (self.x * self.size, self.y * self.size, self.size, self.size * 2))
