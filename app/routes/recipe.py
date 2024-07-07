from flask import Blueprint, send_from_directory


recipes = Blueprint('recipes', __name__)

path = '/recipes'

@recipes.route(path)
def index():
    return send_from_directory('templates/recipes', 'recipe2.html')

@recipes.route(path+'/receta_nueva.html')
def new():
    return send_from_directory('templates/recipes', 'receta_nueva.html')

@recipes.route(path+"/recipe_detail.html")
def detail():
    return send_from_directory('templates/recipes', 'recipe_detail.html')

@recipes.route(path+"/recipe_update.html")
def update():
    return send_from_directory('templates/recipes', 'recipe_update.html')
