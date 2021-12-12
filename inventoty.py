import pygame
import button
import json

class Inventory:
    def __init__(self, file, screen):
        self.height = screen.get_height()
        self.width = screen.get_width()
        self.main_massive = json.load(file)
        
    def draw(self, screen):
        pygame.draw.rect(screen, color=(128, 128, 128), (self.width - self.width // 4, self.height - self.height // 4, self.width // 2, self.height // 2))