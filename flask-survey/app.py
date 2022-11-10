from flask import Flask, render_template
from flask_debugtoolbar import DebugToolbarExtension

from surveys import satisfaction_survey

app = Flask(__name__)

app.config['SECRET_KEY'] = "this-are-the-irulis"

debug = DebugToolbarExtension(app)


@app.route("/")
def renderHome():
  title = satisfaction_survey.title
  instructions = satisfaction_survey.instructions
  questions = satisfaction_survey.questions

  return render_template("index.html", title=title, instructions=instructions, questions=questions)