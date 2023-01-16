from flask import Flask, render_template, redirect
from models import db, connect_db

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
  return render_template("home.html")

@app.route("/users/new")
def add_user_form():
  return render_template("add_user.html")

@app.route("/users/new", methods=["POST"])
def adding_user():
  return redirect("/users/24")

@app.route("/users/<int:user_id>")
def user_details(user_id):
  return render_template("user.html", user_id=user_id)

@app.route("/users/<int:user_id>/edit")
def edit_user_form(user_id):
  return render_template("add_user.html", user_id=user_id)

@app.route("/users/<int:user_id>/edit",methods=["POST"])
def edit_user(user_id):
  return redirect("/users/24")

@app.route("/users/<int:user_id>/delete",methods=["POST"])
def delte_user(user_id):
  return redirect("/users")
