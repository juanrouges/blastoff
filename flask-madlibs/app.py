from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from stories import Story

app = Flask(__name__)
app.config['SECRET_KEY'] = "this-are-the-irulis"

debug = DebugToolbarExtension(app)

@app.route('/')
def renderHome():
  return render_template('index.html')

@app.route('/story')
def renderStory():
  words = [request.args['place'], request.args['noun'], request.args['verb'], request.args['adjective'], request.args['plural_noun']]
  text = """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
  story = Story(words, text)
  return render_template('story.html', story=story.generate())