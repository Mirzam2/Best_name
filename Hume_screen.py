import pygame
import button
import time
import os
import shutil
import map
import inventoty
import pathlib
from file import save_map
FPS = 60
clock = pygame.time.Clock()


def new_game():
    """
    Создаёт фаил с новой игрой
    Созвдаёт файл с картой в saves
    Создаёт фаил с инвентарём в Saves_inventory
    Фаил в Saves_inventory будет отличаться от фаила в saves
    Тем, что перед основным названием будет inventory
    """
    tmp = str(int(round(time.time()))) + ".json"
    file = open(pathlib.Path(pathlib.Path.cwd(),
                "Saves_inventory", "inventory" + tmp), 'wt+')
    inventoty.new_file(file)
    file = open(pathlib.Path(pathlib.Path.cwd(), "saves", tmp), 'w')
    shutil.copyfile(pathlib.Path(pathlib.Path.cwd(), "saves", "test.json"), pathlib.Path(
        pathlib.Path.cwd(), "saves", tmp), follow_symlinks=True)
    massive_slov = []
    massive_slov = map.create_field(massive_slov)
    save_map(massive_slov, tmp)
    return tmp


def return_save(content, number):
    """
    Возвращает сохранение
    """
    return content[number]


def saved_games(screen, width, height):
    """
    Рисует сохранения
    width - ширина экрана
    height - высота экрана
    """
    screen.fill("black")
    content = os.listdir(path='saves')
    screen_image = pygame.image.load("MuoOgkxsoVo.jpg")
    buttons = []
    for i in range(min(len(content), 5)):
        tmp = button.Button(width // 2 - width // 8,
                            height // 3 - height // 16 + height // 8 * i, width // 4,
                            height // 16, return_save, (content, i), color=(128, 128, 128), text=content[i])
        buttons.append(tmp)
    finished = False
    result = None
    while not finished:
        pygame.init()
        screen.blit(screen_image, (0, 0))
        for i in buttons:
            i.drawing(screen)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for i in buttons:
                    result = i.tap(event)
                    if result is not None:
                        finished = True
        screen.fill("black")
    print(result)
    return result


def finish_game():
    return "exit"


class Menu:
    """
    Главное меню
    Надо подать только pygame.Surface
    """

    def __init__(self, screen):
        self.height = screen.get_height()
        self.width = screen.get_width()
        self.new_game_button = button.Button(self.width // 2 - self.width // 8,
                                             self.height // 2 - self.height // 16, self.width // 4,
                                             self.height // 16, new_game, (), color=(128, 128, 128), text="New game")
        self.button_saved_games = button.Button(self.width // 2 - self.width // 8,
                                                self.height // 2 - self.height // 16 + self.height // 8, self.width // 4,
                                                self.height // 16, saved_games, (screen, self.width, self.height), color=(128, 128, 128), text="Saved games")
        self.exit_button = button.Button(self.width // 2 - self.width // 8,
                                         self.height // 2 - self.height // 16 + self.height // 4, self.width // 4,
                                         self.height // 16, finish_game, (), color=(128, 128, 128), text="Exit")

    def event_(self, eventq):
        """
        Принимает event из pygame.event.get()
        Возвращает False при закрытии игры
        Возыращает фаил при открытии сохранения или создании новой игры
        """
        y = self.exit_button.tap(eventq)
        if y is not None:
            return y
        y = self.new_game_button.tap(eventq)
        if y is not None:
            return y
        y = self.button_saved_games.tap(eventq)
        if y is not None:
            print(y)
            return y

    def draw(self, screen):
        """
        Рисукт Menu
        """
        self.new_game_button.drawing(screen)
        self.button_saved_games.drawing(screen)
        self.exit_button.drawing(screen)


def hyme_screen(screen):
    """
    Рисует главный экран
    Возвращает фаил сохранения или новый фаил
    Может вернуть False,  что будет означать закрытие
    """
    pygame.init()
    screen_image = pygame.image.load("MuoOgkxsoVo.jpg")
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
