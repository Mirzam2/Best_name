from block import *
from mobs2 import *
import pygame
import button
from file import *


def veb_cam(main_screen,x_cam,y_cam):
    size_y = len(massive_slov)
    size_x = len(massive_slov[1])
    screen = pygame.Surface((size_x * 48, size_y * 48))
    main_hero.screen = screen
    draw_map(massive_slov, types_block, screen)
    main_hero.draw()
    size_screen = main_screen.get_size()
    hight = size_screen[1]
    width = size_screen[0]
    x_cam = -main_hero.x * 48 + main_screen.get_size()[0] / 2
    y_cam = -main_hero.y * 48 + main_screen.get_size()[1] / 2
    main_screen.blit(screen, (x_cam,y_cam))
    return(x_cam,y_cam)
massive_slov = load_map()
types_block = {}
main_screen = pygame.display.set_mode((1000, 800), pygame.RESIZABLE)
types(types_block)
main_hero = Main_person(0, 0, main_screen)
x_cam = -main_hero.x * 48 + main_screen.get_size()[0] / 2
y_cam = -main_hero.y * 48 + main_screen.get_size()[1] / 2
finished = False
FPS = 60
clock = pygame.time.Clock()
pygame.display.update()
while not finished:
    main_screen.fill((0, 0, 0))
    '''начало блока рисования'''
    x_cam, y_cam = veb_cam(main_screen, x_cam, y_cam)
    '''конец блока рисования'''
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
    main_hero.input(event)
    main_hero.control_collision(massive_slov, types_block)
    main_hero.move()
    pygame.display.update()
save_map(massive_slov)
pygame.quit()
