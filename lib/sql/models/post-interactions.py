from lib.sql.database import database as db


class PostInteractions(db):
    __tablename__ = 'post_interactions'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.String(36), db.ForeignKey('users.id'))
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))
    action = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Post interaction on {} by {}>'.format(self.post_id, self.user_id)
