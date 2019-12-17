from lib.sql.database import database as db


class PostLikes(db.Model):
    __tablename__ = 'post_likes'

    id = db.Column(db.Integer, db.ForeignKey('posts.id'))
    likes = db.Column(db.Integer, nullable=False, default=0)
    platforms = db.Column(db.Integer, nullable=False, default=1)

    def __repr__(self):
        return '<Post {} with {} likes and {} platforms'.format(self.id, self.likes, self.platforms)
