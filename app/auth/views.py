from . import auth
from flask import render_template, redirect, url_for, request, flash
from ..models import User
from .auth_form import UserRegistration, UserLoginForm
from .. import db
from flask_login import login_user, logout_user, login_required
from ..email import mail_message


@auth.route('/signUp', methods=["GET", "POST"])
def signUp():
    form = UserRegistration()
    if form.validate_on_submit():
        user = User(email=form.email.data, username=form.username.data, password=form.user_password.data)
        db.session.add(user)
        db.session.commit()

        mail_message("Welcome to 1 minute pitch app", "email/welcome_user", user.email, user=user)

        return redirect(url_for('auth.user_login'))
    return render_template('user_auth/signup.html', signup_form=form)


@auth.route('/logIn', methods=['GET', 'POST'])
def user_login():
    login_form = UserLoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email=login_form.email.data).first()
        if user is not None and user.verify_password(login_form.user_password.data):
            login_user(user, login_form.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))

        flash('Invalid username or Password')

    title = "login"
    return render_template('user_auth/login.html', userlogin_form=login_form, title=title)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))
