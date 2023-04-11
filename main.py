from timber import readTimberMap, makeHeightmap
from viz import viewMapMayavi

def main():
    # read the timber map
    timberMap = readTimberMap('map.timber')
    heightmap = makeHeightmap(timberMap)
    print(heightmap)
    viewMapMayavi(heightmap)


if __name__ == '__main__':
    main()
