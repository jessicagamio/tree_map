from model import db, TreeSpecies, Locations, Districts, connect_to_db
from shapely.geometry import Point,Polygon,shape
import json



def findDistrict(lat,lon)
    """returns district the point/tree belongs to"""

    with open('/resource/SF_Find_Neighborhoods.geojson') as f:
        js = json.load(f)

    point=Point(lon,lat)#outer sunset

    for feature in js['features']:
        polygon = shape(feature['geometry'])
        if polygon.contains(point):
            district = feature['properties']['name']

    return district

# Record all Neighborhoods in Districts db
data = "/resource/SF_FIND_Neighborhoods.geojson"
districts = open(data).read()

districts_data = json.loads(districts)

for i,district in enumerate(districts_data['features']):
    district_name = districts_data['features'][i]['properties']['name']
    coord = districts_data['features'][i]['geometry']['coordinates'][0][0]

    # Add districts to db
    tree_district=Districts(district_name= district_name, coord = coord)


# Get street tree sci_name and common name from json file
tree_data = "/resource/rows.json"
tree_data_json = open(tree_data).read()

street_trees = json.loads(tree_data_json)
entries = street_trees['data'].__len__()

# iterated through all json file and record tree names and location coordinates
while (i<entries):
    tree_type =tree_info['data'][i][10]
    latitude = tree_info['data'][i][23]
    longitude = tree_info['data'][i][24]


    if latitude == None and longitude==None:
        pass
    
    elif tree_type == 'Tree(s) ::':
        pass

    else:
        sci_name, common_name = tree_type.split('::')
        sci_name = sci_name.rstrip()
        common_name = common_name.lstrip()  
    # add Tree Specias to db
    tree_type = TreeSpecies(sci_name=sci_name, common_name=common_name)
    # find district tree species is located in
    districtIn = findDistrict(latitude, longitude)
    # record tree Locations
    tree_loc = Locations(lat =latitude, lon = longitude, tree_species = tree_type, districts = districtIn)

    i+=1


