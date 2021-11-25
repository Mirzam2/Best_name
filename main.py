from block import *
import pygame
import button
massive_block = []
generate_new_map(massive_block)
screen = pygame.display.set_mode((400, 400), pygame.RESIZABLE)
main_hero = main_person(80, 80, screen)
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
save_map(massive_block)
pygame.quit()
