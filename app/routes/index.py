from flask import Blueprint, render_template

home = Blueprint('home', __name__)

path = '/'

@home.route(path)
def index():
    return render_template('index.html')