from random import randint
from typing import Any

import pygame
from perlin_noise import PerlinNoise
from pygame import surface

from constans import (AIR_LAYER, GRASS_LAYER, NUMBER_TREES, SIZE_MAP_X,
                      SIZE_MAP_Y)
from not_constant import types_block


def create_field(map: list):
    """
    random card generation function
    map - the array where the card is saved
    """
    generate_layer(map, 0, AIR_LAYER)
    generate_layer(map, 2, GRASS_LAYER)

    noise = PerlinNoise(octaves=10, seed=randint(1, 1000))
    x_gen = SIZE_MAP_X
    y_gen = SIZE_MAP_Y - AIR_LAYER - GRASS_LAYER
    map1 = [[noise([i / x_gen, j / y_gen]) for j in range(x_gen)]
            for i in range(y_gen)]
    massive_chance = []
    calculate_chance(massive_chance)
    for i in range(y_gen):
        for j in range(x_gen):
            flag: Any = True
            for k in range(len(massive_chance)):
                if map1[i][j] < massive_chance[k] and flag:
                    map1[i][j] = k
                    flag = False
            if flag:
                map1[i][j] = 0
    map += map1
    interval = (SIZE_MAP_X - 6) // NUMBER_TREES
    for i in range(NUMBER_TREES):
        generate_tree(map, randint(i * interval + 2,
                                   (i + 1) * interval - 2), AIR_LAYER - 6)
    generate_curb(map)
    return map


def generate_layer(map: list, id: int, number: int = 1):
    """
    Full Layer Generation Function
    map - the array where the card is stored
    id - the index of a block whose layer must be made
    number - number of layers
    """
    for _ in range(number):
        layer = []
        for _ in range(SIZE_MAP_X):
            layer.append(id)
        map.append(layer)


def calculate_chance(list_chance: list):
    """
    Function of counting the chance of generation
    list_chance - an array to be filled
    """
    for i in range(len(types_block)):
        type = types_block.get(i, 0)
        list_chance.append(type.chance_generate)
    summa = sum(list_chance)
    for i in range(len(list_chance)):
        list_chance[i] = list_chance[i] / summa
    for i in range(len(list_chance)):
        list_chance[i] += list_chance[i - 1]
    for i in range(len(list_chance)):
        list_chance[i] = list_chance[i] - 0.5


def generate_tree(map: list, x_tree: int, y_tree: int):
    """
    Tree generating function
    map - map array
    x, y - the coordinates of the upper left tree
    """
    tree = [[0, 0, 10, 0, 0], [0, 11, 10, 11, 0], [12, 11, 4, 11, 12],
            [0, 12, 4, 12, 0], [0, 0, 4, 0, 0], [0, 0, 4, 0, 0]]
    for i in range(len(tree)):
        for j in range(len(tree[i])):
            map[y_tree + i][j + x_tree] = tree[i][j]


def generate_curb(map: list):
    """
    Bedrock wall generation function
    map - list of map
    """
    for i in range(0, SIZE_MAP_X - 1):
        map[0][i] = 6
        map[SIZE_MAP_Y - 1][i] = 6
    for i in range(0, SIZE_MAP_Y - 1):
        map[i][0] = 6
        map[i][SIZE_MAP_X - 1] = 6


def draw_map(list_map: list, screen: surface):
    """
    Drawing map function
    list_map - map array
    screen - map drawing area
    """
    for i in range(len(list_map)):
        for j in range(len(list_map[i])):
            block = types_block.get(list_map[i][j], 0)
            block.draw(j, i, screen)


if __name__ == "__main__":
    pygame.init()
    main_screen = pygame.display.set_mode((1000, 800), pygame.RESIZABLE)
    massive_map = []
    massive_map = create_field(massive_map)
    print(massive_map)
    x = input()
