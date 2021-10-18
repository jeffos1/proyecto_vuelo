from flask_wtf import FlaskForm
from wtforms import TextField, SubmitField, PasswordField
from wtforms.fields.html5 import EmailField
from wtforms.validators import EqualTo, InputRequired
from markupsafe import Markup


class Login(FlaskForm):
    # maskup
    user_icon = Markup(
        '<i class="bi bi-person text_purple" style="font-size: 2.5rem;"></i>')
    pass_icon = Markup(
        '<i class="bi bi-lock text_purple" style="font-size: 2.5rem;"></i>')
    usuario = TextField(user_icon, validators=[
                        InputRequired(message='Indique el usuario')])

    clave = PasswordField(
        pass_icon, validators=[InputRequired(message='Indique la clave')])
    btn = SubmitField('Login')


class Registro(FlaskForm):

    nombre = TextField(
        'Nombre *', validators=[InputRequired(message='Indique el nombre')])
    apellido = TextField(
        'Apellido *', validators=[InputRequired(message='Indique el apellido')])
    numero = TextField(
        'Numero *', validators=[InputRequired(message='Indique el numero')])

    usuario = TextField(
        'Usuario *', validators=[InputRequired(message='Indique el usuario')])

    email = EmailField(
        'Email *', validators=[InputRequired(message='Indique el email')])
    clave = PasswordField(
        'Clave *', validators=[InputRequired(message='Indique la clave')])
    verificacion_clave = PasswordField('Verificación *', validators=[InputRequired(
        message='Indique la verificación'), EqualTo(clave, message='Clave y la verificación no coinciden')])
    btn = SubmitField('Registrar')
