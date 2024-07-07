from app.utils.db import db

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    pelicula = db.Column(db.String(100), nullable=False)
    imagen = db.Column(db.String(400), nullable=False)
    ingredientes = db.Column(db.String(1000), nullable=False)
    instrucciones = db.Column(db.String(2000), nullable=False)
    descripcion = db.Column(db.String(1000), nullable=False)

    def __init__(self, nombre, pelicula, imagen, ingredientes, instrucciones, descripcion):
        self.nombre = nombre
        self.pelicula = pelicula
        self.imagen = imagen
        self.ingredientes = ingredientes
        self.instrucciones = instrucciones
        self.descripcion = descripcion

    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'pelicula': self.pelicula,
            'imagen': self.imagen,
            'ingredientes': self.ingredientes,
            'instrucciones': self.instrucciones,
            'descripcion': self.descripcion
        }