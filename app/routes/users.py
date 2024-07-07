from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models.user import User
from werkzeug.security import generate_password_hash
from app.utils.db import db
from flask_login import login_required
from app.utils.validator import validate_form

users = Blueprint('users', __name__)
path = "/users"
required_fields = ['username', 'email', 'password', 'password2']

@users.route(path)
@login_required
def index():
    users = User.query.all()
    return render_template('users/user.html', users = users)

@users.route(path+"/new", methods=['POST'])
@login_required
def new():
    if not validate_form(request.form, required_fields):
        flash("Error! Todos los campos deben estar completos.", "error")
        return redirect(url_for('users.index'))
    
    if request.form['password'] != request.form['password2']:
        flash("Error! Las contraseñas ingresadas no coinciden", "error")
        return redirect(url_for('users.index'))
    
    user = User(request.form['username'], request.form['email'], generate_password_hash(request.form['password']), True)
    db.session.add(user)
    db.session.commit()
    flash("Usuario creada satisfactoriamente!!", "success")

    return redirect(url_for('users.index'))

@users.route(path+"/update/<id>", methods=['POST', 'GET'])
@login_required
def update(id):
    user = User.query.get(id)
    if request.method == 'POST':
        if not validate_form(request.form, required_fields):
            flash("Error! Todos los campos deben estar completos.", "error")
            return render_template('users/update.html', user = user)
        
        if request.form['password'] != request.form['password2']:
            flash("Error! Las contraseñas ingresadas no coinciden", "error")
            return render_template('users/update.html', user = user)

        user.username = request.form['username']
        user.email = request.form['email']
        user.password = generate_password_hash(request.form['password'])

        db.session.commit()
        flash("Usuario actualizada satisfactoriamente!!", "success")

        return redirect(url_for('users.index'))

    return render_template('users/update.html', user = user)

@users.route(path+"/delete/<id>")
@login_required
def delete(id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()
    flash("Usuario borrada satisfactoriamente!!", "success")

    return redirect(url_for('users.index'))

@users.route(path+"/activate/<id>")
@login_required
def activate(id):
    user = User.query.get(id)
    user.actived = True
    db.session.commit()
    flash("Usuario habilitado satisfactoriamente!!", "success")

    return redirect(url_for('users.index'))