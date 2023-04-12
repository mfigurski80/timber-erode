import numpy as np
from hydro_erosion.erodeLandscape import erodeMap


from timber import readTimberMap, makeHeightmap
from viz import viewMapMayavi

SCALE=1000

def main():
    # read the timber map
    timberMap = readTimberMap('map.timber')
    heightmap = makeHeightmap(timberMap)
    #  viewMapMayavi(heightmap)

    lim = heightmap - 1
    print(heightmap, lim)
    (res, _) = erodeMap(heightmap * SCALE, lim * SCALE, 1000000, 0.00001)
    viewMapMayavi(res/SCALE)
    print(res)


if __name__ == '__main__':
    main()
