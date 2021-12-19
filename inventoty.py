import json

import pygame
import pygame.freetype
from pygame import image

import block
import button
from not_constant import types_block

pygame.font.init()


def new_file(file):
    """
    Fills in a new file to save inventory
    """
    result = {}
    for i in types_block:
        result[i] = 0
    json.dump(result, file)


class Inventory:
    """
    Inventory
    It is required to submit a file with inventory
    And Pygame.Surface
    """

    def __init__(self, file, screen):
        self.file = file
        self.blocks = {}
        block.types(self.blocks, {})
        self.reverse_block = {}
        for i in self.blocks:
            self.reverse_block[self.blocks[i]] = int(i)
        self.height = screen.get_height()
        self.width = screen.get_width()
        self.main_massive = json.load(file)
        self.mas_of_buttons = []

    def update(self, screen):
        """
        If the window size has changed, it creates new buttons
        """
        self.height = screen.get_height()
        self.width = screen.get_width()
        create_buttons(self.main_massive, self.mas_of_buttons, self.blocks,
                       self.width, self.height)

    def draw(self, screen):
        """
        Accepts pygame.Surface
        Draws inventory on it
        If the window size has changed, it calls update
        """
        if self.width != screen.get_width() or self.height != screen.get_height():
            self.update(screen)
        f1 = pygame.font.SysFont('arial', 36)
        pygame.draw.rect(screen, (128, 128, 128), (self.width - 3 * self.width // 4,
                                                   self.height - 3 * self.height // 4, self.width // 2,
                                                   self.height // 2))
        j = 0
        k = 1
        for i in self.main_massive:
            if (j + 1) * 3 / 2 * 48 + 48 > self.width // 2:
                k = k + 1
                j = 0
            self.blocks[int(i)].draw((self.width - 3 * self.width // 4) / 48 + j * 3 / 2 + 1,
                                     (self.height - 3 * self.height // 4) / 48 + k * 3 / 2, screen)
            tmp_text = f1.render(str(self.main_massive.get(str(i))), False,
                                 (255, 255, 255))
            screen.blit(tmp_text, (self.width - 3 * self.width // 4 + 48 * j * 3 / 2 + 48,
                                   self.height - 3 * self.height // 4 + 48 * k * 3 / 2))
            j = j + 1

    def add_or_delete_block(self, number_of_block, num):
        """
        Accepts number_of_block - the block number and changes the number of blocks in the inventory
        num - the number of blocks to add or remove
        If num < 0, the blocks are removed from the inventory
        If num > 0, then blocks are added
        Returns the same block if they still exist
        If the blocks of this type have run out, it returns 0
        """
        tmp = self.main_massive.get(str(number_of_block))
        if tmp + num >= 0:
            self.main_massive[str(number_of_block)] = tmp + num
            return number_of_block
        else:
            return 0

    def event_(self, event):
        """
        Takes event from pygame.event.get()
        And returns the block type if there are no blocks 0
        Returns False if the exit button is clicked
        Returns None in all other cases,
        even if there are 0 blocks
        """
        for i in self.mas_of_buttons:
            result = i.tap(event)
            if result is not None:
                return result

    def save_inventory(self, file):
        """
        Saves inventory to a file
        Open the inventory file for recording and run this function
        """
        file = open(file, 'w')
        json.dump(self.main_massive, file)


def create_buttons(main_massive, mas_of_buttons, blocks, width, height):
    """
    Creates buttons in the inventory
    """
    j = 0
    k = 1
    for i in blocks:
        if (j + 1) * 3 / 2 * 48 + 48 > width // 2:
            k = k + 1
            j = 0
        tmp = button.Button(width - 3 * width // 4 + 48 * j * 3 / 2 + 48,
                            height - 3 * height // 4 + 48 * k * 3 / 2, 48, 48, return_button,
                            (main_massive, i))
        j = j + 1
        mas_of_buttons.append(tmp)


def return_button(main_massive, i):
    """
    Returns a block when you click on it,
    if the blocks are not 0
    In other cases it returns 0
    """
    if main_massive.get(str(i)) != 0:
        return int(i)
    else:
        return 0


def inventory_screen(screen, inventory, block_in_hands):
    finished = False
    result = block_in_hands
    while not finished:
        inventory.draw(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pre_result = inventory.event_(event)
                if type(pre_result) == int:
                    result = pre_result
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            finished = True
        pygame.display.update()
    return result
