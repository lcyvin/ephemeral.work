from flask_sqlalchemy import SQLAlchemy
from webapp.app import app

database = SQLAlchemy(app)
