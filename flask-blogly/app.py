from flask import Flask, render_template
from models import db, connect_db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'

app.config['SECRET_KEY'] = 'chicharronesconcalzones123'
# ================== Whar are this for? =======================
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SQLALCHEMY_ECHO'] = True
# =============================================================

connect_db(app)

@app.route('/')
def home_page():
  return render_template('root.html')
