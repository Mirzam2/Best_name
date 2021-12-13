from perlin_noise import PerlinNoise
from random import randint
import pygame
from block import types
from constans import AIR_LAYER, NUMBER_TREES, SIZE_MAP_Y, SIZE_MAP_X


def create_field(map: list):
    """
    Функция генерации произвольной карты
    """
    pygame.init()
    types_block = {}
    person_images = {}
    types(types_block, person_images)
    generate_air(map)
    layer = []
    for j in range(SIZE_MAP_X):
        layer.append(2)
    map.append(layer)
    noise = PerlinNoise(octaves=10, seed=randint(1, 1000))
    xpix = SIZE_MAP_X
    ypix = SIZE_MAP_Y-AIR_LAYER
    map1 = [[noise([i/xpix, j/ypix]) for j in range(xpix)]
            for i in range(ypix)]
    massive_chance = []
    massive_chance = calculate_chance(massive_chance, types_block)
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
    # generate_cave(map)
    generate_curb(map)
    return map

def generate_air(map):
    for i in range(AIR_LAYER + 1):
        layer = []
        for j in range(SIZE_MAP_X):
            layer.append(0)
        map.append(layer)
    pass
def calculate_chance(massive_chance: list, types_block):
    """
    Функция подсчёта шанса генерации
    massive_chance - массив который надо заносить
    types_block - типы блоков
    """
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
    tree = [[0, 0, 10, 0, 0], [0, 11, 10, 11, 0], [12, 11, 10, 11, 12],
            [0, 12, 4, 12, 0], [0, 0, 4, 0, 0], [0, 0, 4, 0, 0]]
    for i in range(len(tree)):
        for j in range(len(tree[i])):
            map[y + i][j + x] = tree[i][j]


def generate_curb(map:list):
    """
    Функция генерация стенок из бедрока
    map - карта
    """
    for i in range(0, SIZE_MAP_X):
        map[0][i] = 6
        map[SIZE_MAP_Y - 2][i] = 6
    for i in range(0, SIZE_MAP_Y - 1):
        map[i][0] = 6
        map[i][SIZE_MAP_X - 1] = 6


def generate_cave(map):
    a = 0.00000001
    c = 1
    b = SIZE_MAP_Y/SIZE_MAP_X * 2 - c / SIZE_MAP_Y - a * SIZE_MAP_X
    for i in range(5, 25):
        k = 2 - 1
        y = int(a*i**3 + b*i**2 + c*i)
        for j in range(i - k, i + k + 1):
            for l in range(y - k, y + k + 1):
                if l < SIZE_MAP_Y and i < SIZE_MAP_X:
                    map[l][j] = 0


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
