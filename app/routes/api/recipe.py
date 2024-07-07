from flask import Blueprint, jsonify, request
from app.models.recipe import Recipe
from app.utils.db import db

api_recipes = Blueprint('api_location', __name__)
path = '/api/recipes'

@api_recipes.route(path, methods=['GET'])
def get_Recipes():
    all_recipes = Recipe.query.all()
    recipes_list = [recipe.to_dict() for recipe in all_recipes]
    return jsonify(recipes_list)

@api_recipes.route(path+'/<id>', methods=['GET'])
def get_recipe(id):
    recipe = Recipe.query.get(id)
    return jsonify(recipe.to_dict()) 

@api_recipes.route(path+'/<id>', methods=['DELETE'])
def delete_recipe(id):
    recipe = Recipe.query.get(id)
    db.session.delete(recipe)
    db.session.commit()
    return jsonify(recipe.to_dict())

@api_recipes.route(path, methods=['POST'])
def create_recipe():
    nombre = request.json['nombre']
    pelicula = request.json['pelicula']
    imagen = request.json['imagen']
    ingredientes = request.json['ingredientes']
    instrucciones = request.json['instrucciones']
    descripcion = request.json['descripcion']

    new_recipe = Recipe(nombre,pelicula,imagen,ingredientes,instrucciones,descripcion)
    db.session.add(new_recipe)
    db.session.commit()
    return jsonify(new_recipe.to_dict())

@api_recipes.route(path+'/<id>', methods=['PUT'])
def update_recipe(id):
    recipe = Recipe.query.get(id)
    recipe.nombre = request.json['nombre']
    recipe.pelicula = request.json['pelicula']
    recipe.imagen = request.json['imagen']
    recipe.ingredientes = request.json['ingredientes']
    recipe.instrucciones = request.json['instrucciones']
    recipe.descripcion = request.json['descripcion']

    db.session.commit()
    return jsonify(recipe.to_dict())    
