from pygame import surface
import pygame
from constans import SIZE_BLOCK
import map
import mobs
import pygame
import file
from constans import *
import Hume_screen
import pathlib
import inventoty
from not_constant import person_images


def veb_cam(blit_screen: surface, x: float, y: float, cam_screen: surface, hero: mobs.Person, mobs: list, list_map: list):
    """
    A function calls a camera that draws a picture depending on the position of the player
    main_screen - the main screen on which the picture should be
    x, y - the position of the camera in the predictive tick
    cam_screen - a picture of the overall drawing
    hero - character
    mobs - an array of mobs
    map - list of map
    """
    speed_cam = 1  # коэфициент пропорциональности скорости
    max_distant = 2 * SIZE_BLOCK  # максимальное удаление
    # отдаление от центра по X
    diff_x = -hero.x * SIZE_BLOCK + blit_screen.get_size()[0] / 2 - x
    # отдаление от центра по Y
    diff_y = -hero.y * SIZE_BLOCK + blit_screen.get_size()[1] / 2 - y
    "Собственно движение камеры"
    if diff_x >= max_distant:
        x += speed_cam * diff_x / max_distant
    if diff_x <= -max_distant:
        x += speed_cam * diff_x / max_distant
    if diff_y >= max_distant:
        y += speed_cam * diff_y / max_distant
    if diff_y <= -max_distant:
        y += speed_cam * diff_y / max_distant
    map.draw_map(list_map, cam_screen)
    hero.draw()
    for mob in mobs:
        mob.draw()
    blit_screen.blit(cam_screen, (x, y))
    return x, y


def music_event(klick):
    if klick[pygame.K_1]:
        pygame.mixer.music.pause()
        # pygame.mixer.music.stop()
    elif klick[pygame.K_2]:
        pygame.mixer.music.unpause()
        # pygame.mixer.music.play()
        pygame.mixer.music.set_volume(0.5)


class Game:
    def __init__(self, main_screen):
        self.main_screen = main_screen
        self.screen = pygame.Surface(
            (SIZE_MAP_X * SIZE_BLOCK, SIZE_MAP_Y * SIZE_BLOCK))
        self.file_world = pathlib.Path(pathlib.Path.cwd(), "music.wav")
        pygame.display.set_icon(pygame.image.load(
            pathlib.Path(pathlib.Path.cwd(), "icon.jpg")))
        pygame.display.set_caption('Best_name')
        pygame.mixer.music.load(self.file_world)
        pygame.mixer.music.play(-1)
        self.file_world = Hume_screen.home_screen(self.main_screen)
        self.name_of_file_with_inventory = "Saves_inventory\inventory" + self.file_world
        self.file_inventory = open(pathlib.Path(pathlib.Path.cwd(),
                                   "Saves_inventory", "inventory" + self.file_world), 'r')
        self.inventory = inventoty.Inventory(self.file_inventory, main_screen)
        self.block_in_hands = 0
        self.massive_slov, self.map_types = file.load_map(self.file_world)
        self.main_hero = mobs.Person(
            SIZE_MAP_X // 2, AIR_LAYER - 2, person_images, self.screen)
        self.massive_mobs = list()
        self.x_cam = -self.main_hero.x * \
            SIZE_BLOCK + main_screen.get_size()[0] / 2
        self.y_cam = -self.main_hero.y * \
            SIZE_BLOCK + main_screen.get_size()[1] / 2
        self.finished = False
        self.clock = pygame.time.Clock()
        self.time = 0
        pygame.display.update()

    def process(self):
        while not self.finished:
            self.time += 1
            self.main_screen.fill((0, 0, 0))
            '''начало блока рисования'''
            self.x_cam, self.y_cam = veb_cam(
                self.main_screen, self.x_cam, self.y_cam, self.screen, self.main_hero, self.massive_mobs, self.massive_slov)
            '''конец блока рисования'''
            for self.zombie in self.massive_mobs:
                self.zombie.strike = False
            if self.time % TIME_ZOMBIE_GENERATE == 0:
                self.x1, self.y1 = mobs.generate_mobs(self.massive_slov)
                self.massive_mobs.append(mobs.Zombie(
                    self.x1, self.y1, person_images, self.screen))
            for self.event in pygame.event.get():
                self.main_hero.angle(self.event, self.x_cam, self.y_cam)
                if self.event.type == pygame.QUIT:
                    self.finished = True
                elif self.event.type == pygame.MOUSEBUTTONDOWN:
                    self.main_hero.start_time = pygame.time.get_ticks()
                    if self.event.button == 3:
                        self.main_hero.build(self.block_in_hands, self.massive_slov,
                                             self.inventory)
                    self.main_hero.hit(self.event, self.massive_mobs)
                self.main_hero.angle(self.event, self.x_cam, self.y_cam)
            self.keys = pygame.key.get_pressed()
            music_event(self.keys)
            if self.keys[pygame.K_e]:
                self.block_in_hands = inventoty.inventory_screen(
                    self.main_screen, self.inventory, self.block_in_hands)
            """
            Обработка событий связанных с персонажем и зомби
            """
            self.main_hero.broke(self.massive_slov, self.inventory)
            self.main_hero.input()
            self.main_hero.update_frame_dependent()
            "Обработка событий связанных с зомби"
            for self.zombie in self.massive_mobs:
                self.zombie.input_zombie(self.main_hero)
                self.zombie.update_frame_dependent()
                self.finished = self.zombie.kick(self.main_hero, self.finished)
                self.zombie.control_collision(self.massive_slov)
                self.zombie.move()
            self.main_hero.control_collision(self.massive_slov)
            self.main_hero.move()
            pygame.display.update()
            pygame.display.flip()
        self.file.save_map(self.massive_slov, self.file_world)
        self.inventory.save_inventory(self.name_of_file_with_inventory)
        pygame.quit()
