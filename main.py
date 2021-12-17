import pygame

from constans import *
from game_module import *
from not_constant import person_images

pygame.init()
main_screen = pygame.display.set_mode((1000, 800), pygame.RESIZABLE)
game = Game(main_screen)
game.process()
