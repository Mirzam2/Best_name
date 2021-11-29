from mobs import *
import pygame
from pygame import surface
from file import *
from spritesheet import SpriteSheet


class Type_block():
    def __init__(self,name, permeability, durability, image, alpha = 1):
        self.name = name
        self.permeability = permeability  # проницаемость
        self.durability = durability  # прочность
        self.size = 48 # размер
        self.image = image # пока цвет кваратика
        self.alpha = alpha # масштаб
        self.rect = self.image.get_rect()
        self.x = 0
        self.y = 0
    def draw(self, x, y, screen):
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.topleft = x * self.size, y * self.size
        screen.blit(self.image, self.rect)


def types(types_block):
    ss = SpriteSheet("./all.png")
    types_block[0] = Type_block("Air", True, -1, ss.image_at((96, 0, 48, 48)))
    types_block[1] = Type_block("Dirt", False, 10, ss.image_at((0, 0, 48, 48)))
    types_block[2] = Type_block("Grass", False, 10, ss.image_at((48, 0, 48, 48)))

if __name__ == "__main__":
    massive_block = []
    pygame.init()
    screen = pygame.display.set_mode((480, 480))
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
    
    
