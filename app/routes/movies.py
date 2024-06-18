from flask import Blueprint, render_template, request, redirect, url_for
from app.models.movie import Movie
from app.utils.db import db

movies = Blueprint('movies', __name__)

path = '/movies'

@movies.route(path)
def index():
    movies = Movie.query.all()
    return render_template('movies/movie.html', movies=movies)

@movies.route(path +'/new', methods=['POST'])
def new():
    title = request.form['title']
    premiere = request.form['premiere']
    director = request.form['director']
    description = request.form['description']
    music = request.form['music']
    writer = request.form['writer']

    movie = Movie(title,premiere,director,description,music,writer)

    db.session.add(movie)
    db.session.commit()

    return redirect(url_for('movies.index'))

@movies.route(path+'/update/<id>', methods=['POST', 'GET'])
def update(id):
    print(f"update {id}")

    movie = Movie.query.get(id)
    if request.method == 'POST':
        movie.title = request.form['title']
        movie.premiere = request.form['premiere']
        movie.director = request.form['director']
        movie.description = request.form['description']
        movie.music = request.form['music']
        movie.writer = request.form['writer']

        db.session.commit()

        return redirect(url_for('movies.index'))
     
    return render_template('movies/update.html', movie = movie)

@movies.route(path+'/delete/<id>')
def delete(id):
    print(f"delete {id}")
    movie = Movie.query.get(id)
    db.session.delete(movie)
    db.session.commit()

    return redirect(url_for('movies.index'))



