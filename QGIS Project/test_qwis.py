import ee

image = ee.Image('USDA/NAIP/DOQQ/m_4609915_sw_14_1_20100629')
region = image.geometry()  # specify the roi 
scale = image.projection().nominalScale().multiply(10)  # specify the image resolution
description = image.get('system:index').getInfo()  # set the output image filename
print(scale) 
# Set configration parameters for output image
task_config = {
    'folder': 'gee-data', # output Google Drive folder
    'region': region,     # roi 
    'scale': scale,       # image resolution
    'crs': 'EPSG:4326',
    'maxPixels': 1.0E13,
    'fileFormat': 'GeoTIFF'
    }

# Export image to Google Drive
task = ee.batch.Export.image.toDrive(image, description, **task_config)
task.start()
print("Exporting {}".format(description))