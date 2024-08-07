from flask_sqlalchemy import SQLAlchemy
import json

db = SQLAlchemy()

def load_data():
    #Borra toda la info de la base de datos
    delete_actual_data()
    #Cargo automaticamente datos a la base de datos
    load_users()
    load_movies()
    load_locations()

def delete_actual_data():
    from app.models.movie import Movie
    from app.models.location import Location
    from app.models.user import User
    db.session.query(Location).delete()
    db.session.query(Movie).delete()
    db.session.query(User).delete()
    db.session.commit()

def load_users():
    from app.models.user import User
    with open('app/static/users.json', 'r') as f:
        data = json.load(f)

        for item in data:
            user = User(
                id = item['id'],
                username = item['username'],
                email = item['email'],
                actived = item['actived'],
                password = item['password']
            )
            db.session.add(user)
        db.session.commit()
        print("Usuarios cargados a la base de datos satisfactoriamente!!")

def load_movies():
    from app.models.movie import Movie
    from datetime import datetime
    with open('app/static/movies.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

        for item in data:
            premiere_str = item['premiere']
            movie = Movie(
                id = item['id'],
                title = item['title'],
                premiere = datetime.strptime(premiere_str, '%Y-%m-%d').date(),
                director = item['director'],
                description = item['description'],
                music = item['music'],
                writer = item['writer'],
                image = item['image']
            )
            db.session.add(movie)
        db.session.commit()
        print("Peliculas cargadas a la base de datos satisfactoriamente!!")

def load_locations():
    from app.models.location import Location
    with open('app/static/ubicaciones.json', 'r') as f:
        data = json.load(f)
        
        for item in data:
            location = Location(
                id = item['id'],
                name = item['name'],
                movie = item['movie'],
                climate = item['climate'],
                terrain = item['terrain'],
                image = item['image']
            )
            db.session.add(location)
        db.session.commit()
        print("Ubicaciones cargadas a la base de datos satisfactoriamente!!")
