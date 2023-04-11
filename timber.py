from zipfile import ZipFile
import json
import numpy as np

## Read a timber map
## @param fname the name of the file to read
def readTimberMap(fname):
    # read internal zip file and return world.json
    with ZipFile(fname, 'r') as zipObj:
        zipObj.extract('world.json')
        with open('world.json', 'r') as f:
            return json.load(f)

## Make a heightmap from a timber map
## @param timberMap the timber map
def makeHeightmap(timberMap):
    size = timberMap['Singletons']['MapSize']['Size']
    x, y = size['X'], size['Y']
    arr = timberMap['Singletons']['TerrainMap']['Heights']['Array'].split(' ')
    return np.array(arr).astype(int).reshape(x, y)

## Write a timber map
## @param fname the name of the file to write
## @param timberMap the timber map
def writeTimberMap(fname, timberMap):
    # TODO: implement
    pass


