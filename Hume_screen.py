import pygame
import button
import time
import os
import shutil
import map
from file import save_map
FPS = 60
clock = pygame.time.Clock()
def new_game():
    tmp = str(time.time()) + ".json"
    file = open("saves" + "\\" + tmp, 'w')
    shutil.copyfile(r"saves\test.json", r"saves" + "\\" + tmp, follow_symlinks=True)
    massive_slov =[]
    massive_slov = map.create_field(massive_slov)
    save_map(massive_slov,tmp)
    return tmp

def return_save(x, number):
    return x[number]

def saved_games(screen, width, height):
    screen.fill("black")
    content = os.listdir(path='saves')
    print(content)
    buttons = []
    for i in range(min(len(content), 5)):
        tmp = button.Button(width // 2 - width // 8,\
            height // 3 - height // 16 + height // 8 * i, width // 4,\
           height // 16 , return_save, (content, i), color=(128, 128, 128), text=content[i])
        buttons.append(tmp)
    finished = False
    result = ""
    while(not finished):
        pygame.init()
        for i in buttons:
            i.drawing(screen)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for i in buttons:
                    y = i.tap(event)
                    if type(y) == str:
                        finished = True
                        result = y
        screen.fill("black")
    return result

def finish_game():
    pygame.quit
    return False
class Menu:
    def __init__(self, screen):
        self.height = screen.get_height()
        self.width = screen.get_width()
        self.new_game_button = button.Button(self.width // 2 - self.width // 8,\
            self.height // 2 - self.height // 16, self.width // 4,\
           self.height // 16, new_game, (), color=(128, 128, 128), text="New game")
        self.button_saved_games = button.Button(self.width // 2 - self.width // 8,\
            self.height // 2 - self.height // 16 + self.height // 8, self.width // 4,\
           self.height // 16, saved_games, (screen, self.width, self.height), color=(128, 128, 128), text="Saved games")
        self.exit_button = button.Button(self.width // 2 - self.width // 8,\
            self.height // 2 - self.height // 16 + self.height // 4 , self.width // 4,\
           self.height // 16, finish_game, (), color=(128, 128, 128), text="Exit")  
    
    def event_ (self, eventq):
        y = self.exit_button.tap(eventq)
        if y != None: return y
        y = self.new_game_button.tap(eventq)
        if y != None: return y
        y = self.button_saved_games.tap(eventq)
        if y != None: return y
  
    def draw(self,screen):
        self.new_game_button.drawing(screen)
        self.button_saved_games.drawing(screen)
        self.exit_button.drawing(screen)



def hyme_screen(screen):
    pygame.init()
    x = Menu(screen)
    f = True
    while(f):
        pygame.init()
        x.draw(screen)
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    finished = True
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    y = x.event_(event)
                    if type(y) == bool:
                        if y == False:
                            f = y
                        print(y)
                    if type(y) == str:
                        f = False
                        print(y)
                        break
        pygame.display.update()
        screen.fill("black")
    return y
if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((800, 800), pygame.RESIZABLE)
    x = Menu(screen)
    f = True
    while(f):
        pygame.init()
        x.draw(screen)
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    finished = True
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    y = x.event_(event)
                    if type(y) == bool:
                        if y == False:
                            f = y
                    print(y)
        pygame.display.update()
        screen.fill("black")