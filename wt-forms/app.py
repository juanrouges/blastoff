from flask import Flask, render_template
from models import db, connect_db

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///blogly"
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config["SECRET_KEY"] = "unelefantesebalanseaba5687"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False
app.config["SQLALCHEMY_ECHO"] = False

connect_db(app)

@app.route("/")
def home_page():
  return render_template("/index.html")