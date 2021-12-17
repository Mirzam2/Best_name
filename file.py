import json
import pathlib
from os import write
from pathlib import Path

from block import *
from not_constant import person_images, types_block


def save_map(massive_slov: list, world_name="test"):
    """
    функция сохранения данных карты мира
    massive_block - массив для блоков
    world_name - название мира который нужно сохранять
    """
    file = pathlib.Path(pathlib.Path.cwd(), "saves", world_name)
    with open(file, 'w') as input_file:
        main_string = "[" + "\n"
        for slovo in massive_slov:
            string = ""
            for i in slovo:
                string += (str(i) + ", ")
            string = string[:len(string)-2]
            main_string += ("[" + string + "]," + "\n")
        main_string = main_string[:len(main_string)-2]
        main_string += ("\n" + "]")
        input_file.write(main_string)


def load_map(world_name="test"):
    """
    функция загрузки данных карты мира
    massive_block - массив для блоков
    world_name - название мира который нужно загружать
    """
    file = pathlib.Path(pathlib.Path.cwd(), "saves", world_name)
    with open(file, 'r') as f:
        massive_slov = json.load(f)
    map_types = []
    for i in range(len(massive_slov)):
        map_types.append([])
        for j in range(len(massive_slov[i])):
            map_types[i].append(types_block.get(massive_slov[i][j], 0))
    return massive_slov, map_types
