from flask import Blueprint, render_template, request, redirect, url_for, jsonify, flash
from app.models.movie import Movie
from app.utils.db import db
from flask_login import login_required
from app.utils.validator import validate_form

movies = Blueprint('movies', __name__)

path = '/movies'
required_fields = ['title', 'premiere', 'director', 'description', 'music', 'writer', 'image']

@movies.route(path)
@login_required
def index():
    movies = Movie.query.all()
    return render_template('movies/movie.html', movies=movies)

@movies.route(path +'/new', methods=['POST'])
@login_required
def new():
    if not validate_form(request.form, required_fields):
        flash("Error! Todos los campos deben estar completos.", "error")
        return redirect(url_for('movies.index'))

    title = request.form['title']
    premiere = request.form['premiere']
    director = request.form['director']
    description = request.form['description']
    music = request.form['music']
    writer = request.form['writer']
    image = request.form['image']

    movie = Movie(title,premiere,director,description,music,writer,image)

    db.session.add(movie)
    db.session.commit()

    flash("Pelicula creada satisfactoriamente!", "success")

    return redirect(url_for('movies.index'))

@movies.route(path+'/update/<id>', methods=['POST', 'GET'])
@login_required
def update(id):
    movie = Movie.query.get(id)
    if request.method == 'POST':
        if not validate_form(request.form,required_fields):
            flash("Error! Todos los campos deben estar completos.", "error")
            return render_template('movies/update.html', movie = movie)
            #return redirect(url_for('movies.index'))
        
        movie.title = request.form['title']
        movie.premiere = request.form['premiere']
        movie.director = request.form['director']
        movie.description = request.form['description']
        movie.music = request.form['music']
        movie.writer = request.form['writer']

        db.session.commit()

        flash("Pelicula actualizada satisfactoriamente!", "success")

        return redirect(url_for('movies.index'))
     
    return render_template('movies/update.html', movie = movie)

@movies.route(path+'/delete/<id>')
@login_required
def delete(id):
    print(f"delete {id}")
    movie = Movie.query.get(id)

    if not movie:
        flash("Error! La pelicula a borrar no se encontro", "error")
        return redirect(url_for('movies.index'))
    if movie.locations:
        flash("Error! No se puede borrar esta pelicula por que cuenta con localidades en el sistema!", "error")
        return redirect(url_for('movies.index'))
    
    db.session.delete(movie)
    db.session.commit()

    flash("Pelicula borrada satisfactoriamente!", "success")

    return redirect(url_for('movies.index'))
