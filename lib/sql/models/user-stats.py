from lib.sql.database import database as db


class UserStats(db.Model):
    __tablename__ = 'user-stats'

    user_id = db.Column(db.String(36), db.ForeignKey('users.id'))
    posts = db.Column(db.Integer, nullable=False, default=0)
    likes = db.Column(db.Integer, nullable=False, default=0)
    liked = db.Column(db.Integer, nullable=False, default=0)
    platforms = db.Column(db.Integer, nullable=False, default=0)
    platformed = db.Column(db.Integer, nullable=False, default=0)
