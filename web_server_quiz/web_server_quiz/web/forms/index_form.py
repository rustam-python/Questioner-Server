from wtforms import StringField, PasswordField, SubmitField, Form
from wtforms.validators import DataRequired


class IndexFormError(Exception):
    pass


class BaseForm(Form):
    """
    Base class reconfiguration in order to turn off nasty csrf tokens
    """

    class Meta:
        csrf = False


class IndexForm(BaseForm):
    pass
