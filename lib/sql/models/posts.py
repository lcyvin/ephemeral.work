from datetime import datetime
from lib.sql.database import database as db


class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    text = db.Column(db.String(500), nullable=False)
    created_date = db.Column(db.Datetime, default=datetime.utcnow)
    origin = db.Column(db.Integer, default=id)
    author = db.Column(db.String(36), db.ForeignKey('users.id'), nullable=False)
    poster = db.Column(db.String(36), db.ForeignKey('users.id'), nullable=False)

    def __repr__(self):
        return '<Post by {} hosted by {}>'.format(self.author, self.poster)
