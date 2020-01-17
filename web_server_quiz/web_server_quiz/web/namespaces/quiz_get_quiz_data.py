from flask import jsonify, request
from flask_restplus import Namespace, Resource
from peewee import fn

from models import QuizNames, Choices
from models import QuizQuestions

api = Namespace(
    name='Get quiz data',
    description='Returns quiz elements.',
    path='/get_quiz'
)


@api.route('/quiz_list')
class QuizList(Resource):
    @api.response(200, 'Success')
    def get(self):
        quiz_list = [quiz for quiz in QuizQuestions.select(QuizNames.id.alias('quiz_id'), QuizNames.quiz_name,
                                                           QuizNames.description, fn.COUNT(QuizQuestions.id).alias(
                'questions_count')).dicts().join(QuizNames).group_by(
            QuizNames.id, QuizNames.quiz_name, QuizNames.description)]
        return jsonify(quiz_list)


@api.route('/quiz_result')
class QuizResult(Resource):
    @api.response(200, 'Success')
    def post(self):
        data = request.get_json()
        quiz_id = data['url'].split('/')[-1]  # split "/quiz/10" by "/" and get "10".
        answers_correct_row = [quiz for quiz in Choices.select(Choices.id).dicts().join(QuizQuestions).group_by()
            .where((Choices.is_correct == True) & (QuizQuestions.quiz_id == quiz_id))]
        answers_correct_db = {id_['id'] for id_ in answers_correct_row}
        answers_user = {int(v) for k, v in data.items() if k != 'url'}
        correct_answers_count = len(answers_correct_db) - len(answers_user.difference(answers_correct_db))
        percent = (100 * correct_answers_count)//len(answers_user)
        return jsonify({'score': percent})
