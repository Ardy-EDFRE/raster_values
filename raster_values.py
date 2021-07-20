from arcgis.gis import GIS
from decouple import config

url = config('url', default='')
username = config('username', default='')
password = config('password', default='')

# Connect to the GIS.
try:
    web_gis = GIS(url, username, password)
    print("Successfully connected to {0}".format(web_gis.properties.name))
except:
    print("Failed login")

# Search for the DEM imagery layer item by title
dem_user_search = input("What dem are you searching for? (Please use exact name) -- ")
item_dem_search = web_gis.content.search(f'title:{dem_user_search}', 'Imagery Layer')[0]
item_dem = item_dem_search.layers[0]

# Search for the Ventura County feature layer item by title
study_area_user_search = input("What is your study area? (ex: EDF Project Boundaries) ")
item_study_area = web_gis.content.search(f'title:{study_area_user_search}', 'Feature Layer')[0]
item_study_area

# Get a reference to the feature layer from the portal item
lyr_study_area = item_study_area.layers[0]
lyr_study_area

project_name = input("What is your project name? ")
# Query the study area layer to get the boundary feature
query_study_area = lyr_study_area.query(where=f"ProjectName = '{project_name}'")

layer_sr = query_study_area.spatial_reference
tmp_samples = []
for feature in query_study_area.features:
    feature.geometry['spatialReference'] = layer_sr
    tmp_samples.append(item_dem.get_samples(feature.geometry))

tmp_samples
