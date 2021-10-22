from logging import PlaceHolder
from flask_wtf import FlaskForm
from wtforms import TextField, SubmitField, PasswordField
from wtforms.fields.core import SelectField
from wtforms.fields.html5 import DateField, DateTimeLocalField, EmailField
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


class AgregarAvion(FlaskForm):
    id = TextField(
        'ID *', validators=[InputRequired(message='Indique el ID')])
    modelo = TextField(
        'Modelo *', validators=[InputRequired(message='Indique el modelo')])
    matricula = TextField(
        'Matricula *', validators=[InputRequired(message='Indique el matrícula')])
    cantidad = TextField(
        'Cantidad de Pasajeros *', validators=[InputRequired(message='Indique la cantidad de pasajeros')])
    btn = SubmitField('AgregarAvion')


class AgregarUsuario(FlaskForm):
    id = TextField('ID ')
    nombres = TextField(
        'Nombre *', validators=[InputRequired(message='Indique el nombre')])
    apellidos = TextField(
        'Apellido *', validators=[InputRequired(message='Indique el apellido')])
    numero = TextField(
        'Número de Teléfono *', validators=[InputRequired(message='Indique el número de teléfono')])

    usuario = TextField(
        'Usuario *', validators=[InputRequired(message='Indique el usuario')])

    email = EmailField(
        'Email *', validators=[InputRequired(message='Indique el email')])
    clave = PasswordField(
        'Clave *', validators=[InputRequired(message='Indique la clave')])
    tipoUsuario = SelectField('Tipo de Usuario', choices=[(
        'p', 'piloto'), ('c', 'usuario final'), ('a', 'SuperUsuario')])
    btn = SubmitField('Agregar Usuario')


class AgregarPilotos(FlaskForm):
    id = TextField(
        'ID *', validators=[InputRequired(message='Indique el ID')])
    nombres = TextField(
        'Nombre *', validators=[InputRequired(message='Indique el nombre')])
    apellidos = TextField(
        'Apellido *', validators=[InputRequired(message='Indique el apellido')])
    usuario = TextField(
        'Usuario *', validators=[InputRequired(message='Indique el usuario')])
    email = EmailField(
        'Email *', validators=[InputRequired(message='Indique el email')])
    clave = PasswordField(
        'Clave *', validators=[InputRequired(message='Indique la clave')])
    numero = TextField(
        'Número de Teléfono*', validators=[InputRequired(message='Indique el número de teléfono')])
    direccion = TextField(
        'Dirección *', validators=[InputRequired(message='Indique una dirección')])
    fechaIngreso = DateField(
        'Fecha de Ingreso *', validators=[InputRequired(message='Indique la fecha de ingreso')])
    tiempoC = TextField(
        'Tiempo del contrato (meses)*', validators=[InputRequired(message='Indique el tiempo del contrato')])
    estado = SelectField('Estado', choices=[
                         ('A', 'Activo'), ('I', 'Inactivo')])

    btn = SubmitField('Agregar Piloto')


class AgregarVuelo(FlaskForm):
    id = TextField(
        'ID *', validators=[InputRequired(message='Indique la id')])
    origen = TextField(
        'Origen *', validators=[InputRequired(message='Indique la ciudad origen')])
    destino = TextField(
        'Destino *', validators=[InputRequired(message='Indique la ciudad destino')])
    cupos = TextField(
        'Cupos *', validators=[InputRequired(message='Indique el número de cupos')])
    avion = SelectField('Avion *', choices=[])
    piloto = SelectField('Piloto *', choices=[])
    # fechaSalida = DateTimeLocalField(
    #     'Fecha de Salida *', validators=[InputRequired(message='Indique la fecha de salida')])
    fechaSalida = DateField(
        'Fecha de Salida *', validators=[InputRequired(message='Indique la fecha de salida')])
    cupos = TextField(
        'Cupos *', validators=[InputRequired(message='Indique el número de cupos')])
    btn = SubmitField('Agregar Vuelo')
