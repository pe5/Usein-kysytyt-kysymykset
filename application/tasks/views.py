from application import app, db
from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user
from application.tasks.models import Task
from application.tasks.forms import TaskForm
from application.subjects.models import Subject

@app.route("/tasks", methods=["GET"])
def tasks_index():
    return render_template("tasks/list.html", tasks = Task.query.all())

@app.route("/tasks/new/")
@login_required
def tasks_form():
    return render_template("tasks/new.html", form = TaskForm())

@app.route("/tasks/paivita", methods=["POST"])
@login_required
def tasks_set_done():
    uusi = request.form.get("uusi")
    vanha = request.form.get("vanha")
    task = Task.query.filter_by(done=vanha).first()
    task.done = uusi
    db.session().commit()
  
    return redirect(url_for("tasks_index"))

@app.route("/tasks/", methods=["POST"])
@login_required
def tasks_create():
    form = TaskForm(request.form)

    if not form.validate():
        return render_template("tasks/new.html", form = form)

    t = Task(form.name.data)
    t.done = form.answer.data
    t.account_id = current_user.id
    apu = Subject.find_id_of_subject(form.subject.data)
    if apu != -999:
        t.subject_id = apu
    else:
        s = Subject(form.subject.data)
        db.session().add(s)
        db.session().commit()
        apu2 = Subject.find_id_of_subject(form.subject.data)
        t.subject_id = apu2

    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("tasks_index"))

@app.route("/delete", methods=["POST"])
def delete():
    id = request.form.get("id")
    task = Task.query.filter_by(id=id).first()
    db.session.delete(task)
    db.session.commit()
    return redirect("/")

