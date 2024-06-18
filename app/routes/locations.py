from flask import Blueprint, render_template, request, redirect, url_for
from app.models.location import Location
from app.models.movie import Movie
from app.utils.db import db

locations = Blueprint('locations', __name__)

path = '/location'

@locations.route(path)
def index():
    locations = Location.query.all()
    movies = Movie.query.all()
    return render_template('locations/location.html', locations = locations, movies = movies)

@locations.route(path+'/new', methods=['POST'])
def new():
    name = request.form['name']
    climate = request.form['climate']
    terrain = request.form['terrain']
    image = request.form['image']
    id_movie = request.form['id_movie']

    location = Location(name,climate,terrain,image,id_movie)

    db.session.add(location)
    db.session.commit()

    return redirect(url_for('locations.index'))

@locations.route(path+'/update/<id>', methods=['POST', 'GET'])
def update(id):
    location = Location.query.get(id)
    if request.method == 'POST':
        location.name = request.form['name']
        location.climate = request.form['climate']
        location.terrain = request.form['terrain']
        location.image = request.form['image']
        location.id_movie = request.form['id_movie']

        db.session.commit()
        return redirect(url_for('locations.index'))
    else:
        movies = Movie.query.all()
        return render_template('locations/update.html', location = location, movies = movies)

@locations.route(path+'/delete/<id>')
def delete(id):
    location = Location.query.get(id)
    db.session.delete(location)
    db.session.commit()

    return redirect(url_for(locations.index))