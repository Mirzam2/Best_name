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
        self.move_x = True
        self.move_y = True
        self.vx = 0
        self.vy = 0
        self.size = 48
        self.screen = screen
    def control_collision(self, massive_slov):
        if (self.x - self.x_otn) < 0.02:
            self.flagx = True
            self.x = float(self.x_otn)
        if (self.y - self.y_otn) < 0.02:
            self.flagy = True
            self.y = float(self.y_otn)
        self.move_x, self.move_y = False, False
        if not(self.flagx) and not(self.flagy):
            self.move_y = True
            self.move_x = True
        if self.flagx and not(self.flagy):
            self.move_y = True
            if massive_slov[self.x_otn + 1][self.y_otn] == 0 and massive_slov[self.x_otn + 1][self.y_otn + 1] == 0 and massive_slov[self.x_otn + 1][self.y_otn + 2] == 0:
                self.move_x = True
            else:
                self.move_x = False
        if not(self.flagx) and self.flagy:
            if massive_slov[self.x_otn][self.y_otn + 1] == 0 and massive_slov[self.x_otn + 2][self.y_otn + 2] == 0:
                self.move_y = True
            else:
                self.move_y = False
            self.move_x = True
        if self.flagx and self.flagy:
            if massive_slov[self.x_otn][self.y_otn + 2] == 0:
                self.move_y = True
            else:
                self.move_y = False
            if massive_slov[self.x_otn + 1][self.y_otn] == 0 and massive_slov[self.x_otn + 1][self.y_otn + 1] == 0:
                self.move_x = True
            else:
                self.move_x = False
        
    def move(self, event):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.vx = 0.03
        elif keys[pygame.K_a]:
            self.vx = -0.03
        else:
            self.vx = 0
        if keys[pygame.K_w]:
            self.vy = 0.2
        if self.move_x:
            self.x += self.vx
        if self.move_y:
            self.y -= self.vy
            self.vy -=  0.025
        elif self.vy == 0.2:
            self.y -= self.vy
            self.vy -= 0.025
        else:
            self.vy = 0
        self.x_otn = int(self.x // 1)
        self.y_otn = int(self.y // 1)
    def draw(self):
        pygame.draw.rect(self.screen, (225, 0, 0), (self.x * self.size, self.y * self.size, self.size, self.size * 2))
