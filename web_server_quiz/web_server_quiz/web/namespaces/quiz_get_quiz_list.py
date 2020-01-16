from flask import jsonify
from flask_restplus import Namespace, Resource
from peewee import fn

from models import QuizNames
from models import QuizQuestions

api = Namespace(
    name='Get quiz list',
    description='Returns returns list of available quiz with descriptions.',
    path='/get_quiz_list'
)


@api.route('/')
class QuizList(Resource):
    @api.response(200, 'Success')
    def get(self):
        quiz_list = [quiz for quiz in QuizQuestions.select(QuizNames.id.alias('quiz_id'), QuizNames.quiz_name,
                                                           QuizNames.description, fn.COUNT(QuizQuestions.id).alias(
                                                               'questions_count')).dicts().join(QuizNames).group_by(
            QuizNames.id, QuizNames.quiz_name, QuizNames.description)]
        return jsonify(quiz_list)
