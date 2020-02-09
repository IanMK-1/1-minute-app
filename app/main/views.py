from flask import render_template, request, redirect, url_for, abort
from . import main
from flask_login import login_required, current_user
from ..models import User, Pitch
from .main_form import UpdateBio, UserPitchForm
from .. import db, photos


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/pitch/new-pitch')
@login_required
def new_pitch():
    user_pitch = UserPitchForm()
    if user_pitch.validate_on_submit():
        title = user_pitch.title.data
        pitch = user_pitch.pitch.data
        type = user_pitch.type.data

        new_user_pitch = Pitch(title=title, pitch=pitch, type=type, user=current_user, upvote=0, downvote=0)

        new_user_pitch.save_user_pitch()
        return redirect(url_for('.index'))
    return render_template('pitch.html', user_pitch=user_pitch)


@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username=uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user=user)


@main.route('/user/<uname>/update_bio', methods=['GET', 'POST'])
@login_required
def update_bio(uname):
    user = User.query.filter_by(username=uname).first()
    if user is None:
        abort(404)

    form = UpdateBio()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile', uname=user.username))

    return render_template('profile/update.html', form=form)


@main.route('/user/<uname>/update/pic', methods=['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username=uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile', uname=uname))


@main.route('/pitches/pick_up_lines_pitches')
def pickup_pitches():
    pitches = Pitch.obtain_all_pitches('pick up lines')

    return render_template("pick_up.html", pitches=pitches)


@main.route('/pitches/interview_pitches')
def interview_pitches():
    pitches = Pitch.obtain_all_pitches('interview')

    return render_template("interview.html", pitches=pitches)


@main.route('/pitches/product_pitches')
def product_pitches():
    pitches = Pitch.obtain_all_pitches('product')

    return render_template("product.html", pitches=pitches)


@main.route('/pitches/promotion_pitches')
def promotion_pitches():
    pitches = Pitch.obtain_all_pitches('promotion')

    return render_template("promotion.html", pitches=pitches)
