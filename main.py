from block import *
import pygame
import button
button_quit = button.Button(0,0,40,40,pygame.quit,(),(255,255,255),"quit")
massive_block =[]
generate_map(massive_block)
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