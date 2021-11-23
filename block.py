from mobs import *
import pygame
from pygame import surface


class Block():
    def __init__(self, x, y):
        self.x0 = x
        self.y0 = y
        self.size_block = 40

    def draw(self, surface):
        self.surface = pygame.Surface((self.size_block, self.size_block))
        pygame.draw.rect(self.surface, (100, 100, 255),
                         (0, 0, self.size_block, self.size_block))
        surface.blit(self.surface, (self.x0 * self.size_block, self.y0 * self.size_block))


massive_block=[]
for i in range(5):
    for j in range(5):
        massive_block.append(Block(i, j))
pygame.init()
screen = pygame.display.set_mode((400, 400), pygame.RESIZABLE)
main_hero = main_person(100, 100, screen)
finished = False
FPS = 60
clock = pygame.time.Clock()
pygame.display.update()
while not finished:
    screen.fill((0, 0, 0))
    for i in massive_block:
        i.draw(screen)
    main_hero.draw()
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        main_hero.move(5)
    elif keys[pygame.K_a]:
        main_hero.move(-5)
    pygame.display.update()
pygame.quit()
