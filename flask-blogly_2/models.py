from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

def connect_db(app):
  db.app = app
  db.init_app(app)

class User(db.Model):
  __tablename__ = "users"

  def __repr__(self):
    return f"<User id={self.id} first_name={self.first_name} last_name={self.last_name} image_url={self.image_url}>"

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  first_name = db.Column(db.String(20), nullable=False)
  last_name = db.Column(db.String(20), nullable=False)
  image_url = db.Column(db.String(100), default="https://placehold.co/600x400")

  def get_full_name(self):
    full_name = f"{self.first_name} {self.last_name}"
    return full_name

class Post(db.Model):
  __tablename__ = "posts"

  def __repr__(self):
    return f"<Post id={self.id} title={self.title} user_id={self.user_id} >"
  
  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  title = db.Column(db.Text, nullable=False)
  content = db.Column(db.Text, nullable=False)
  created_at = db.Column(db.DateTime, default=datetime.datetime.now())
  user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

  usr = db.relationship("User", backref="posts")
