from flask import Blueprint, jsonify
from app.models.location import Location

api_locations = Blueprint('api_locations',__name__)

path = '/api/locations'

@api_locations.route(path)
def index():
    locations = Location.query.all()
    locations_list = [location.to_dict() for location in locations]
    return jsonify(locations_list)