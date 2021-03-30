import ee
from ee_plugin import Map

image = ee.Image('LANDSAT/LC08/C01/T1_TOA/LC08_044034_20140318');

#Define the visualization parameters.
vizParams = {
  'bands': ['B5', 'B4', 'B3'],
  'min': 0,
  'max': 0.5,
  'gamma': [0.95, 1.1, 1]
};

#Center the map and display the image.
Map.setCenter(-122.1899, 37.5010, 15); #San Francisco Bay Coordinate
# signées en degres par rapport à l'équateur et méridien de Greenwich d'où le négatif
Map.addLayer(image, vizParams, 'false color composite');

# code from https://www.geodose.com/2019/12/google-earth-engine-qgis-plugin-tutorial.html