import pygame
from pygame import surface
import json

from constans import SIZE_BLOCK
from spritesheet import SpriteSheet


class TypeBlock:
    def __init__(self, name: str, permeability: bool, durability: int, image: surface, chance_generate: int = 0):
        """
        Block subtype generation
        name - name
        permeability - whether to go through a block
        durability - how many ticks will break the block
        image - the image corresponding to the block
        chance_generate - probability to appear
        """
        self.name = name
        self.permeability = permeability
        self.durability = durability
        self.size = SIZE_BLOCK
        self.image = image
        self.chance_generate = chance_generate
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
    with open('blocks.json', 'r') as f:
        data = json.load(f)
        for btype, binfo in data.items():
            types_block[binfo["id"]] = TypeBlock(btype, binfo["permeability"], binfo["durability"],
                                                 ss.image_at(tuple(binfo["sheet_rect"])), binfo["chance_generate"])

    person_images[0] = ss.image_at((0, 96, 45, 90), (0, 0, 0))
    person_images[1] = ss.image_at((48, 96, 45, 90), (0, 0, 0))
    person_images[2] = ss.image_at((96, 96, 45, 90), (0, 0, 0))
    person_images[3] = ss.image_at((144, 96, 45, 90), (0, 0, 0))
    person_images[4] = ss.image_at((192, 96, 45, 90), (0, 0, 0))
    person_images[5] = ss.image_at((240, 96, 45, 90), (0, 0, 0))
    person_images[6] = ss.image_at((0, 192, 45, 90), (255, 255, 255))
    person_images[7] = ss.image_at((48, 192, 45, 90), (255, 255, 255))
    person_images[8] = ss.image_at((96, 192, 45, 90), (255, 255, 255))
    person_images[9] = ss.image_at((144, 192, 45, 90), (255, 255, 255))


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
