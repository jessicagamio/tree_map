import json
from pprint import pprint

"""
All information in geojson file is under 'features' key
'properties' key under 'name' gives name of district
'geometry' key under 'coordinates' contains list of lon and lat coordinates

"""


data = "SF_FIND_Neighborhoods.geojson"
districts = open(data).read()

districts_data = json.loads(districts)


district_name = districts_data['features'][0]['properties']['name']
coord = districts_data['features'][0]['geometry']['coordinates'][0][0]


#allows you to view the districts of SF
for i,district in enumerate(districts_data['features']):
    pprint(districts_data['features'][i]['properties']['name'])
    pprint(districts_data['features'][0]['geometry']['coordinates'][0][0])
