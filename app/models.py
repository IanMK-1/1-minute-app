from . import db


class User(db.Model):
    __tablename__ = 'pitch_users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    user_right_id = db.Column(db.Integer, db.ForeignKey('rights.id'))

    # return a printable representation of the object
    def __repr__(self):
        return f'User{self.username}'


class UserRights(db.Model):
    __tablename__ = 'rights'

    id = db.Column(db.Integer, primary_key=True)
    user_rights = db.Column(db.String(255))
    users_rights = db.relationship('User', backref='right', lazy="dynamic")

    # return a printable representation of the object
    def __repr__(self):
        return f'User {self.user_rights}'
