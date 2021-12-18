import pygame
from game_module import *

main_screen = pygame.display.set_mode((1000, 800), pygame.RESIZABLE)
game = Game(main_screen)
game.process()
