from flask import Flask, render_template, flash, redirect
from models import db, connect_db
from forms import AddSnackForm

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///blogly"
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config["SECRET_KEY"] = "unelefantesebalanseaba5687"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = True
app.config["SQLALCHEMY_ECHO"] = False

connect_db(app)

@app.route("/")
def home_page():
  return render_template("/index.html")

@app.route("/add-snack", methods=["GET", "POST"])
def add_snack():
  form = AddSnackForm()

  if form.validate_on_submit():
    name = form.name.data
    price = form.price.data
    flash(f"Snack added name: {name}, price: ${price}")
    return redirect("/")
  else:
    return render_template("snack-form.html", form=form)