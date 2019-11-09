from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length

class SelectAgeForm(FlaskForm):
    user_age = SelectField('Your_age',
                           validators=[DataRequired()],
                           choices=[('1', 'Jovem'), ('2', 'Adulto'), ('3', 'Idoso')])
    submit = SubmitField('Continuar')

class FraseForm(FlaskForm):
    frase = StringField('User_phrase',
                        validators=[DataRequired(), Length(max=150)])
    submit = SubmitField('Enviar')



