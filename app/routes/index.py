from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from app.models.user import User
from werkzeug.security import generate_password_hash
from app.utils.db import db

home = Blueprint('home', __name__)

path = '/'

@home.route(path)
@login_required
def index():
    return render_template('index.html')

@home.route(path+"/register", methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        if not validate_user2_form(request.form):
            flash("Error! Todos los campos deben estar completos.", "error")
            return redirect(url_for('home.register'))
        
        password = request.form['password']
        password2 = request.form['password2']

        if password != password2:
            flash("Error! Las contraseñas ingresadas no coinciden", "error")
            return redirect(url_for('home.register'))
        
        username = request.form['username']
        email = request.form['email']

        user = User(username, email, generate_password_hash(password), False)
        db.session.add(user)
        db.session.commit()

        flash("Cuenta creada exitosamente! Espere a ser habilitado por el administrador!", "success")

        return redirect(url_for('home.login'))

    return render_template('auth/register.html')

@home.route(path+"/login", methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        #print(request.form['username'])
        #print(request.form['password'])
        #return None
        if not validate_user_form(request.form):
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
@login_required
def logout():
    logout_user()
    return redirect(url_for('home.login'))

def status_401(error):
    return redirect(url_for('home.login'))

def status_404(error):
    return "<h1>La ruta ingresada no existe<h1>", 404

def validate_user_form(form):
    required_fields = ['username', 'password']
    for field in required_fields:
        if not form.get(field):
            return False
    return True

def validate_user2_form(form):
    required_fields = ['username', 'email', 'password', 'password2']
    for field in required_fields:
        if not form.get(field):
            return False
    return True