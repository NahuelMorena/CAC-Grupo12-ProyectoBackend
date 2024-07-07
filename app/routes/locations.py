from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models.location import Location
from app.models.movie import Movie
from app.utils.db import db
from flask_login import login_required
from app.utils.validator import validate_form

locations = Blueprint('locations', __name__)

path = '/location'
required_fields = ['name', 'climate', 'terrain', 'image', 'id_movie']

@locations.route(path)
@login_required
def index():
    locations = Location.query.all()
    movies = Movie.query.all()
    return render_template('locations/location.html', locations = locations, movies = movies)

@locations.route(path+'/new', methods=['POST'])
@login_required
def new():
    if not validate_form(request.form,required_fields):
        flash("Error! Todos los campos deben estar completos.", "error")
        return redirect(url_for('locations.index'))
    
    name = request.form['name']
    climate = request.form['climate']
    terrain = request.form['terrain']
    image = request.form['image']
    id_movie = request.form['id_movie']

    location = Location(name,climate,terrain,image,id_movie)

    db.session.add(location)
    db.session.commit()

    flash("Localización creada satisfactoriamente!!", "success")

    return redirect(url_for('locations.index'))

@locations.route(path+'/update/<id>', methods=['POST', 'GET'])
@login_required
def update(id):
    location = Location.query.get(id)
    if request.method == 'POST':
        if not validate_form(request.form, required_fields):
            flash("Error! Todos los campos deben estar completos.", "error")
        else:
            location.name = request.form['name']
            location.climate = request.form['climate']
            location.terrain = request.form['terrain']
            location.image = request.form['image']
            location.id_movie = request.form['id_movie']

            db.session.commit()
            flash("Localización actualizada satisfactoriamente!!", "success")
            return redirect(url_for('locations.index'))
    
    movies = Movie.query.all()
    return render_template('locations/update.html', location = location, movies = movies)

@locations.route(path+'/delete/<id>')
@login_required
def delete(id):
    location = Location.query.get(id)
    db.session.delete(location)
    db.session.commit()

    flash("Localización borrada satisfactoriamente!!", "success")

    return redirect(url_for('locations.index'))