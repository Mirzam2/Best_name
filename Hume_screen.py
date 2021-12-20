import json
import os
import pathlib
import time
import sys

import pygame

import button
from constans import AIR_LAYER, SIZE_MAP_X
import inventoty
import map
from file import save_map


def new_game():
    """
    Creates a file with a new game
    Creates a file with a map in saves
    Creates an inventory file in Saves_inventory
    The file in Saves_inventory will be different from the file in saves
    The fact that before the main name will be inventory
    """
    tmp = str(int(round(time.time()))) + ".json"
    file = open(pathlib.Path(pathlib.Path.cwd(),
                             "saves_invent", "inventory" + tmp), 'w')
    inventoty.new_file(file)
    open(pathlib.Path(pathlib.Path.cwd(), "saves_map", tmp), 'w')
    massive_words = []
    massive_words = map.create_field(massive_words)
    save_map(massive_words, tmp)
    with open(pathlib.Path(pathlib.Path.cwd(), "saves_units_", "units" + tmp), 'w') as f:
        json.dump([[SIZE_MAP_X // 2, AIR_LAYER - 2, 10]], f)

    return tmp


def restart_game():
    return "restart"


def return_save(content, number):
    """
    Returns a save
    """
    return content[number]


def finish_game():
    return "exit"


def open_main_menu():
    os.execl(sys.executable, sys.executable, *sys.argv)


def saved_games(screen, width, height):
    """
    Draws saves
    width - width of the screen
    height - screen height
    """
    screen.fill("black")
    content = os.listdir(path='saves_map')
    content.sort(reverse=True)
    screen_image = pygame.image.load("wallpapers.png")
    buttons = []
    pygame.init()
    for i in range(min(len(content), 7)):
        tmp = button.Button(width // 2 - width // 8,
                            height // 4 - height // 16 + height // 8 * i, width // 4,
                            height // 16, return_save, (content, i), color=(208, 208, 208), text=content[i])
        buttons.append(tmp)
    finished = False
    result = []
    while not finished:
        if screen.get_height() != height or screen.get_width() != width:  # If the window size has changed,
            # it creates new buttons
            height = screen.get_height()
            width = screen.get_width()
            buttons.clear()
            for i in range(min(len(content), 7)):
                tmp = button.Button(width // 2 - width // 8,
                                    height // 4 - height // 16 + height // 8 * i, width // 4,
                                    height // 16, return_save, (content, i), color=(208, 208, 208), text=content[i])
                buttons.append(tmp)
        screen_image = pygame.transform.scale(screen_image, (screen.get_width(), screen.get_height()))
        screen.blit(screen_image, (0, 0))
        for i in buttons:
            i.drawing(screen)
        pygame.display.update()
        screen.fill("black")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                result.append(None)
                finished = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for i in buttons:
                    if i.tap(event) is not None:
                        result.append(i.tap(event))
                        finished = True
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            result.append(None)
            finished = True
    return result[0]


class Menu:
    """
    Main Menu
    It is necessary to submit only pygame.Surface
    """

    def __init__(self, screen):
        self.height = screen.get_height()
        self.width = screen.get_width()
        self.new_game_button = button.Button(self.width // 2 - self.width // 8,
                                             self.height // 2 - self.height // 16, self.width // 4,
                                             self.height // 16, new_game, (), color=(208, 208, 208), text="New game")
        self.button_saved_games = button.Button(self.width // 2 - self.width // 8,
                                                self.height // 2 - self.height // 16 + self.height // 8,
                                                self.width // 4, self.height // 16, saved_games,
                                                (screen, self.width, self.height), color=(208, 208, 208),
                                                text="Saved games")
        self.exit_button = button.Button(self.width // 2 - self.width // 8,
                                         self.height // 2 - self.height // 16 + self.height // 4, self.width // 4,
                                         self.height // 16, finish_game, (), color=(208, 208, 208), text="Exit")

    def event_(self, event):
        """
        Accepts event from pygame.event.get()
        Returns file when closing the game
        Returns the file when opening saving or creating a new game
        """
        result = []
        pre_result = self.exit_button.tap(event)
        if pre_result is not None:
            result.append(pre_result)
        pre_result = self.new_game_button.tap(event)
        if pre_result is not None:
            result.append(pre_result)
        pre_result = self.button_saved_games.tap(event)
        if pre_result is not None:
            result.append(pre_result)
        result.append(None)
        return result[0]

    def update(self, screen):
        """
        Updates the buttons when the screen changes
        """
        self.height = screen.get_height()
        self.width = screen.get_width()
        self.new_game_button = button.Button(self.width // 2 - self.width // 8,
                                             self.height // 2 - self.height // 16, self.width // 4,
                                             self.height // 16, new_game, (), color=(208, 208, 208), text="New game")
        self.button_saved_games = button.Button(self.width // 2 - self.width // 8,
                                                self.height // 2 - self.height // 16 + self.height // 8,
                                                self.width // 4, self.height // 16, saved_games,
                                                (screen, self.width, self.height), color=(208, 208, 208),
                                                text="Saved games")
        self.exit_button = button.Button(self.width // 2 - self.width // 8,
                                         self.height // 2 - self.height // 16 + self.height // 4, self.width // 4,
                                         self.height // 16, finish_game, (), color=(208, 208, 208), text="Exit")

    def draw(self, screen):
        """
        Draws Menu
        If the window size has changed, it calls update
        """
        if screen.get_height() != self.height or screen.get_width() != self.width:
            self.update(screen)
        self.new_game_button.drawing(screen)
        self.button_saved_games.drawing(screen)
        self.exit_button.drawing(screen)


class DeathMenu:
    """
    Death Menu
    It is necessary to submit only pygame.Surface
    """

    def __init__(self, screen):
        self.height = screen.get_height()
        self.width = screen.get_width()
        self.restart_game_button = button.Button(self.width // 2 - self.width // 8,
                                                 self.height // 2 - self.height // 16, self.width // 4,
                                                 self.height // 16, restart_game, (), color=(136, 0, 21),
                                                 text="Restart game")
        self.button_new_menu = button.Button(self.width // 2 - self.width // 8,
                                             self.height // 2 - self.height // 16 + self.height // 8,
                                             self.width // 4, self.height // 16, open_main_menu, (),
                                             color=(136, 0, 21), text="Main menu")
        self.exit_button = button.Button(self.width // 2 - self.width // 8,
                                         self.height // 2 - self.height // 16 + self.height // 4, self.width // 4,
                                         self.height // 16, finish_game, (), color=(136, 0, 21), text="Exit")

    def event_(self, event):
        """
        Accepts event from pygame.event.get()
        Returns file when closing the game
        Returns the file when opening saving or creating a new game
        """
        result = []
        pre_result = self.exit_button.tap(event)
        if pre_result is not None:
            result.append(pre_result)
        pre_result = self.restart_game_button.tap(event)
        if pre_result is not None:
            result.append(pre_result)
        pre_result = self.button_new_menu.tap(event)
        if pre_result is not None:
            result.append(pre_result)
        result.append(None)
        return result[0]

    def update(self, screen):
        self.height = screen.get_height()
        self.width = screen.get_width()
        self.restart_game_button = button.Button(self.width // 2 - self.width // 8,
                                                 self.height // 2 - self.height // 16, self.width // 4,
                                                 self.height // 16, restart_game, (), color=(136, 0, 21),
                                                 text="Restart game")
        self.button_new_menu = button.Button(self.width // 2 - self.width // 8,
                                             self.height // 2 - self.height // 16 + self.height // 8,
                                             self.width // 4, self.height // 16, open_main_menu, (),
                                             color=(136, 0, 21), text="Main menu")
        self.exit_button = button.Button(self.width // 2 - self.width // 8,
                                         self.height // 2 - self.height // 16 + self.height // 4, self.width // 4,
                                         self.height // 16, finish_game, (), color=(136, 0, 21), text="Exit")

    def draw(self, screen):
        """
        Draws Menu
        If the window size has changed, it calls update
        """
        if screen.get_height() != self.height or screen.get_width() != self.width:
            self.update(screen)
        screen_image = pygame.image.load("death.jpg")
        screen_image = pygame.transform.scale(screen_image, (screen.get_width(), screen.get_height()))
        screen.blit(screen_image, (0, 0))
        self.restart_game_button.drawing(screen)
        self.exit_button.drawing(screen)
        self.button_new_menu.drawing(screen)


def home_screen(screen):
    """
    Draws the main screen
    Returns a save file or a new file
    It can return False, which will mean closing
    """
    pygame.init()
    screen_image = pygame.image.load("wallpapers.png")
    x = Menu(screen)
    fin = False
    result = None
    pygame.init()
    while not fin:
        screen_image = pygame.transform.scale(screen_image, (screen.get_width(), screen.get_height()))
        screen.blit(screen_image, (0, 0))
        x.draw(screen)
        pygame.display.update()
        screen.fill("black")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                result = x.event_(event)
                if result is not None:
                    if result == "exit":
                        fin = True
                        pygame.quit()
                        exit()
                    else:
                        fin = True
    return result


def death_screen(screen, hero):
    """
    Draws the death screen
    """
    pygame.init()
    x = DeathMenu(screen)

    fin = False
    result = None
    pygame.init()
    while not fin:
        x.draw(screen)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                result = x.event_(event)
                if result is not None:
                    if result == "exit":
                        fin = True
                        pygame.quit()
                        exit()
                    elif result == "restart":
                        fin = True
                        hero.revive()
                    else:
                        fin = True
    print("result1: ", result)
    return result
