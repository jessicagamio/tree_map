from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from model import db, TreeSpecies, Locations, Districts, connect_to_db
from shapely.geometry import Point,Polygon,shape
from server import app
import json

if __name__ == "__main__":
    connect_to_db(app, "map")
    db.create_all()

def findDistrict(lat,lon):
    """returns district the point/tree belongs to"""
    # district = ''

    with open('resource/SF_Find_Neighborhoods.geojson') as f:
        js = json.load(f)

    point=Point(lon,lat)

    for feature in js['features']:
        polygon = shape(feature['geometry'])
        if polygon.contains(point):
            district = feature['properties']['name']

            return district

# Record all Neighborhoods in Districts db
data = "resource/SF_FIND_Neighborhoods.geojson"
districts = open(data).read()

districts_data = json.loads(districts)

district_dict={}

for i,district in enumerate(districts_data['features']):
    district_name = districts_data['features'][i]['properties']['name']
    coord = districts_data['features'][i]['geometry']['coordinates'][0][0]

    # Add districts to db
    tree_district=Districts(district_name= district_name, coord = coord)

    district_dict[tree_district.district_name] = tree_district

    db.session.add(tree_district)
    db.session.commit()


# Get street tree sci_name and common name from json file
tree_data = "resource/rows.json"
tree_data_json = open(tree_data).read()

street_trees = json.loads(tree_data_json)
entries = street_trees['data'].__len__()

print('*********number of entries*******', entries)

# iterated through all json file and record tree names and location coordinates
while (i<entries):
    tree_type =street_trees['data'][i][10]
    latitude = street_trees['data'][i][23]
    longitude = street_trees['data'][i][24]


    if latitude == None or longitude==None:
        pass

    
    elif tree_type == 'Tree(s) ::' or tree_type == None or tree_type == '':
        pass

    else:
        sci_name, common_name = tree_type.split('::')
        sci_name = sci_name.rstrip()
        common_name = common_name.lstrip()  
    
    # if latitude != None and longitude != None:
        # add Tree Specias to db
        tree_type = TreeSpecies(sci_name=sci_name, common_name=common_name)
        db.session.add(tree_type)

        # find district tree species is located in
        districtName = findDistrict(float(latitude), float(longitude))

        if districtName:
       
            print('------district info-------->',districtName)

            # fetch district from Districts class before passing to relationship
            districtIn = district_dict[districtName]

            print('----name----->',districtIn)

            # record tree Locations
            tree_loc = Locations(lat= float(latitude), lon= float(longitude), tree_species= tree_type, districts= districtIn)
            db.session.add(tree_loc)

            db.session.commit()

    i+=1



