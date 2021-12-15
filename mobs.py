import pygame
import math
from constans import GRAVITAION, JUMP_SPEED, KICK_CONSTANT_X, KICK_CONSTANT_Y, SIZE_BLOCK, TIME_KICK, TIME_STOP, SPEED_Player, DELITA, SPEED_Zombie
from not_constant import types_block


def point_collision_x(x, y, vx, massive_map):
    """
    The function checks the collision of a point with coordinates (x + vx, y) with map blocks.
    Returns the possibility of movement along the x-axis.
    """
    considered_block = types_block.get(massive_map[int(y // 1)][int((x + vx) // 1)], 0)
    if not considered_block.permeability:
        move_x = False
    else:
        move_x = True
    return move_x


def point_collision_y(x, y, vy, massive_map):
    """
    The function checks the collision of a point with coordinates (x, y + vy) with map blocks
    Returns the possibility of movement along the y-axis.
    """
    considered_block = types_block.get(massive_map[int((y + vy) // 1)][int(x // 1)], 0)
    if not considered_block.permeability:
        move_y = False
    else:
        move_y = True
    return move_y


class Person:
    """
    Person
    This class is responsible for all the actions of the main character.
    """

    def __init__(self, x, y, images, screen):
        self.destroy = True
        self.x_dot = None
        self.y_dot = None
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.size = SIZE_BLOCK
        self.real_size = 45
        self.an = 0
        self.image_idx = 0
        self.current_frame = 0
        self.animation_frames = 10  # Number of frames between animation changes
        self.images = images
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

    def input(self):
        """Sets the speed by pressing the movement buttons on the keyboard and by gravity."""
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

    def control_collision(self, massive_map):
        """
        Checks collisions with blocks at specified speeds, determines the possibility of movement in these directions.
        Makes sure that when shifting, none of the selected points of the person does not end up in an invalid block.
        """
        for i in self.x + DELITA, self.x + 1 * self.otn - DELITA:
            for j in self.y + DELITA, self.y + 1 * self.otn, self.y + 2 * self.otn - DELITA:
                if not (point_collision_x(i, j, self.vx, massive_map)):
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
                if not (point_collision_y(i, j, self.vy, massive_map)):
                    if self.vy < 0:
                        self.y = round(self.y)
                        self.vy = 0.002
                    else:
                        self.y = round(self.y) + 2 * (1 - self.otn)
                        self.vy = 0
                    break

    def control_collision_of_putting(self, massive_map):
        """Makes sure that the person does not end up in the block that he wants to put."""
        self.put = True
        for i in self.x + DELITA, self.x + 1 * self.otn - DELITA:
            for j in self.y + DELITA, self.y + 1 * self.otn, self.y + 2 * self.otn - DELITA:
                if not (point_collision_x(i, j, 0, massive_map)):
                    self.put = False
                    break
                else:
                    self.put = True
        if self.put:
            for i in self.x + DELITA, self.x + 1 * self.otn - DELITA:
                for j in self.y + DELITA, self.y + 1 * self.otn, self.y + 2 * self.otn - DELITA:
                    if not (point_collision_y(i, j, 0, massive_map)):
                        self.put = False
                        break
                    else:
                        self.put = True

    def move(self):
        """Moves a person."""
        self.x += self.vx
        self.y += self.vy

    def angle(self, event, x0, y0):
        """
        Counts the angle between the center of the person and the mouse cursor.
        It is necessary for setting and removing the block in the right place.
        """
        if event.type == pygame.MOUSEMOTION:
            if event:
                self.an = math.atan2(((event.pos[1] - y0) / self.size - (self.y + self.otn)),
                                     ((event.pos[0] - x0) / self.size - (self.x + self.otn / 2)))
            else:
                self.an = 0

    def broke(self, massive_map, inventory):
        """
        Breaks blocks at a certain distance when the left mouse button is pressed for a certain time
        (closest in the direction of the cursor).
        """
        self.mouse_pressed = pygame.mouse.get_pressed()
        if self.mouse_pressed[0]:
            time_to_die = pygame.time.get_ticks()
            for i in range(30):
                self.x_dot = self.x + self.otn / 2 + math.cos(self.an) * i / 10
                self.y_dot = self.y + self.otn + math.sin(self.an) * i / 10
                if massive_map[int(self.y_dot)][int(self.x_dot)] != 0:
                    self.destroy = True
                    break
                else:
                    self.destroy = False
            if self.destroy:
                breakable_block = types_block.get(massive_map[int(self.y_dot)][int(self.x_dot)], 0)
                seconds = breakable_block.durability
                if time_to_die - self.start_time >= seconds * 10 ** 3 / 10:
                    inventory.add_or_delete_block(massive_map[int(self.y_dot)][int(self.x_dot)], 1)
                    massive_map[int(self.y_dot)][int(self.x_dot)] = 0
                    self.start_time = pygame.time.get_ticks()

    def build(self, block_in_hands, massive_map, inventory):
        """Puts the block in the hand in the place indicated by the mouse cursor."""
        if block_in_hands != 0:
            for i in range(30):
                self.x_dot = self.x + self.otn / 2 + math.cos(self.an) * i / 10
                self.y_dot = self.y + self.otn + math.sin(self.an) * i / 10
                if massive_map[int(self.y_dot)][int(self.x_dot)] != 0:
                    man_rect = pygame.Rect(
                        (self.x * 10 ** 5, self.y * 10 ** 5, self.otn * 10 ** 5, 2 * self.otn * 10 ** 5))
                    block_rect = pygame.Rect((int(self.x + self.otn / 2 + math.cos(self.an) * (i - 1) / 10) * 10 ** 5,
                                              int(self.y + self.otn + math.sin(self.an) * (i - 1) / 10) * 10 ** 5,
                                              10 ** 5, 10 ** 5))
                    if not man_rect.colliderect(block_rect):
                        block_in_hands = inventory.add_or_delete_block(block_in_hands, -1)
                        massive_map[int(self.y + self.otn + math.sin(self.an) * (i - 1) / 10)][
                            int(self.x + self.otn / 2 + math.cos(self.an) * (i - 1) / 10)] = block_in_hands
                    break
        return block_in_hands

    def breath(self):
        pass

    def hit(self, event, massive_mobs):
        """A hit on a zombie, determined by clicking the left mouse button."""
        if event.button == 1:
            for zombie in massive_mobs[::-1]:
                if (zombie.x - self.x) ** 2 + (zombie.y - self.y) ** 2 <= 3:
                    zombie.life -= 1
                    if zombie.life == 0:
                        massive_mobs.remove(zombie)
                    break

    def draw(self):
        """Draws the main character."""
        rect = self.images[self.image_idx].get_rect()
        rect.topleft = self.x * self.size, self.y * self.size
        self.screen.blit(self.images[self.image_idx], rect)


class Zombie(Person):
    """
    Zombie
    The zombie mob is fully described in this class.
    """

    def __init__(self, x, y, images, screen):
        super().__init__(x, y, images, screen)
        self.vx = 0
        self.vy = 0
        self.time_tick = 0
        self.sign = 1
        self.image_idx = 6
        self.current_frame = 0
        self.animation_frames = 10  # Number of frames between animation changes
        self.images = images
        self.life = 5
        self.time = 0
        self.can_kick = True

    def input_zombie(self, main_hero):
        """This function sets the speed of the mob depending on the position of the person."""
        if self.x - main_hero.x > 0:
            self.sign = -1
        elif self.x - main_hero.x < 0:
            self.sign = 1
        else:
            self.sign = 0
        if self.vx == 0:
            self.time_tick += 1
        if self.time_tick == TIME_STOP:
            if self.vy == 0: self.vy = -JUMP_SPEED
            self.time_tick = 0
        self.vx = self.sign * SPEED_Zombie
        self.vy += GRAVITAION

    def update_frame_dependent(self):
        self.current_frame += 1
        if self.current_frame >= self.animation_frames:
            self.current_frame = 0
            if self.sign == 1:
                self.image_idx = (self.image_idx + 1) % 2 + 6  # 6 <-> 7
            elif self.sign == -1:
                self.image_idx = (self.image_idx + 1) % 2 + 8  # 8 <-> 9
            else:
                self.image_idx = 6

    def draw(self):
        """Draws the zombie."""
        rect = self.images[self.image_idx].get_rect()
        rect.topleft = self.x * self.size, self.y * self.size
        self.screen.blit(self.images[self.image_idx], rect)

    def kick(self, main_hero):
        """The function describes a zombie hitting a person."""
        if self.can_kick and (math.sqrt((main_hero.x - self.x) ** 2 + (main_hero.y - self.y) ** 2) <= 1):
            main_hero.breath()
            main_hero.vx += self.sign * KICK_CONSTANT_X
            main_hero.vy -= KICK_CONSTANT_Y
            self.time = 0
            self.can_kick = False
        elif not self.can_kick:
            self.time += 1
            if self.time == TIME_KICK:
                self.can_kick = True
