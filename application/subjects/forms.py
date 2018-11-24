from flask_wtf import FlaskForm
from wtforms import StringField

class SubjectForm(FlaskForm):
    name = StringField("Aihe")
 
    class Meta:
        csrf = False
