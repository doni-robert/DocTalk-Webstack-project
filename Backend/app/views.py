#!/usr/bin/env python3
""" Handles different routes for the app """

from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import RegistrationForm, LoginForm


@app.route('/')
@app.route('/index')
def index():
    """ Return the home page """
    user = {'username': 'Remmy'}
    return render_template('index.html', title='Home', user=user)


@app.route('/register', methods=['GET', 'POST'])
def register():
    """ Return the register page """
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!')
        return redirect(url_for('index'))
    return render_template('register.html', title='Register', form=form)


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
