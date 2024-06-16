from app.app import app
from app.utils.db import db
import config

with app.app_context():
    from app.models.movie import Movie
    from app.models.location import Location

    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)