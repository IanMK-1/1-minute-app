from flask import render_template
from . import auth
from flask import render_template, redirect, url_for
from ..models import User
from .auth_form import UserRegistration
from .. import db


@auth.route('/login')
def login():
    return render_template('auth/login.html')


@auth.route('/signUp', methods=["GET", "POST"])
def signUp():
    form = UserRegistration()
    if form.validate_on_submit():
        user = User(email=form.email.data, username=form.username.data, password=form.user_password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('user_auth.login'))
    return render_template('user_auth/signup.html', signup_form=form)
