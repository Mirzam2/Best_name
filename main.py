from block import *
from mobs import *
import pygame
import button
from file import *

size_map_x = 24
size_map_y = 24
massive_slov = load_map()
types_block = {}
screen = pygame.display.set_mode((1000, 800), pygame.RESIZABLE)
types(types_block)
main_hero = main_person(0, 0, screen)
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
    main_hero.control_collision(massive_slov)
    main_hero.move(event)
    pygame.display.update()
save_map(massive_slov)
pygame.quit()
