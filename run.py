from app.app import app
from app.utils.db import db, load_data
import config
import argparse

#Comando de consola para cargar datos en la bd automaticamente
def load_data_command():
    with app.app_context():
        load_data()

parser = argparse.ArgumentParser(description='Script to run application tasks.')
parser.add_argument('command', choices=['load_data'], nargs='?', default=None, help='Command to execute')
args = parser.parse_args()

with app.app_context():
    from app.models.movie import Movie
    from app.models.location import Location

    db.create_all()

    if args.command == 'load_data':
        load_data_command()

if __name__ == "__main__":
    app.run(debug=True)