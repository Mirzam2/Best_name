from mobs import *
import pygame
from pygame import surface
from file import *
from spritesheet import SpriteSheet

class Type_block:
    def __init__(self,name, permeability, durability, image, chance_generate = 0, alpha = 1):
        self.name = name
        self.permeability = permeability  # проницаемость
        self.durability = durability  # прочность
        self.size = SIZE_BLOCK  # размер
        self.image = image  # пока цвет кваратика
        self.chance_generate = chance_generate
        self.alpha = alpha  # масштаб
        self.rect = self.image.get_rect()
        self.x = 0
        self.y = 0

    def draw(self, x, y, screen):
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.topleft = x * self.size, y * self.size
        screen.blit(self.image, self.rect)


def types(types_block, person_images):
    ss = SpriteSheet("./all.png")
    types_block[0] = Type_block("Air", True, -1, ss.image_at((96, 0, 48, 48)), 0)
    types_block[1] = Type_block("Dirt", False, 5, ss.image_at((0, 0, 48, 48)), 20)
    types_block[2] = Type_block("Grass", False, 5, ss.image_at((48, 0, 48, 48)), 0)
    types_block[3] = Type_block("Stone", False, 10, ss.image_at((144, 0, 48, 48)), 20)
    types_block[4] = Type_block("Log", False, 10, ss.image_at((192, 0, 48, 48)))
    types_block[5] = Type_block("Sand", False, 10, ss.image_at((240, 0, 48, 48)),5)
    types_block[6] = Type_block("Bedrock", False, -1, ss.image_at((288, 0, 48, 48)))
    types_block[7] = Type_block("Granite", False, 10, ss.image_at((336, 0, 48, 48)),3)
    types_block[8] = Type_block("Amethyst", False, 10, ss.image_at((384, 0, 48, 48)),1)
    types_block[9] = Type_block("Stone1", False, 10, ss.image_at((432, 0, 48, 48)),10)
    types_block[10] = Type_block("Leaves", False, 10, ss.image_at((0, 48, 48, 48)))
    types_block[11] = Type_block("Leaves1", False, 10, ss.image_at((48, 48, 48, 48)))
    types_block[12] = Type_block("Leaves2", False, 10, ss.image_at((96, 48, 48, 48)))
    types_block[13] = Type_block("EmeraldOre", False, 10, ss.image_at((144, 48, 48, 48)),1)
    types_block[14] = Type_block("Emerald", False, 10, ss.image_at((192, 48, 48, 48)))
    types_block[15] = Type_block("GoldOre", False, 10, ss.image_at((240, 48, 48, 48)),1)
    types_block[16] = Type_block("Gold", False, 10, ss.image_at((288, 48, 48, 48)))
    types_block[17] = Type_block("CoalOre", False, 10, ss.image_at((336, 48, 48, 48)),4)
    types_block[18] = Type_block("Coal", False, 10, ss.image_at((384, 48, 48, 48)))
    types_block[19] = Type_block("Planks", False, 10, ss.image_at((432, 0, 48, 48)))
    person_images[0] = ss.image_at((0, 96, 37, 90), (0,0,0))
    person_images[1] = ss.image_at((48, 96, 37, 90), (0, 0, 0))
    person_images[2] = ss.image_at((96, 96, 37, 90), (0, 0, 0))
    person_images[3] = ss.image_at((96+48, 96, 37, 90), (0, 0, 0))
    person_images[4] = ss.image_at((96+96, 96, 37, 90), (0, 0, 0))
    person_images[5] = ss.image_at((96+96+48, 96, 37, 90), (0, 0, 0))

if __name__ == "__main__":
    main_screen = pygame.display.set_mode((1000, 1000))
    massive_block = {}
    types(massive_block, {})
    pygame.init()
    for i in massive_block:
        massive_block[i].draw(10, 10, main_screen)
    finished = False
    pygame.display.update()
    while not finished:
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
    pygame.quit()
    
    
