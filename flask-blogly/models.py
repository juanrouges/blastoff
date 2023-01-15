from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
  db.app = app
  db.init_app(app)

class User(db.Model):
  __tablename__ = "users"

  id = db.column(db.Integer, primary_key=True, autoincrement=True)
  first_name = db.column(db.String(20), nullable=False)
  last_name = db.column(db.String(20), nullable=False)
  image_url = db.column(db.String(100), default="https://placehold.co/600x400")