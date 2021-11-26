import json
import pickle
import pathlib
from pathlib import Path


def save_map(massive_slove: list, world_name="test"):
    """
    функция сохранения данных карты мира
    massive_block - массив для блоков
    world_name - название мира который нужно сохранять
    """
    file = pathlib.Path(pathlib.Path.cwd(), "saves", world_name+".json")
    with open(file, 'w') as f:
        json.dump(massive_slov, f)


def load_map(massive_slov: list, world_name="test"):
    """
    функция загрузки данных карты мира
    massive_block - массив для блоков
    world_name - название мира который нужно загружать
    """
    file = pathlib.Path(pathlib.Path.cwd(), "saves", world_name+".json")
    with open(file, 'r') as f:
        massive_slov = json.load(f)
def draw_map(massive_slov):
    for i in range(massive_slov):
        for j in range(len(massive_slov[i])):
            pass
