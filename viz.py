from mayavi import mlab

### Vizualize surface map with mayavi
### NOTE: this can be hard to install. Try install PyQt5 first.
### Also, don't commit to `requirements.txt`

def viewMapMayavi(map, factor=40):
    mlab.surf(map)
    mlab.show()
