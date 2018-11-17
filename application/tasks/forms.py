from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, validators

class TaskForm(FlaskForm):
    name = StringField("Kysymys", [validators.Length(min=5)])
    answer = BooleanField("Vastattu")
 
    class Meta:
        csrf = False
