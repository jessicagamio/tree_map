from flask_sqlalchemy import SQLAlchemy 

db =SQLAlchemy()

def connect_to_db(app,dbname):
    """connect to database"""
    
    app.config['SQLALCHEMY_DATABASE_URI']=f"postgres:///{dbname}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False 
    app.config['SQLALCHEMY_ECHO'] = True

    # connnect database to app in server
    db.app = app
    db.init_app(app)




# user clicks on district
    # get all tree types existing in district
    # can calculate from db how many trees of each type exist within the district for D3 bubble size

# clicks on tree types 
    # get all districts where tree grows
    # shows how many trees of those types on record
    # display map with trees in districts
    ## trees=db.session.query(TreeSpecies).join(Locations).join(Districts).filter(Districts.district_name=='Nob Hill').all()

class TreeSpecies(db.Model):
    """SF Trees"""

    __tablename__="tree_species"

    tree_species_id = db.Column(db.Integer,
                        primary_key=True,
                        autoincrement = True)
    sci_name = db.Column(db.String, nullable = False)
    common_name = db.Column(db.String, nullable = False)

    locations=db.relationship('Locations')


class Locations(db.Model):
    """Locations of Trees"""

    __tablename__="location"

    locate_id= db.Column(db.Integer,
                            primary_key=True,
                            autoincrement=True)
    district_id = db.Column(db.Integer,
                            db.ForeignKey('districts.district_id'))
    tree_species_id = db.Column(db.Integer,
                            db.ForeignKey('tree_species.tree_species_id'))
    lat = db.Column(db.Float, nullable=False)
    lon = db.Column(db.Float, nullable=False)

    tree_species=db.relationship('TreeSpecies')
    districts=db.relationship('Districts')


class Districts(db.Model):
    """SF districts"""

    __tablename__="districts"

    district_id = db.Column(db.Integer,
                    primary_key=True,
                    autoincrement=True)
    district_name=db.Column(db.String,nullable=False)
    # coord = db.Column(db.ARRAY(db.Float(precision=None,asdecimal=True), dimensions=1), nullable=False)
    coord = db.Column(db.ARRAY(db.Float(precision=None,asdecimal=True), dimensions=2), nullable=False)
    tree_species=db.relationship('TreeSpecies', secondary = "location", backref='districts')


# magnolia = TreeSpecies(sci_name='magnolia grandiflora', common_name='Magnolia')
# magdistrict=Districts(district_name='Nob Hill', coord=[1.2,1.4,1.4,1.5])
# magnolia_loc = Locations(lat=1.2, lon= 1.5, tree_species=magnolia, districts=magdistrict)

if __name__=="__main__":
    from server import app
    connect_to_db(app, 'map')
    db.create_all()

    # db.session.add(magnolia)
    # db.session.add(magdistrict)
    # db.session.add(magnolia_loc)
    # db.session.commit()

