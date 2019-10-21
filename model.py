from flask_sqlalchemy import SQLAlchemy 

def connect_to_db(app,dbname='tree_map'):
    """connect to database"""
    
    db.config['SQLALCHEMY_DATABASE_URI']=f'postgres:///{dbname}'
    db.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False 
    db.config['SQLALCHEMY_ECHO'] = True

    # connnect database to app in server
    db.app = app
    db.init_app(app)
    db.connect_all()



# user clicks on district
    # get all tree types existing in district
    # can calculate from db how many trees of each type exist

# clicks on tree types 
    # get all districts where tree grows
    # shows how many trees of those types on record
    # display map with trees in districts

class TreeSpecies(db.Model):
    """SF Trees"""

    __tablename__="tree_species"

    tree_species_id = db.Column(db.Integer,
                        primary_key=True,
                        autoincremint = True)
    sci_name = db.Column(db.String, nullable = False)
    common_name = db.Column(db.String, nullable = False)


class Locations(db.Model):
    """Locations of Trees"""

    __tablename__="location"

    locate_id= db.Column(db.Integer,
                            primary_key=True,
                            autoincriment=True)
    district_id = db.Column(db.Integer,
                            db.ForeignKey('district.district_id'))
    tree_species_id = db.Column(db.Integer,
                            db.ForeignKey('tree_species.tree_species_id'))
    lat = db.Column(db.Float, nullable=False)
    lon = db.Column(db.Float, nullable=False)

    tree_point=db.relationship('TreeSpecies', backref='tree_species')

class Districts(db.Model):
    """SF districts"""

    __tablename__="district"

    district_id = db.Column(db.Integer,
                    primary_key=True,
                    autoincriment=True)
    district_name=db.Column(db.String,nullable=False)
    coord = db.Column(db.Float, nullable=False)

    

if __name__=="__main__":
    from server import app
    connect_to_db(app)