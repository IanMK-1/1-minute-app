from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime


class User(UserMixin, db.Model):
    __tablename__ = 'pitch_users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), index=True)
    email = db.Column(db.String(255), unique=True, index=True)
    user_right_id = db.Column(db.Integer, db.ForeignKey('rights.id'))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    user_password = db.Column(db.String(255))
    user_pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id'))

    # return a printable representation of the object
    def __repr__(self):
        return f'User{self.username}'

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.user_password = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.user_password, password)

    @login_manager.user_loader
    def load_user(pitch_user_id):
        return User.query.get(int(pitch_user_id))


class UserRights(db.Model):
    __tablename__ = 'rights'

    id = db.Column(db.Integer, primary_key=True)
    user_rights = db.Column(db.String(255))
    users_rights = db.relationship('User', backref='right', lazy="dynamic")

    # return a printable representation of the object
    def __repr__(self):
        return f'User {self.user_rights}'


class Pitch(db.Model):
    __tablename__ = 'pitches'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    pitch = db.Column(db.String())
    type = db.Column(db.String())
    posted = db.Column(db.DateTime, default=datetime.utcnow)
    upvote = db.Column(db.Integer)
    downvote = db.Column(db.Integer)
    user_pitches = db.relationship('User', backref='user_pitch', lazy='dynamic')

    def save_user_pitch(self):
        db.session.add(self)

    @classmethod
    def obtain_all_pitches(cls, type):
        all_pitches = Pitch.query.filter_by(type=type).all()
        return all_pitches

    @classmethod
    def obtain_user_pitch(cls, id):
        user_pitch = Pitch.query.filter_by(id=id).first()
        return user_pitch

    @classmethod
    def vote_pitch(cls, uname):
        user = User.query.filter_by(username=uname).first()
        pitch = Pitch.query.filter_by(id=user.id).all()

        vote_count = 0
        for user_pitch in pitch:
            vote_count += 1

        return vote_count
