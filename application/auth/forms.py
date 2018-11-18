from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField
  
class LoginForm(FlaskForm):
    name = StringField("Käyttäjänimi")
    username = StringField("Käyttäjätunnus")
    password = PasswordField("Salasana")
  
    class Meta:
        csrf = False
