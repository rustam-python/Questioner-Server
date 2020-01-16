from wtforms import StringField, PasswordField, SubmitField, BooleanField, Form
from wtforms.validators import DataRequired


class IndexFormError(Exception):
    pass


class BaseForm(Form):
    """
    Base class reconfiguration in order to turn off nasty csrf tokens
    """

    class Meta:
        csrf = False


class LoginForm(BaseForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    sign_in_button = SubmitField('Sign In')
