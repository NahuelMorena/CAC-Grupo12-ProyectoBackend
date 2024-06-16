from flask import Blueprint, render_template

locations = Blueprint('locations', __name__)

@locations.route('/')
def hello():
    return render_template('index.html')
