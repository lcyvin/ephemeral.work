from datetime import datetime
from lib.sql.database import database as db


class Users(db.Model):
    '''
    id: uuid.uuid4()
    user_name: user-entered string
    display_name: user-entered string
    email: user-entered string
    join_daate: auto-filled date of user's signup
    '''
    id = db.Column(db.String(36), primary_key=True)
    user_name = db.Column(db.String(50), nullable=False)
    display_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(150), nullable=False)
    join_date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repre__(self):
        return '<User {} ({})>'.format(self.display_name, self.user_name)
