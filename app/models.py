from . import db
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    __tablename__ = 'pitch_users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    user_right_id = db.Column(db.Integer, db.ForeignKey('rights.id'))
    user_password = db.Column(db.String(255))

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


class UserRights(db.Model):
    __tablename__ = 'rights'

    id = db.Column(db.Integer, primary_key=True)
    user_rights = db.Column(db.String(255))
    users_rights = db.relationship('User', backref='right', lazy="dynamic")

    # return a printable representation of the object
    def __repr__(self):
        return f'User {self.user_rights}'
