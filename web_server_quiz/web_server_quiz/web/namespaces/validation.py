import peewee

from flask import request, jsonify
from flask_restplus import Namespace, Resource

from models import User

api = Namespace(
    name='Validation',
    description='Returns registration validation result',
    path='/validation'
)


@api.route('/validate_user')
class UserValidation(Resource):
    @api.response(200, 'Success')
    def post(self):
        data = request.get_json()
        try:
            User.get(User.username == data)
            return jsonify({"message": "username is already in use"})
        except peewee.DoesNotExist:
            return jsonify({"message": "username is available"})


@api.route('/validate_email')
class EmailValidation(Resource):
    @api.response(200, 'Success')
    def post(self):
        data = request.get_json()
        try:
            User.get(User.email == data)
            return jsonify({"message": "email is already in use"})
        except peewee.DoesNotExist:
            return jsonify({"message": "email is available"})
