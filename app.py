# Jon Compton
# Springboard May 26 Cohort

from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)

app.config['SECRET_KEY'] = "123456"
debug = DebugToolbarExtension(app)

@app.route('/')
def home_page():
    classes = story.prompts
    return render_template("home.html", classes=classes)

@app.route('/madlib')
def mad_lib():
    madlib = story.generate(request.args)
    return render_template("madlib.html", madlib=madlib)