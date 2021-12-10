import pygame
import math

from constans import GRAVITAION, JUMP_SPEED, KICK_CONSTANT, SIZE_BLOCK, TIME_STOP, SPEED_Player, DELITA, SPEED_Zombie


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
    def __init__(self, x, y, images, screen):
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.size = SIZE_BLOCK
        self.real_size = 45
        self.an = 0
        self.image_idx = 0
        self.current_frame = 0
        self.animation_frames = 10  # Количество кадров между сменой анимации
        self.images = images
        # реальный размер, меньше 37 пикселей не надо жеательно больше 40
        self.otn = self.real_size / self.size
        self.screen = screen
        self.state = 'STAYING'  # can be STAYING/R_RUNNING/L_RUNNING/JUMPING/...

    def update_frame_dependent(self):
        self.current_frame += 1
        if self.current_frame >= self.animation_frames:
            self.current_frame = 0
            if self.state == 'R_RUNNING':
                self.image_idx = self.image_idx % 2 + 1  # 1 <-> 2
            elif self.state == 'L_RUNNING':
                self.image_idx = (self.image_idx + 1) % 2 + 4  # 4 <-> 5
            else:
                self.image_idx = 0

    def input(self, event):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.vx = SPEED_Player
            self.state = 'R_RUNNING'
        elif keys[pygame.K_a]:
            self.vx = -SPEED_Player
            self.state = 'L_RUNNING'
        else:
            self.vx = 0
            self.state = 'STAYING'
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
                self.an = math.atan2(((event.pos[1] - y0)/self.size-(self.y + self.otn)), ((
                    event.pos[0] - x0) / self.size - (self.x + self.otn / 2)))
            else:
                self.an = 0

    def draw(self):
        if self.images is None:
            pygame.draw.rect(self.screen, (225, 0, 0), (self.x * self.size,
                             self.y * self.size, self.real_size, self.real_size * 2))
            pygame.draw.line(self.screen, (0, 225, 0), (self.x * self.size, (self.y + 1) * self.size), (math.cos(
                self.an) * 200 + self.x * self.size, (self.y + 1) * self.size + math.sin(self.an) * 200), 2)
        else:
            rect = self.images[self.image_idx].get_rect()
            rect.topleft = self.x * self.size, self.y * self.size
            self.screen.blit(self.images[self.image_idx], rect)

class Zombie(Main_person):
    def __init__(self, x, y, screen, image=None):
        super().__init__(x, y, image, screen)
        self.time_tick = 0
        self.sign = 1

    def input(self, main_hero):
        if self.x - main_hero.x > 0:
            self.sign = -1
        elif self.x - main_hero.x < 0:
            self.sign = 1
        else:
            self.sign = 0
        if self.vx == 0:
            self.time_tick += 1
        if self.time_tick == TIME_STOP:
            if self.vy ==0:self.vy = -JUMP_SPEED
            self.time_tick = 0
        self.vx = self.sign * SPEED_Zombie
        self.vy += GRAVITAION

    def draw(self):
        pygame.draw.rect(self.screen, (0, 255, 0), (self.x * self.size,
                         self.y * self.size, self.real_size, self.real_size * 2))
    def kick(self, main_hero):
        if math.sqrt((main_hero.x - self.x) ** 2 + (main_hero.y - self.y) ** 2) <= 1:
            main_hero.vx += self.sign * KICK_CONSTANT
