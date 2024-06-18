from app.utils.db import db
from app.models.movie import Movie

class Location(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    climate = db.Column(db.String(255), nullable=False)
    terrain = db.Column(db.String(255), nullable=False)
    image = db.Column(db.String(255), nullable=False)
    id_movie = db.Column(db.Integer, db.ForeignKey('movie.id'),nullable=False)
    movie = db.relationship("Movie", back_populates="locations")

    def __init__(self, name, climate, terrain, image, movie):
        self.name = name
        self.climate = climate
        self.terrain = terrain
        self.image = image
        self.id_movie = movie

    def to_dict(self):
        movie = Movie.query.get(self.id_movie)

        return {
            'id': self.id,
            'name': self.name,
            'climate': self.climate,
            'terrain': self.terrain,
            'image': self.image,
            'movie': movie.title
        }