from app.utils.db import db
from werkzeug.security import check_password_hash
from flask_login import UserMixin

class User(db.Model, UserMixin):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    actived = db.Column(db.Boolean, default=False)

    def __init__(self, username, email, password, actived, id=None):
        self.username = username
        self.password = password
        self.email = email
        self.id = id
        self.actived = actived

    @classmethod
    def check_password(self, hashed_password, password):
        return check_password_hash(hashed_password,password)