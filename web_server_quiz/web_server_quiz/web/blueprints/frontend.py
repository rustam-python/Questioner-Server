import hashlib
import json

from flask import render_template, flash, redirect, url_for, request, Blueprint, escape
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.urls import url_parse

from models import User, Sessions
import web.forms as forms

frontend = Blueprint('frontend', __name__)


@frontend.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = forms.LoginForm(request.form)
    if form.validate():
        user = User.get(User.username == form.username.data)
        if user is None or user.password_hash != hashlib.sha256(form.password.data.encode('UTF-8')).hexdigest():
            flash('Invalid username or password')
            return redirect(url_for('frontend.login'))
        login_user(user)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('frontend.index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@frontend.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('frontend.index'))


@frontend.route('/', methods=['GET', 'POST'])
@frontend.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    form = forms.IndexForm(request.form)
    return render_template('index.html', title='Server', form=form)


@frontend.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('frontend.index'))
    form = forms.RegistrationForm(request.form)
    if form.validate():
        try:
            User.add(username=form.username.data,
                     email=form.email.data,
                     password=form.password.data,
                     gender=form.gender.data,
                     age=form.age.data,
                     religion=form.religion.data)
            flash('Congratulations, you are now a registered user!')
            return redirect(url_for('frontend.login'))
        except Exception as err:
            flash(str(err), 'danger')
            return redirect(url_for('frontend.register'))
    return render_template('registration.html', title='Register', form=form)


@frontend.route('/quiz_creation', methods=['GET', 'POST'])
@login_required
def quiz_creation():
    return render_template('quiz_creation.html', title='Quiz creation')


@frontend.route('/logged_user', methods=['GET', 'POST'])
def logged_user():
    pass


@frontend.route('/quiz/<quiz_id>', methods=['GET', 'POST'])
@login_required
def quiz(quiz_id: int):
    return render_template('quiz.html', title='Quiz')
