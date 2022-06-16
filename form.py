from unicodedata import numeric
from wtforms import Form, BooleanField, StringField, PasswordField, validators, ValidationError, SubmitField

from wtforms.validators import InputRequired, Length

class consulta(Form):
    username = StringField('username', validators=[InputRequired(),
                                             Length(min=4, max=15)])



