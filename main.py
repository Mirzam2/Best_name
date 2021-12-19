import pygame
import game_module


main_screen = pygame.display.set_mode((1000, 800), pygame.RESIZABLE)
game = game_module.Game(main_screen)
while not game.finished:
    game.process()
