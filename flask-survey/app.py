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

  return render_template("index.html", title=title, instructions=instructions)

@app.route("/questions/<int:id>")
def renderQuestion(id):
  questions = satisfaction_survey.questions[id]

  return render_template("question.html", questions=questions)

@app.route("/questions/choice")
def addChoice():
  return "Helo"

responses = []