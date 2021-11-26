from mobs import *
import pygame
from pygame import surface
class Block():
    def __init__(self, x, y):
        self.x0 = x
        self.y0 = y
        self.size_block = 40
        self.surface = pygame.Surface((self.size_block, self.size_block))
        pygame.draw.rect(self.surface, (150, 150, 150),
                         (0, 0, self.size_block, self.size_block), width=1)  # обводка, потом можно убрать , так будет делать карту проще

    def draw(self, surface):
        surface.blit(self.surface, (self.x0 * self.size_block,
                     self.y0 * self.size_block))


class Air_Block(Block):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.permeability = True  # проницаемость
        self.durability = 0  # прочность
        pygame.draw.rect(self.surface, (150, 150, 250),
                         (0, 0, self.size_block, self.size_block))  # картинку сюда


def generate_new_map(massive_block:list):
    """
    функция создающая новую карту
    massive_block - массив для блоков
    """
    for i in range(5):
        for j in range(1, 5):
            massive_block.append(Block(i, j))
    for i in range(5):
        massive_block.append(Air_Block(i, 0))
if __name__ == "__main__":
    massive_block = []
    generate_new_map(massive_block)
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
