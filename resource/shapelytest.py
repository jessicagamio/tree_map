from shapely.geometry import Point,Polygon,shape
import json




def findDistrict(lat,lon)
    """returns district the point belongs to"""

    with open('SF_Find_Neighborhoods.geojson') as f:
        js = json.load(f)

    point=Point(lon,lat)#outer sunset

    for feature in js['features']:
        polygon = shape(feature['geometry'])
        if polygon.contains(point):
            district = feature['properties']['name']

    return district



