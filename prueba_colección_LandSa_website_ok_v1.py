# prueba colección LandSat

import sys
import webbrowser
import folium
import ee

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
ultimoID=cuenteIds.getInfo()[nICFilter-1]
#randomID=random.choice(cuenteIds.getInfo())

print(primerID)
print(ultimoID)
#print(randomID)

primeraImage=ee.Image(IDcollection+'/'+primerID).select('B3','B2','B1')
ultimaImagen=ee.Image(IDcollection+'/'+ultimoID).select('B3','B2','B1')
#randomImage=ee.Image(IDcollection+'/'+randomID).select('B6','B5','B4')

feature_group=folium.FeatureGroup(name=primerID);
ee_plot(primeraImage).add_to(feature_group)

mymap.add_child(feature_group)

#mymap.add_child(folium.map.LayerControl())
mymap.add_child(folium.raster_layers.ImageOverlay(primeraImage.transpose(1, 2, 0), opacity=.7, bounds = bounds_fin))
mymap
mymap.save('lagocoya_v5.html')
webbrowser.open('lagocoya_v5.html')
