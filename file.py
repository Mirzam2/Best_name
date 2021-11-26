import json
import pickle
import pathlib
from pathlib import Path

def save_data(massive_block,main_person):
    pass
def save_map(massive_block: list, world_name="test"):
    """
    функция сохранения данных карты мира
    massive_block - массив для блоков
    world_name - название мира который нужно сохранять
    """
    data = []
    for block in massive_block:
        data.append([str(type(block)), block.x0, block.y0])
    file = pathlib.Path(pathlib.Path.cwd(), "saves", world_name+".json")
    with open(file, 'w') as f:
        json.dump(data, f)


def load_map(massive_block: list, world_name="test"):
    """
    функция загрузки данных карты мира
    massive_block - массив для блоков
    world_name - название мира который нужно загружать
    """
    file = pathlib.Path(pathlib.Path.cwd(), "saves", world_name+".json")
