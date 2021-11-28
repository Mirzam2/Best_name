from block import *
from mobs import *
import pygame
import button
from file import *

size_map_x = 20
size_map_y = 20
massive_slov = load_map()
types_block = {}
types(types_block)
screen = pygame.display.set_mode((400, 400), pygame.RESIZABLE)
main_hero = main_person(0, 2, screen)
finished = False
FPS = 60
clock = pygame.time.Clock()
pygame.display.update()
while not finished:
    screen.fill((0, 0, 0))
    '''начало блока рисования'''
    draw_map(massive_slov, types_block, screen)
    main_hero.draw()
    '''конец блока рисования'''
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
    pygame.display.update()
save_map(massive_slov)
pygame.quit()
