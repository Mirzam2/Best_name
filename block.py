from mobs import *
import pygame
from pygame import surface
from file import *


class Type_block():
    def __init__(self,name, permeability, durability, cartinka, alpha = 1):
        self.name = name
        self.permeability = permeability  # проницаемость
        self.durability = durability  # прочность
        self.size_block = 40
        self.cartinka = cartinka
        self.alpha = alpha


def types(types_block):
    types_block.update(["a", Type_block("Air", True, -1, "h" )])
    types_block.update(["d", Type_block("Dirt", False, 10, "g")])

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
