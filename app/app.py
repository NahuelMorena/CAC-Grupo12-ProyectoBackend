from flask import Flask
from flask_login import LoginManager
from app.models.user import User
from .routes.locations import locations
from .routes.movies import movies
from .routes.index import home, status_401, status_404
from .routes.api.locations import api_locations
from flask_wtf.csrf import CSRFProtect

#from flask_sqlalchemy import SQLAlchemy
from .utils.db import db
from config import DATABASE_CONNECTION_URI
def create_app():
    app = Flask(__name__)

    app.secret_key = "secret key"
    csrf = CSRFProtect()
    csrf.init_app(app)

    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_CONNECTION_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    #SQLAlchemy(app)
    db.init_app(app)
    
    ##Registro de rutas
    app.register_blueprint(home)
    app.register_blueprint(locations)
    app.register_blueprint(movies)
    app.register_error_handler(401, status_401)
    app.register_error_handler(404, status_404)

    ##Rutas para la API
    app.register_blueprint(api_locations)

    ##Configuración de sesiones
    login_manager_app = LoginManager(app)
    @login_manager_app.user_loader
    def load_user(id):
        return User.query.get(id)
    
    return app


app = create_app()

