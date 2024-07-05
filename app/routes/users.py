from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models.user import User
from werkzeug.security import generate_password_hash
from app.utils.db import db

users = Blueprint('users', __name__)
path = "/users"

@users.route(path)
def index():
    users = User.query.all()
    return render_template('users/user.html', users = users)

@users.route(path+"/new", methods=['POST'])
def new():
    if not validate_user_form(request.form):
        flash("Error! Todos los campos deben estar completos.", "error")
        return redirect(url_for('users.index'))
    
    password = request.form['password']
    password2 = request.form['password2']

    if password != password2:
        flash("Error! Las contraseñas ingresadas no coinciden", "error")
        return redirect(url_for('users.index'))
    
    username = request.form['username']
    email = request.form['email']

    user = User(username, email, generate_password_hash(password), True)
    db.session.add(user)
    db.session.commit()

    flash("Usuario creada satisfactoriamente!!", "success")

    return redirect(url_for('users.index'))

@users.route(path+"/update/<id>", methods=['POST', 'GET'])
def update(id):
    user = User.query.get(id)
    if request.method == 'POST':
        if not validate_user_form(request.form):
            flash("Error! Todos los campos deben estar completos.", "error")
            return render_template('users/update.html', user = user)
        
        password = request.form['password']
        password2 = request.form['password2']
        if password != password2:
            flash("Error! Las contraseñas ingresadas no coinciden", "error")
            return render_template('users/update.html', user = user)

        user.username = request.form['username']
        user.email = request.form['email']
        user.password = generate_password_hash(password)

        db.session.commit()
        flash("Usuario actualizada satisfactoriamente!!", "success")

        return redirect(url_for('users.index'))

    return render_template('users/update.html', user = user)

@users.route(path+"/delete/<id>")
def delete(id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()

    flash("Usuario borrada satisfactoriamente!!", "success")

    return redirect(url_for('users.index'))

@users.route(path+"/activate/<id>")
def activate(id):
    user = User.query.get(id)
    user.actived = True
    db.session.commit()
    flash("Usuario habilitado satisfactoriamente!!", "success")

    return redirect(url_for('users.index'))

def validate_user_form(form):
    required_fields = ['username', 'email', 'password', 'password2']
    for field in required_fields:
        if not form.get(field):
            return False
    return True