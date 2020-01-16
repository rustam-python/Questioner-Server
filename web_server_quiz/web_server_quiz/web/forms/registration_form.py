from wtforms import StringField, PasswordField, IntegerField, RadioField, Form, validators
from wtforms.fields.html5 import EmailField
from wtforms.widgets import html5


class IndexFormError(Exception):
    pass


class BaseForm(Form):
    """
    Base class reconfiguration in order to turn off nasty csrf tokens
    """

    class Meta:
        csrf = False


class RegistrationForm(BaseForm):
    username = StringField('Username', validators=[validators.required()])
    password = PasswordField('Password', validators=[validators.required()])
    repeat_password = PasswordField('Password', validators=[validators.required()])
    email = EmailField('e-mail', validators=[validators.required(), validators.Email()])
    gender = RadioField('gender', validators=[validators.required()], choices=[('male', 'Male'),
                                                                               ('female', 'Female')])
    age = IntegerField('Age', widget=html5.NumberInput(min="1", max="99"), validators=[validators.required()])
    religion = StringField('religion', validators=[validators.required()])
