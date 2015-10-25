from flask_wtf import Form
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired

class FormNovaTarefa(Form):
    titulo = StringField('titulo', validators=[DataRequired()])
    descricao = TextAreaField('descricao', validators=[DataRequired()])
