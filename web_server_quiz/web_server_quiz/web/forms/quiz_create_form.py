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


class QuizCreateForm(BaseForm):
    quiz_name = StringField('Username', validators=[validators.required()])
    question_text = StringField('Question text', validators=[validators.required()],
                                render_kw={"placeholder": "Please enter question text"})
    answer_1 = StringField('Answer text', validators=[validators.required()],
                           render_kw={"placeholder": "Please enter answer version"})
    answer_2 = StringField('Answer text', validators=[validators.required()],
                           render_kw={"placeholder": "Please enter answer version"})
    answer_3 = StringField('Answer text', validators=[validators.required()],
                           render_kw={"placeholder": "Please enter answer version"})
    answer_4 = StringField('Answer text', validators=[validators.required()],
                           render_kw={"placeholder": "Please enter answer version"})
    is_correct = RadioField('Choice correct answer', validators=[validators.required()],
                            choices=[('answer_1', 'Answer 1'), ('answer_2', 'Answer 2'),
                                     ('answer_3', 'Answer 3'), ('answer_4', 'Answer 4')])
