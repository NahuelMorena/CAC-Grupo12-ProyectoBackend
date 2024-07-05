from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from app.models.user import User

home = Blueprint('home', __name__)

path = '/'

@home.route(path)
def index():
    return render_template('index.html')

@home.route(path+"/login", methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        #print(request.form['username'])
        #print(request.form['password'])
        #return None
        if not validate_movie_form(request.form):
            flash("Error! Todos los campos deben estar completos.", "error")
            return redirect(url_for('home.login'))
        
        user = User.query.filter_by(username=request.form['username']).first()
        if user:
            if User.check_password(user.password,request.form['password']):
                login_user(user)
                return render_template('index.html')
        
        flash("Error! Los datos ingresados no son validos", "error")

    return render_template('auth/login.html')

@home.route(path+"/logout")
def logout():
    logout_user()
    return redirect(url_for('home.login'))

@home.route(path+"/protected")
@login_required
def protected():
    return "<h1>Pantalla proteguida</h1>"

def status_401(error):
    return redirect(url_for('home.login'))

def status_404(error):
    return "<h1>La ruta ingresada no existe<h1>", 404

def validate_movie_form(form):
    required_fields = ['username', 'password']
    for field in required_fields:
        if not form.get(field):
            return False
    return True