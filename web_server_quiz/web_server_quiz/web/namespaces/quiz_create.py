from flask import request, jsonify
from flask_restplus import Namespace, Resource

from models import QuizNames, QuizQuestions, Choices

api = Namespace(
    name='Create quiz',
    description='Creates quiz',
    path='/quiz_create'
)


@api.route('/')
class QuizCreate(Resource):
    @api.response(200, 'Success')
    def post(self):
        data = request.get_json()
        if data['quiz_name'] == '' or data['quiz_description'] == '':
            return jsonify({'message': 'no data'})
        else:
            quiz_name = data['quiz_name']
            quiz_description = data['quiz_description']
            QuizNames.add(quiz_name=quiz_name, description=quiz_description)
            quiz_id = QuizNames.get(QuizNames.quiz_name == quiz_name)

            for key, value in data.items():
                if 'question' in key:
                    QuizQuestions.add(quiz_id=quiz_id, question_text=value['question-text'])
                    question = QuizQuestions.get(QuizQuestions.question_text == value['question-text'])
                    Choices.add(question_id=question.id, choice_text=value['choice']['answer-1'])
                    Choices.add(question_id=question.id, choice_text=value['choice']['answer-2'])
                    Choices.add(question_id=question.id, choice_text=value['choice']['answer-3'])
                    Choices.add(question_id=question.id, choice_text=value['choice']['answer-4'])
                    correct_answer_json = value['choice']['is-correct']  # get correct answer name
                    correct_answer_db = Choices.get(
                        Choices.choice_text == value['choice'][
                            correct_answer_json])  # get answer_id by correct_answer value.
                    Choices.update({Choices.is_correct: True}).where(
                        Choices.id == correct_answer_db.id).execute()  # update selected answer with "is_correct" flag.
            return jsonify(data)
