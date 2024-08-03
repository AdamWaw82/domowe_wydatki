from flask_wtf import FlaskForm
from wtforms.fields.choices import SelectField
from wtforms.fields.datetime import DateField
from wtforms.fields.numeric import DecimalField
from wtforms.fields.simple import TextAreaField
from wtforms.validators import DataRequired


class WydatekForm(FlaskForm):

    date = DateField("Data", validators=[DataRequired()])
    kategoria = SelectField('Kategoria', coerce=str, choices=[
        ("", 'Wybierz kategorię'),
        ("food", 'Jedzenie'),
        ("transport", "Transport"),
        ("utilities", "Rachunki"),
        ("entertainment", "Rozrywka"),
        ("other", "Inne")
    ], validators=[DataRequired()])
    opis = TextAreaField('Opis', validators=[DataRequired()])
    kwota = DecimalField('Kwota', validators=[DataRequired()])
