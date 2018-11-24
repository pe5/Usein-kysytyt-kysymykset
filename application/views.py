from flask import render_template
from application import app
from application.tasks.models import Task

@app.route("/")
def index():
    return render_template("index.html", needs_answers=Task.find_questions_with_no_answers())
