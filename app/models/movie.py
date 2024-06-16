from app.utils.db import db

class Movie(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    premiere = db.Column(db.Date, nullable=False)
    director = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    music = db.Column(db.String(255), nullable=False)
    writer = db.Column(db.String(255), nullable=False)
    # image =
    locations = db.relationship("Location",back_populates="movie")

    def __init__(self, title, premiere, director, description, music, writer):
        self.title = title
        self.premiere = premiere
        self.director = director
        self.description = description
        self.music = music
        self.writer = writer
        self.locations = []
        ##