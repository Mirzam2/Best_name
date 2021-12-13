import pygame
import math
import time

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
        self.mouse_pressed = None
        self.start_time = 0
        self.life = 10
        self.put = True

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
                    self.put = False
                    break
                else:
                    self.put = True
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
    def control_collision_of_putting(self, massive_slov):
        for i in self.x + DELITA, self.x + 1 * self.otn - DELITA:
            for j in self.y + DELITA, self.y + 1 * self.otn, self.y + 2 * self.otn - DELITA:
                if not(point_collision_x(i, j, 0, massive_slov)):
                    self.put = False
                    break
                else:
                    self.put = True
        if self.put:
            for i in self.x + DELITA, self.x + 1 * self.otn - DELITA:
                for j in self.y + DELITA, self.y + 1 * self.otn, self.y + 2 * self.otn - DELITA:
                    if not(point_collision_y(i, j, 0, massive_slov)):
                        self.put = False
                        break
                    else:
                        self.put = True
    def move(self):
        self.x += self.vx
        self.y += self.vy

    def angle(self, event, x0, y0):
        if event.type == pygame.MOUSEMOTION:
            if event:
                self.an = math.atan2(((event.pos[1] - y0)/self.size-(self.y + self.otn)), ((
                    event.pos[0] - x0) / self.size - (self.x + self.otn / 2)))
            else:
                self.an = 0
    def broke(self, massive_slov, types_block):
        self.mouse_pressed = pygame.mouse.get_pressed()
        if self.mouse_pressed[0]:
            time_to_die = pygame.time.get_ticks()
            for i in range(30):
                self.x_dot = self.x + self.otn / 2 + math.cos(self.an) * i / 10
                self.y_dot = self.y + self.otn + math.sin(self.an) * i / 10
                if massive_slov[int(self.y_dot)][int(self.x_dot)] != 0:
                    self.destroy = True
                    break
                else:
                    self.destroy = False
            if self.destroy:
                breakable_block = types_block.get(massive_slov[int(self.y_dot)][int(self.x_dot)], 0)
                seconds = breakable_block.durability
                if time_to_die - self.start_time >= seconds * 10 ** 3 / 10:
                    massive_slov[int(self.y_dot)][int(self.x_dot)] = 0
                    time_to_die = pygame.time.get_ticks()
                    self.start_time = pygame.time.get_ticks()

    def build(self, massive_slov):
        for i in range(30):
            self.x_dot = self.x + self.otn / 2 + math.cos(self.an) * i / 10
            self.y_dot = self.y + self.otn + math.sin(self.an) * i / 10
            if massive_slov[int(self.y_dot)][int(self.x_dot)] != 0:
                massive_slov[int(self.y + self.otn + math.sin(self.an) * (i - 1) / 10)][int(self.x + self.otn / 2 + math.cos(self.an) * (i - 1) / 10)] = 1
                self.control_collision_of_putting(massive_slov)
                if not(self.put):
                    massive_slov[int(self.y + self.otn + math.sin(self.an) * (i - 1) / 10)][int(self.x + self.otn / 2 + math.cos(self.an) * (i - 1) / 10)] = 0
                break
    def breath(self):
        pass
    def draw(self):
        rect = self.images[self.image_idx].get_rect()
        rect.topleft = self.x * self.size, self.y * self.size
        self.screen.blit(self.images[self.image_idx], rect)

class Zombie(Main_person):
    def __init__(self, x, y, images, screen):
        super().__init__(x, y, images, screen)
        self.time_tick = 0
        self.sign = 1
        self.image_idx = 6
        self.current_frame = 0
        self.animation_frames = 10  # Количество кадров между сменой анимации
        self.images = images

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

    def update_frame_dependent(self):
        self.current_frame += 1
        if self.current_frame >= self.animation_frames:
            self.current_frame = 0
            if self.sign == 1:
                self.image_idx = (self.image_idx+1) % 2 + 6  # 6 <-> 7
            elif self.sign == -1:
                self.image_idx = (self.image_idx + 1) % 2 + 8  # 8 <-> 9
                print(self.image_idx)
            else:
                self.image_idx = 6

    def draw(self):
        rect = self.images[self.image_idx].get_rect()
        rect.topleft = self.x * self.size, self.y * self.size
        self.screen.blit(self.images[self.image_idx], rect)

    def kick(self, main_hero):
        if math.sqrt((main_hero.x - self.x) ** 2 + (main_hero.y - self.y) ** 2) <= 1:
            main_hero.breath()
            main_hero.vx += self.sign * KICK_CONSTANT
            print("Kick")