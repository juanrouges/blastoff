from flask import Flask, render_template, redirect, request
from models import db, connect_db, User, Post

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///blogly"

app.config["SECRET_KEY"] = "chicharronesconcalzones123"
# ================== Whar are this for? =======================
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False
app.config["SQLALCHEMY_ECHO"] = True
# =============================================================

connect_db(app)

@app.route("/")
def home_page():
  return redirect("/users")

@app.route("/users")
def users_list():
  users = User.query.all()
  return render_template("home.html", users=users)

@app.route("/users/new")
def add_user_form():
  return render_template("user_form.html")

@app.route("/users/new", methods=["POST"])
def adding_user():

  first_name = request.form['first_name']
  last_name = request.form['last_name']
  image_url = request.form['image_url']

  new_user = User(first_name=first_name, last_name=last_name, image_url = image_url or None)

  db.session.add(new_user)
  db.session.commit()

  return redirect(f"/users/{new_user.id}")

@app.route("/users/<int:user_id>")
def user_details(user_id):
  user = User.query.get(user_id)
  user_posts = Post.query.filter(Post.user_id == user_id)
  print(user_posts)
  return render_template("user.html", user=user, posts=user_posts)

@app.route("/users/<int:user_id>/edit")
def edit_user_form(user_id):
  user = User.query.get(user_id)
  return render_template("user_form.html", user=user)

@app.route("/users/<int:user_id>/edit",methods=["POST"])
def edit_user(user_id):
  update_user = User.query.get(user_id)

  update_user.first_name = request.form['first_name']
  update_user.last_name = request.form['last_name']
  update_user.image_url = request.form['image_url']

  db.session.add(update_user)
  db.session.commit()

  return redirect("/users")

@app.route("/users/<int:user_id>/delete",methods=["POST"])
def delte_user(user_id):
  return redirect("/users")
