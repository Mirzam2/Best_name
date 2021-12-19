import json
import pathlib
from os import write
from pathlib import Path

from block import *
from not_constant import person_images, types_block


def save_map(massive_block: list, world_name: str = "test"):
    """
    function for storing world map data
    massive_block - an array for blocks
    world_name - the name of the world that you want to save
    """
    file = pathlib.Path(pathlib.Path.cwd(), "saves", world_name)
    with open(file, 'w') as input_file:
        main_string = "[" + "\n"
        for word in massive_block:
            string = ""
            for i in word:
                string += (str(i) + ", ")
            string = string[:len(string) - 2]
            main_string += ("[" + string + "]," + "\n")
        main_string = main_string[:len(main_string) - 2]
        main_string += ("\n" + "]")
        input_file.write(main_string)


def load_map(world_name: str = "test"):
    """
    world map download function
    world_name - the name of the world that you want to download
    """
    file = pathlib.Path(pathlib.Path.cwd(), "saves", world_name)
    with open(file, 'r') as f:
        list_map = json.load(f)
    map_types = []
    for i in range(len(list_map)):
        map_types.append([])
        for j in range(len(list_map[i])):
            map_types[i].append(types_block.get(list_map[i][j], 0))
    return list_map, map_types
