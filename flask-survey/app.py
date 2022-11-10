from flask import Flask, render_template
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.config['SECRET_KEY'] = "this-are-the-irulis"

debug = DebugToolbarExtension(app)


@app.route("/")
def renderHome():
  return render_template("index.html")