from shapely.geometry import Point,Polygon,shape
import json




with open('SF_Find_Neighborhoods.geojson') as f:
    js = json.load(f)


# point= Point(-122.457133,37.737350) # in sherwood
# point=Point(-122.462396,37.733606) # not in montery heights
# point=Point(-122.462396,37.733606)
point=Point(-122.49024,37.761847)#outer sunset

for feature in js['features']:
    polygon = shape(feature['geometry'])
    if polygon.contains(point):
        print('found in polygon',feature['properties']['name'])



