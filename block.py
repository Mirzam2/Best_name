import pygame
from pygame import surface
size_block = 40


class Block():
    def __init__(self, x, y):
        self.x0 = x
        self.y0 = y

    def draw(self, surface):
        global size_block
        self.surface = pygame.Surface((size_block, size_block))
        pygame.draw.rect(self.surface, (100, 100, 255),
                         (0, 0, size_block, size_block))
        surface.blit(self.surface, (self.x0 * size_block, self.y0 * size_block))


massive_block=[]
for i in range(5):
    for j in range(5):
        massive_block.append(Block(i, j))
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
