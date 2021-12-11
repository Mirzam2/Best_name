from perlin_noise import PerlinNoise
from random import randint
def create_field(map):
    noise = PerlinNoise(octaves=10, seed=randint(1,1000) )
    xpix = 21
    ypix = 21
    map = [[noise([i/xpix, j/ypix]) for j in range(xpix)] for i in range(ypix)]
    for i in range(ypix):
        for j in range(xpix):
            if map[i][j] >= 0:
                map[i][j] = 1
            else:
                map[i][j] = 0
    return map
if __name__ == "__main__":
    massive_map = []
    massive_map = create_field(massive_map)
    print(massive_map)
