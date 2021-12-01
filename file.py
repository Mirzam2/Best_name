import json
from os import write
import pickle
import pathlib
from pathlib import Path
from block import *

def save_map(massive_slov: list, world_name="test"):
    """
    функция сохранения данных карты мира
    massive_block - массив для блоков
    world_name - название мира который нужно сохранять
    """
    file = pathlib.Path(pathlib.Path.cwd(), "saves", world_name+".json")
    with open(file, 'w') as input_file:
        main_string = "[" + "\n"
        for slovo in massive_slov:
            string = ""
            for i in slovo:
                string += (str(i) + ", ")
            string = string[:len(string)-2]
            main_string+=("[" + string + "]," + "\n")
        main_string = main_string[:len(main_string)-2]
        main_string+=("\n" + "]")
        input_file.write(main_string)


def load_map(world_name="test"):
    """
    функция загрузки данных карты мира
    massive_block - массив для блоков
    world_name - название мира который нужно загружать
    """
    file = pathlib.Path(pathlib.Path.cwd(), "saves", world_name+".json")
    with open(file, 'r') as f:
        massive_slov = json.load(f)
    return massive_slov
def draw_map(massive_slov, types_block, screen):
    for i in range(len(massive_slov)):
        for j in range(len(massive_slov[i])):
            drovable_block = types_block.get(massive_slov[j][i], 0)
            drovable_block.draw(i, j, screen)
