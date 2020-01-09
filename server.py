from flask import Flask, request, render_template
import json

app = Flask(__name__)
app.secret_key="Secret"




@app.route('/')
def index():
    """Homepage"""

    # Parse out districts from json file
    with open('resource/SF_Find_Neighborhoods.geojson') as f:
        districts_data = json.load(f)

    neighborhoods = []

    for i,district in enumerate(districts_data['features']):
        neighborhoods.append(districts_data['features'][i]['properties']['name'])


    # Parse out Tree Species

    with open('resource/rows.json') as t:
        trees = json.load(t)

    lines = trees['data'].__len__()
    tree_list = []

    i=0

    while (i<lines):
        tree_type =trees['data'][i][10]
        latitude = trees['data'][i][23]
        longitude = trees['data'][i][24]

        # split out the scientific and common name from data
        scientific_name, common_name = tree_type.split('::')
        sci_name = scientific_name.rstrip()
        common_name = common_name.lstrip()     

        if latitude == None and longitude==None:
            pass
        
        elif tree_type == 'Tree(s) ::':
            pass

        elif sci_name not in tree_list:
            tree_list.append(sci_name)
        
        i+=1

    return render_template('index.html', neighborhoods = neighborhoods, treespecies=tree_list)
    

@app.route("/result")
def statistics():
    """ query tree stats to display on page"""

    region = request.args.get("Districts")
    tree = request.args.get("TreeSpecies")

    if region == "All Districts":

    if tree == "All Types":


    else:
        #Query in database
        # for Districts in region query number of trees of specified treespecies
        # return answer in the form of a list of tuples (district/tree, number)
    return answer




if __name__ == "__main__":
    app.run(debug = True, host = '0.0.0.0')

