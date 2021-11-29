from mobs import *
import pygame
from pygame import surface
from file import *
class Type_block():
    def __init__(self,name, permeability, durability, cartinka, alpha = 1):
        self.name = name
        self.permeability = permeability  # проницаемость
        self.durability = durability  # прочность
        self.size = 40 # размер
        self.cartinka = cartinka # пока цвет кваратика
        self.alpha = alpha # масштаб
    def draw(self, x, y, screen):
    	pygame.draw.rect(screen, self.cartinka, (x * self.size, y * self.size, self.size, self.size))


def types(types_block):
    types_block[0] = Type_block("Air", True, -1, (0, 0, 0))
    types_block[1] = Type_block("Dirt", False, 10, (0, 225, 0))

if __name__ == "__main__":
    massive_block = []
    pygame.init()
    screen = pygame.display.set_mode((400, 400))
    for i in massive_block:
        i.draw(screen)
    finished = False
    pygame.display.update()
    while not finished:
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
    pygame.quit()
    
    
