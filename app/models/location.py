from app.utils.db import db

class Location(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    climate = db.Column(db.String(255), nullable=False)
    terrain = db.Column(db.String(255), nullable=False)
    #image =
    id_movie = db.Column(db.Integer, db.ForeignKey('movie.id'),nullable=False)
    movie = db.relationship("Movie", back_populates="locations")

    def __init__(self, name, climate, terrain, movie):
        self.name = name
        self.climate = climate
        self.terrain = terrain
        self.id_movie = movie