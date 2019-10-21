from flask_sqlalchemy import SQLAlchemy 

def connect_to_db(app,dbname='tree_map'):
    """connect to database"""
    db.config['SQLALCHEMY_DATABASE_URI']=f'postgres:///{dbname}'
    db.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False 
    db.config['SQLALCHEMY_ECHO'] = True

    db.app = app
    db.init_app(app)
    db.connect_all()







if __name__=="__main__":
    from server import app
    connect_to_db(app)