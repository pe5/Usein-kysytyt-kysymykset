from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

from application import app, db
from application.subjects.models import Subject
from application.subjects.forms import SubjectForm

@app.route("/subjects", methods=["GET"])
def subjects_index():
    return render_template("subjects/list.html", subjects = Subject.query.all())


