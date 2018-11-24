from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, validators

class TaskForm(FlaskForm):
    name = StringField("Kysymys", [validators.Length(min=5)])
    answer = StringField("Vastaus")
    subject = StringField("Aihealue")
 
    class Meta:
        csrf = False
