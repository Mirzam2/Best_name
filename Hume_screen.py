import pygame
import time
import os
import pathlib
import shutil
import button
import map
import inventoty

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
                "Saves_inventory", "inventory" + tmp), 'wt+')
    inventoty.new_file(file)
    open(pathlib.Path(pathlib.Path.cwd(), "saves", tmp), 'w')
    shutil.copyfile(pathlib.Path(pathlib.Path.cwd(), "saves", "test.json"), pathlib.Path(
        pathlib.Path.cwd(), "saves", tmp), follow_symlinks=True)
    massive_words = []
    massive_words = map.create_field(massive_words)
    save_map(massive_words, tmp)
    return tmp


def return_save(content, number):
    """
    Returns a save
    """
    return content[number]


def saved_games(screen, width, height):
    """
    Draws saves
    width - width of the screen
    height - screen height
    """
    screen.fill("black")
    content = os.listdir(path='saves')
    screen_image = pygame.image.load("wallpapers.jpg")
    buttons = []
    pygame.init()
    for i in range(min(len(content), 5)):
        tmp = button.Button(width // 2 - width // 8,
                            height // 3 - height // 16 + height // 8 * i, width // 4,
                            height // 16, return_save, (content, i), color=(128, 128, 128), text=content[i])
        buttons.append(tmp)
    finished = False
    while not finished:
        screen.blit(screen_image, (0, 0))
        for i in buttons:
            i.drawing(screen)
        pygame.display.update()
        screen.fill("black")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for i in buttons:
                    result = i.tap(event)
                    if result is not None:
                        finished = True
                        return result


def finish_game():
    return "exit"


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
                                             self.height // 16, new_game, (), color=(128, 128, 128), text="New game")
        self.button_saved_games = button.Button(self.width // 2 - self.width // 8,
                                                self.height // 2 - self.height // 16 + self.height // 8,
                                                self.width // 4, self.height // 16, saved_games,
                                                (screen, self.width, self.height), color=(128, 128, 128),
                                                text="Saved games")
        self.exit_button = button.Button(self.width // 2 - self.width // 8,
                                         self.height // 2 - self.height // 16 + self.height // 4, self.width // 4,
                                         self.height // 16, finish_game, (), color=(128, 128, 128), text="Exit")

    def event_(self, event):
        """
        Accepts event from pygame.event.get()
        Returns file when closing the game
        Returns the file when opening saving or creating a new game
        """
        result = self.exit_button.tap(event)
        if result is not None:
            return result
        result = self.new_game_button.tap(event)
        if result is not None:
            return result
        result = self.button_saved_games.tap(event)
        if result is not None:
            return result

    def draw(self, screen):
        """
        Draws Menu
        """
        self.new_game_button.drawing(screen)
        self.button_saved_games.drawing(screen)
        self.exit_button.drawing(screen)


def home_screen(screen):
    """
    Draws the main screen
    Returns a save file or a new file
    It can return False, which will mean closing
    """
    pygame.init()
    screen_image = pygame.image.load("wallpapers.jpg")
    x = Menu(screen)
    fin = False
    result = None
    pygame.init()
    while not fin:
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
