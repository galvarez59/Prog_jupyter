# prueba chicago resuelto en python
import ee
import folium
import rasterio
from matplotlib import pyplot

ee.Initialize()

tif_file = '/Users/gabrielalvarez/Dropbox/pendrives/Tercera_region/Imagen_landsat_afta/SP27GTIF.TIFf'
src = rasterio.open(tif_file)
pyplot.imshow(src.read(1), cmap='pink')
pyplot.show = lambda : None  # prevents showing during doctests
pyplot.show()

mymap = folium.Map(
    location=[41, -84.108],
    zoom_start=8,
    tiles='OpenStreetMap')
mymap