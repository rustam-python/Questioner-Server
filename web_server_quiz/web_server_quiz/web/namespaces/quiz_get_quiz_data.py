from flask import request, jsonify
from flask_restplus import Namespace, Resource

from models import QuizNames, QuizQuestions

api = Namespace(
    name='Get quiz data',
    description='Returns returns data for quiz',
    path='/get_quiz_data'
)


@api.route('/')
class QuizData(Resource):
    @api.response(200, 'Success')
    def post(self):
        entered_data = request.args.get(key='query')
        return jsonify(payload)
