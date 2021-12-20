import pathlib

import pygame
from pygame import event, surface

import file
import Hume_screen
import inventoty
import map
import mobs
from constans import *
from not_constant import person_images


def music_event(keyboard_buttons: event):
    if keyboard_buttons[pygame.K_1]:
        pygame.mixer.music.pause()
    elif keyboard_buttons[pygame.K_2]:
        pygame.mixer.music.unpause()
        pygame.mixer.music.set_volume(0.5)


class Game:
    def __init__(self, main_screen: surface):
        """
        initializing the game
        main_screen - screen on which to draw an axial picture
        """
        self.main_screen = main_screen
        self.screen = pygame.Surface(
            (SIZE_MAP_X * SIZE_BLOCK, SIZE_MAP_Y * SIZE_BLOCK))  # surface which draw intermideate
        self.file_world = pathlib.Path(pathlib.Path.cwd(), "music.wav")
        pygame.display.set_icon(pygame.image.load(
            pathlib.Path(pathlib.Path.cwd(), "icon.jpg")))
        pygame.display.set_caption('Best_name')
        pygame.mixer.music.load(self.file_world)
        pygame.mixer.music.play(-1)
        self.file_world = Hume_screen.home_screen(self.main_screen)
        self.name_of_file_with_inventory = pathlib.Path(pathlib.Path.cwd(),
                                                        "saves_invent", "inventory" + self.file_world)
        self.file_inventory = open(self.name_of_file_with_inventory, 'r')
        self.inventory = inventoty.Inventory(self.file_inventory, main_screen)
        self.block_in_hands = 0
        self.list_words, self.map_types = file.load_map(self.file_world)
        self.main_hero, self.massive_mobs = file.load_units(
            self.screen, self.file_world)
        self.x_cam = -self.main_hero.x * \
            SIZE_BLOCK + main_screen.get_size()[0] / 2
        self.y_cam = -self.main_hero.y * \
            SIZE_BLOCK + main_screen.get_size()[1] / 2
        self.finished = False
        self.clock = pygame.time.Clock()
        self.time = 0
        self.x1, self.y1 = 1, 1
        self.diff_x, self.diff_y = 0, 0
        self.keys = list()
        pygame.display.update()

    def process(self):
        while not self.finished:
            self.time += 1
            self.main_screen.fill((0, 0, 0))
            self.veb_cam()
            for zombie in self.massive_mobs:
                zombie.strike = False
            if self.time % TIME_ZOMBIE_GENERATE == 0:
                self.x1, self.y1 = mobs.generate_mobs(self.list_words)
                self.massive_mobs.append(mobs.Zombie(
                    self.x1, self.y1, person_images, self.screen))
            self.event_handling()
            self.processes_units()
            if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                self.finished = True

            pygame.display.update()
            pygame.display.flip()
        file.save_map(self.list_words, self.file_world)
        file.save_units(self.massive_mobs, self.main_hero, self.file_world)
        self.inventory.save_inventory(self.name_of_file_with_inventory)
        result = Hume_screen.death_screen(self.main_screen, self.main_hero)
        if result == "exit":
            pygame.quit()
        elif result == "restart":
            self.finished = False

    def veb_cam(self):
        """
        A function calls a camera that draws a picture depending on the position of the player
        """
        # remote center by X
        self.diff_x = -self.main_hero.x * SIZE_BLOCK + \
            self.main_screen.get_size()[0] / 2 - self.x_cam
        # remote center by Y
        self.diff_y = -self.main_hero.y * SIZE_BLOCK + \
            self.main_screen.get_size()[1] / 2 - self.y_cam
        """Camera movement proper"""
        if self.diff_x >= MAX_DISTANT:
            self.x_cam += SPEED_CAM * self.diff_x / MAX_DISTANT
        if self.diff_x <= -MAX_DISTANT:
            self.x_cam += SPEED_CAM * self.diff_x / MAX_DISTANT
        if self.diff_y >= MAX_DISTANT:
            self.y_cam += SPEED_CAM * self.diff_y / MAX_DISTANT
        if self.diff_y <= -MAX_DISTANT:
            self.y_cam += SPEED_CAM * self.diff_y / MAX_DISTANT
        map.draw_map(self.list_words, self.screen)
        self.main_hero.draw()
        for mob in self.massive_mobs:
            mob.draw()
        self.main_screen.blit(self.screen, (self.x_cam, self.y_cam))

    def event_handling(self):
        """
        function handles events, clicks, mouse moves
        """
        for event in pygame.event.get():
            self.main_hero.angle(event, self.x_cam, self.y_cam)
            if event.type == pygame.QUIT:
                self.finished = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.main_hero.start_time = pygame.time.get_ticks()
                if event.button == 3:
                    self.main_hero.build(self.block_in_hands, self.list_words,
                                         self.inventory)
                self.main_hero.hit(event, self.massive_mobs)
            self.main_hero.angle(event, self.x_cam, self.y_cam)
        self.keys = pygame.key.get_pressed()
        music_event(self.keys)
        if self.keys[pygame.K_e]:
            self.block_in_hands = inventoty.inventory_screen(
                self.main_screen, self.inventory, self.block_in_hands)

    def processes_units(self):
        """
        Processing hero and mobs actions
        """
        self.main_hero.broke(self.list_words, self.inventory)
        self.main_hero.input()
        self.main_hero.update_frame_dependent()
        for zombie in self.massive_mobs:
            zombie.input_zombie(self.main_hero)
            zombie.update_frame_dependent()
            self.finished = zombie.kick(self.main_hero, self.finished)
            zombie.control_collision(self.list_words)
            zombie.move()
        self.main_hero.control_collision(self.list_words)
        self.main_hero.move()
