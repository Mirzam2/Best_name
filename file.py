import json
import pathlib
import mobs
from block import *
from not_constant import types_block, person_images


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


def save_units(list_mob: list, hero: mobs.Person,  world_name: str = "test"):
    """
    function for saving unit data
    list_mob - an array for mobs
    hero - main hero
    world_name - the name of the world that you want to save
    """
    file = pathlib.Path(pathlib.Path.cwd(), "saves_units", "units" + world_name)
    data = [[hero.x, hero.y, hero.life]]
    for i in list_mob:
        data.append([i.x, i.y, i.life])
    with open(file, 'w') as input_file:
        json.dump(data, input_file)


def load_units(screen: surface, world_name: str = "test"):
    """
    mobs data download function
    world_name - the name of the world that you want to download
    """
    file = pathlib.Path(pathlib.Path.cwd(), "saves_units", "units" + world_name)
    with open(file, 'r') as f:
        list_units = json.load(f)
    list_mobs = list()
    hero = mobs.Person(
        list_units[0][0], list_units[0][1], person_images, screen)
    hero.life = list_units[0][2]
    for i in range(1, len(list_units)):
        list_mobs.append(mobs.Zombie(
            list_units[i][0], list_units[i][1], person_images, screen))
        list_mobs[i-1].life = list_units[i][2]
    return hero, list_mobs
