from flask import Flask
from .routes.locations import locations
from .routes.movies import movies
from .routes.index import home
from .routes.api.locations import api_locations
#from flask_sqlalchemy import SQLAlchemy
from .utils.db import db
from config import DATABASE_CONNECTION_URI
def create_app():
    app = Flask(__name__)

    app.secret_key = "secret key"

    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_CONNECTION_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    #SQLAlchemy(app)
    db.init_app(app)
    
    ##Registro de rutas
    app.register_blueprint(home)
    app.register_blueprint(locations)
    app.register_blueprint(movies)

    ##Rutas para la API
    app.register_blueprint(api_locations)

    
    return app

app = create_app()

