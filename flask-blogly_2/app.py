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

@app.route("/posts/<int:post_id>")
def display_post(post_id):
  post = Post.query.get(post_id)

  return render_template("post.html", post=post)

@app.route("/users/<int:user_id>/posts/new")
def add_new_post(user_id):
  user = User.query.get(user_id)

  return render_template("post_form.html", user=user)

@app.route("/users/<int:user_id>/posts/new", methods=["POST"])
def save_post(user_id):
  title = request.form['title']
  content = request.form['content']

  post = Post(title=title, content=content, user_id=user_id)

  db.session.add(post)
  db.session.commit()

  return redirect(f"/users/{user_id}")

@app.route("/posts/<int:post_id>/edit")
def edit_post(post_id):
  post = Post.query.get(post_id)

  return render_template("post_form.html", post=post)

@app.route("/posts/<int:post_id>/edit", methods=["POST"])
def process_edit_post(post_id):
  post = Post.query.get(post_id)

  post.title = request.form['title']
  post.content = request.form['content']

  db.session.add(post)
  db.session.commit()

  return redirect(f"/posts/{post_id}")

# Delete route needs to be completed
@app.route("/users/<int:user_id>/delete",methods=["POST"])
def delte_user(user_id):
  return redirect("/users")
