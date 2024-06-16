from flask import Flask
from .routes.locations import locations
from .routes.movies import movies
#from flask_sqlalchemy import SQLAlchemy
from .utils.db import db
from config import DATABASE_CONNECTION_URI
def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_CONNECTION_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    #SQLAlchemy(app)
    db.init_app(app)
    
    ##Registro de rutas
    app.register_blueprint(locations)
    app.register_blueprint(movies)
    return app

app = create_app()

