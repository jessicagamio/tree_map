from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_to_db(app,db_name):
    """Connects to database"""

    app.config['SQLALCHEMY_DATABASE_URI']=f'postgresql:///{db_name}'
    #shows SQL executed
    app.config['SQLALCHEMY_ECHO']= True
    app.config['SQLAlCHEMY_TRACK_MODIFICATIONS']= False
    db.app = app
    db_init_app(app)
    db.create_all()

    print('Connected to db!')





if __name__=="__main__":
    connect_to_db(app)