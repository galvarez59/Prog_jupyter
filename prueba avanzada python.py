# prueba avanzada python
# prueba colección LandSat

import sys
import webbrowser
import folium
import ee
import json
import subprocess
import rasterio
from rasterio import features


from eeconvert import eeImageToFoliumLayer as ee_plot

#ee.Authenticate()

try:
    ee.Initialize()
    print('exitoso')
except ee.EEException as e: 
    print('faild')
except:
    print('error inexperado:', sys.exc_info()[0])
    raise
#coleccion = 'LANDSAT/LC08/T1_TOA'

mymap = folium.Map(
    location=[-11.005, -76.108],
    zoom_start=8,
    tiles='OpenStreetMap')
mymap
IC = ee.ImageCollection("LANDSAT/LE07/C01/T1_RT")

IDcollection='LANDSAT/LE07/C01/T1_RT'

nIC = IC.size().getInfo()
print(nIC)
cuenteIds = IC.reduceColumns(ee.Reducer.toList(), ['system:index']).get('list')
print(cuenteIds.getInfo())
ICFilter= IC.filterDate('2019-07-01','2019-08-01')

GPLCH=ee.Geometry.Point(-76.10, -11.005)

ICFilter=ICFilter.filterBounds(GPLCH)

nICFilter=ICFilter.size().getInfo()

if nICFilter==0:print("no hay imagenes")
else:
    print("cantidad "+str(nICFilter))
    cuenteIds = ICFilter.reduceColumns(ee.Reducer.toList(), ['system:index'])
    cuenteIds = cuenteIds.get('list')
    print(cuenteIds.getInfo())

primerID=cuenteIds.getInfo()[0]

with rasterio.drivers():
    with rasterio.open('LE07_007068_20190711') as src:
        blue = src.read_band(3)
        blue[blue < 255] = 0
mask = blue != 255

# Show the source image.
import matplotlib.pyplot as plt
import matplotlib.cm as cm
plt.imshow(blue, cmap=cm.Greys_r)