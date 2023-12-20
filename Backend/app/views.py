#!/usr/bin/env python3
""" Handles different routes for the app """

from app import app
from flask import render_template, flash, redirect, url_for, request, jsonify, make_response
from app.forms import RegistrationForm, LoginForm
from models.user import User


@app.route('/')
@app.route('/index')
def index():
    """ Return the home page """
    user = {'username': 'Remmy'}
    return render_template('index.html', title='Home', user=user)


@app.route('/register', methods=['GET', 'POST'])
def register():
    """ Registers a new user """
    if request.method == 'POST':
        data = request.get_json()

        username = data.get("username")
        email = data.get('email')
        password = data.get('password')

        if User.get_user_by_email(email):
            return jsonify({"message": f"User with email {email} already exists"})
        
        if User.create_user(email, username, password):
            return make_response(jsonify({"message": "User created successfuly"}), 201)
        
    return make_response(jsonify({"message": "Not a POST request"}), 201)


@app.route('/login', methods=['GET', 'POST'])
def login():
    """ Return the login page """
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'xhD2U@example.com' and form.password.data == 'password':
            flash('You\'re logged in!')
            return redirect(url_for('index'))
        else:
            flash('Login Unsuccessful. Incorrect username or password')
    return render_template('login.html', title='Login', form=form)
