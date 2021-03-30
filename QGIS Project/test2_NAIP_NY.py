import ee
from ee_plugin import Map
import numpy as np
import matplotlib.pyplot as plt 

# Program : download GEE NAIP data in NY city in 2015
#           center and zoom the map to be printed on Manhattan
#            print the map on false colors

def get_ndvi(image):
    ndvi = image.normalizedDifference(['N', 'R']).rename('ndvi')
    return image.addBands([ndvi])
    
def masked_ndvi(image):
    NDVI = image.select(['ndvi'])
    #ee.Image(1) create a constant image of value 1 except for masked value equal that are equal to 0
    # ee.Filter.lte() Filter on metadata less than or equal to the given value and returns the constructed filter.
    return image.addBands(ee.Image(1).updateMask(NDVI.lte(0.2)).rename('NDVI_mask'))

image = ee.Image('USDA/NAIP/DOQQ/m_4007424_ne_18_1_20150729')
Map.setCenter(-74.040666504,40.667663996, 15)
Map.addLayer(image, {'bands': ['R','G','B']}, 'Visual')
Map.addLayer(image, {'bands': ['N','R','G']}, 'VNIR')

# calcul de la cartographie NDVI qui est ajoutée comme une carte hyperspectrale
# la carte NDVI ne permet pas de faire la différence entre la pelouse et les arbres 
# sera utilisée uniquement comme masque mais pas dans la segmentation, object detection a priori
image = get_ndvi(image)
ndvi_param = {'palette': ['008000', '00FF00'], 'bands':['ndvi']}
Map.addLayer(image,ndvi_param,'NDVI')

image = masked_ndvi(image)
Map.addLayer(image, {'bands':['NDVI_mask']}, 'NDVI_mask')
# bien que facilement identifiable à l'oeil nu avec les variations de couleurs 
# les espaces verts sont relativement mal détourés par l'indicateur NDVI 
# SAVI index could be used as well for urban areas


# to work : assemblage de clichés spatiaux

# Define an area of interest.
# statue of liberty 
# commencer dans le coin gauche haut puis tourner sens anti-horaire
aoi = ee.Geometry.Polygon(
  [[[-74.047706,40.691109],
    [-74.047706,40.688360],
    [-74.043276,40.688360],
    [-74.043276,40.691109]]], None, False)    

## Get 2-d pixel array for AOI - returns feature with 2-D pixel array as property per band.
#band_arrs = image.sampleRectangle(region=aoi)
#
## Get individual band arrays.
#band_arr_n = band_arrs.get('N')
#band_arr_r = band_arrs.get('R')
#band_arr_g = band_arrs.get('G')
#
## Transfer the arrays from server to client and cast as np array.
#np_arr_n = np.array(band_arr_n.getInfo())
#np_arr_r = np.array(band_arr_r.getInfo())
#np_arr_g = np.array(band_arr_g.getInfo())
#print(np_arr_n.shape)
#print(np_arr_r.shape)
#print(np_arr_g.shape)
#
## Expand the dimensions of the images so they can be concatenated into 3-D.
#np_arr_n = np.expand_dims(np_arr_n, 2)
#np_arr_r = np.expand_dims(np_arr_r, 2)
#np_arr_g = np.expand_dims(np_arr_g, 2)
#print(np_arr_n.shape)
#print(np_arr_r.shape)
#print(np_arr_g.shape)
#
## Stack the individual bands to make a 3-D array.
#CNIR_img = np.concatenate((np_arr_n, np_arr_r, np_arr_g), 2)
#print(CNIR_img.shape)
#
## Scale the data to [0, 255] to show as an RGB image.
##rgb_img_test = (255*((rgb_img - 100)/3500)).astype('uint8')
#plt.imshow(CNIR_img)
#plt.colorbar()
#plt.show()
#
##region = band_arrs.geometry()  # specify the roi 
##scale = band_arrs.projection().nominalScale().multiply(10)  # specify the image resolution ???
##description = band_arrs.get('system:index').getInfo()  # set the output image filename
### Set configration parameters for output image
##task_config = {
##    'folder': 'gee-data', # output Google Drive folder
##    'region': region,     # roi 
##    'scale': scale,       # image resolution
##    'crs': 'EPSG:3857',
##    'maxPixels': 1.0E13,
##    'fileFormat': 'GeoTIFF'
##    }
##    
##print('ok')
##    # Export image to Google Drive
##task = ee.batch.Export.image.toDrive(band_arrs, description, **task_config)
##task.start()
##print("Exporting {}".format(description))