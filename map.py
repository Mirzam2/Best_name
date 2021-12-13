from perlin_noise import PerlinNoise
from random import randint

import pygame
from block import types
from constans import AIR_LAYER, NUMBER_TREES, SIXE_MAP_Y, SIZE_MAP_X


def create_field(map: list):
    pygame.init()
    main_screen = pygame.display.set_mode((1000, 800), pygame.RESIZABLE)
    types_block = {}
    person_images = {}
    types(types_block, person_images)
    for i in range(AIR_LAYER+1):
        layer = []
        for j in range(SIZE_MAP_X):
            layer.append(0)
        map.append(layer)
    layer = []
    for j in range(SIZE_MAP_X):
        layer.append(2)
    map.append(layer)
    noise = PerlinNoise(octaves=10, seed=randint(1, 1000))
    xpix = SIZE_MAP_X
    ypix = SIXE_MAP_Y-3-AIR_LAYER
    map1 = [[noise([i/xpix, j/ypix]) for j in range(xpix)]
            for i in range(ypix)]
    print(map1)
    massive_chance = []
    massive_chance = calculate_chance(massive_chance, types_block)
    print(massive_chance)
    for i in range(ypix):
        for j in range(xpix):
            flag = True
            for k in range(len(massive_chance)):
                if map1[i][j] < massive_chance[k] and flag:
                    map1[i][j] = k
                    flag = False
            if flag == True:
                map1[i][j] = 0
    map += map1
    interval = (SIZE_MAP_X-6) // NUMBER_TREES
    for i in range(NUMBER_TREES):
        generate_tree(map, randint(i * interval + 2,
                      (i + 1) * interval - 2), AIR_LAYER-5)
    return map


def calculate_chance(massive_chance: list, types_block):
    for i in range(len(types_block)):
        type = types_block.get(i, 0)
        massive_chance.append(type.chance_generate)
    summa = sum(massive_chance)
    for i in range(len(massive_chance)):
        massive_chance[i] = massive_chance[i] / summa
    for i in range(len(massive_chance)):
        massive_chance[i] += massive_chance[i-1]
    for i in range(len(massive_chance)):
        massive_chance[i] = massive_chance[i] - 0.5
    return(massive_chance)


def generate_tree(map, x, y):
    """
    Функция генерация дерева
    map - объект класса list, массив карты
    x, y - координаты верхнего левого дерева
    """
    tree = [
        [0, 0, 10, 0, 0],
        [0, 11, 10, 11, 0],
        [12, 11, 10, 11, 12],
        [0, 12, 4, 12, 0],
        [0, 0, 4, 0, 0],
        [0, 0, 4, 0, 0]
    ]
    for i in range(len(tree)):
        for j in range(len(tree[i])):
            map[y+i][j+x] = tree[i][j]

def generate_curb(map):
    pass
if __name__ == "__main__":
    pygame.init()
    main_screen = pygame.display.set_mode((1000, 800), pygame.RESIZABLE)
    types_block = {}
    person_images = {}
    types(types_block, person_images)
    massive_map = []
    massive_map = create_field(massive_map)
    print(massive_map)
    x = input()
