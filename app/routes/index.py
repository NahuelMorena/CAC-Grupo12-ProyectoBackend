from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from app.models.user import User
from werkzeug.security import generate_password_hash
from app.utils.db import db
from app.utils.validator import validate_form

home = Blueprint('home', __name__)

path = '/'

@home.route(path)
@login_required
def index():
    return render_template('index.html')

@home.route(path+"/register", methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        required_fields = ['username', 'email', 'password', 'password2']
        if not validate_form(request.form, required_fields):
            flash("Error! Todos los campos deben estar completos.", "error")
            return redirect(url_for('home.register'))

        if request.form['password'] != request.form['password2']:
            flash("Error! Las contraseñas ingresadas no coinciden", "error")
            return redirect(url_for('home.register'))

        user = User(request.form['username'], request.form['email'], generate_password_hash(request.form['password']), False)
        db.session.add(user)
        db.session.commit()

        flash("Cuenta creada exitosamente! Espere a ser habilitado por el administrador!", "success")

        return redirect(url_for('home.login'))

    return render_template('auth/register.html')

@home.route(path+"/login", methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        required_fields = ['username', 'password']
        if not validate_form(request.form, required_fields):
            flash("Error! Todos los campos deben estar completos.", "error")
            return redirect(url_for('home.login'))
        
        user = User.query.filter_by(username=request.form['username']).first()
        if user and User.check_password(user.password,request.form['password']):
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