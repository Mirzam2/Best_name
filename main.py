from block import *
from mobs import *
import pygame
import button
from file import *


def veb_cam(main_screen):
    size_y = len(massive_slov)
    size_x = len(massive_slov[1])
    screen = pygame.Surface((size_x * 48, size_y * 48))
    main_hero.screen = screen
    draw_map(massive_slov, types_block, screen)
    main_hero.draw()
    size_screen = main_screen.get_size()
    main_screen.blit(screen, (-main_hero.x * 48 + size_screen[0] / 2, -main_hero.y * 48 + size_screen[1] / 2))


massive_slov = load_map()
types_block = {}
main_screen = pygame.display.set_mode((1000, 800), pygame.RESIZABLE)
types(types_block)
main_hero = main_person(0, 0, main_screen)
finished = False
FPS = 60
clock = pygame.time.Clock()
pygame.display.update()
while not finished:
    main_screen.fill((0, 0, 0))
    '''начало блока рисования'''
    veb_cam(main_screen)
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
