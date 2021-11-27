import pygame
import button
import time
FPS = 60
clock = pygame.time.Clock()

def new_game():
    file = open(str(time.time()) + ".json", 'w')
    return file
def saved_games():
    return True
class Menu:
    def __init__(self, width, height):
        self.screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
        self.new_game_button = button.Button(width // 2 - width // 8,\
            height // 2 - height // 16, width // 4,\
           height // 16, new_game, (), color=(128, 128, 128), text="New game")
        self.button_saved_games = button.Button(width // 2 - width // 8,\
            height // 2 - height // 16 + height // 8, width // 4,\
           height // 16, saved_games, (), color=(128, 128, 128), text="Saved games")
        self.exit_button = button.Button(width // 2 - width // 8,\
            height // 2 - height // 16 + height // 4 , width // 4,\
           height // 16, pygame.quit, (), color=(128, 128, 128), text="Exit")  
    
    def event_ (self, eventq):
        y = self.exit_button.tap(eventq)
        if y != None: return y
        y = self.new_game_button.tap(eventq)
        if y != None: return y
        y = self.button_saved_games.tap(eventq)
        if y != None: return y
  
    def draw(self):
        self.new_game_button.drawing(self.screen)
        self.button_saved_games.drawing(self.screen)
        self.exit_button.drawing(self.screen)



pygame.init()
x = Menu(600, 600)
f = True
while(True):
    pygame.init()
    x.draw()
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                y = x.event_(event)
                #print(y)
                
    pygame.display.update()