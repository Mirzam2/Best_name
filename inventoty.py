import pygame
import button
import json
import block
from constans import *
FPS = 60
clock = pygame.time.Clock()

def new_file(file):
    tmp_block = {}
    tmp_pearson = {}
    result = {}
    block.types(tmp_block, tmp_pearson)
    for i in tmp_block:
        result[i] = 0
    json.dump(result,file)


class Inventory:
    def __init__(self, file, screen):
        self.blocks = {}
        block.types(self.blocks, {})
        self.height = screen.get_height()
        self.width = screen.get_width()
        self.main_massive = json.load(file)
        self.massiv_of_buttons = []
        self.massiv_of_buttons.append(button.Button(3/4 * self.width - 48, self.height * 1/4, 48,48,exit_, (),color=(73, 66, 61), text=" "))
        create_buttons(self.massiv_of_buttons,self.blocks,self.width,self.height)
        
    def draw(self, screen):
        pygame.draw.rect(screen, (128, 128, 128), (self.width - 3 * self.width // 4,\
            self.height - 3 * self.height // 4, self.width // 2, self.height // 2))
        j = 0
        k = 1
        for i in self.main_massive:
            if (j + 1) * 3/2 * 48 + 48 > self.width // 2:
                k = k + 1
                j = 0
            self.blocks[int(i)].draw((self.width - 3 * self.width // 4)/48 + j * 3/2 + 1, (self.height - 3 * self.height // 4)/48 + k * 3/2, screen)
            j = j + 1
        self.massiv_of_buttons[0].drawing(screen)

    def add_block(self, type_of_block):
        self.main_massive.setdefault(type_of_block)

    def event_(self, event):
        for i in self.massiv_of_buttons:
            result = i.tap(event)
            if result != None:
                return result

def create_buttons(massiv_of_buttons, blocks, width, height):
    j = 0
    k = 1
    for i in blocks:
        if (j + 1) * 3/2 * 48 + 48 > width // 2:
            k = k + 1
            j = 0
        tmp = button.Button(width - 3 * width // 4 + 48 * j * 3/2 + 48,\
           height - 3 * height // 4 + 48 * k * 3/2, 48, 48, return_button,\
           (blocks, i))
        j = j + 1
        massiv_of_buttons.append(tmp)

def return_button(blocks, i):
    return blocks[i]

def exit_():
    return False


if __name__ == "__main__":
    screen = pygame.display.set_mode((1000, 1000))
    pygame.init()
    with open ("tmp_invent.json", 'w') as file:
        new_file(file)
    file = open ("tmp_invent.json", 'r')
    m = Inventory(file, screen) 
    finished = False
    while(not finished):
        m.draw(screen)
        for event in pygame.event.get():
                 if event.type == pygame.QUIT:
                     finished = True
                 elif event.type == pygame.MOUSEBUTTONDOWN:
                     y = m.event_(event)
                     if type(y) == bool:
                         if y == False:
                             finished = y
                     print(y)
        pygame.display.update()