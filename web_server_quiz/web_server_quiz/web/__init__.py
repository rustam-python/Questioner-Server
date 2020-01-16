import os

from flask import Flask
from flask_cors import CORS
from flask_login import LoginManager
# from flask_admin import Admin
# from flask_admin.contrib.peewee import ModelView

import log_tools
from models import User, QuizNames, QuizQuestions, Choices
from .api import api
from .blueprints import frontend
from .namespaces import *

login = LoginManager()
logger = log_tools.SmartLogger(class_name=__name__, parameter='--')


def create_app() -> Flask:
    app = Flask(__name__)

    app.config['BOOTSTRAP_SERVE_LOCAL'] = True
    app.config['SECRET_KEY'] = 'devkey'

    # DB
    app.config['DB_USERNAME'] = os.environ['POSTGRES_USER']
    app.config['DB_PASSWORD'] = os.environ['POSTGRES_PASSWORD']
    app.config['DB_HOST'] = os.environ['POSTGRES_DB_HOST_NAME']
    app.config['DB_PORT'] = os.environ['POSTGRES_DB_PORT']
    app.config['DB_BASE'] = os.environ['POSTGRES_DB']

    # SERVER
    app.config['SERVER_HOST'] = os.environ['SERVER_HOST']
    app.config['SERVER_PORT'] = os.environ['SERVER_PORT']

    app.register_blueprint(frontend)

    # admin = Admin(app)
    # admin.add_view(ModelView(QuizNames))
    # admin.add_view(ModelView(QuizQuestions))
    # admin.add_view(ModelView(Choices))

    api.init_app(app)
    api.add_namespace(user_validation)
    api.add_namespace(quiz_create)
    api.add_namespace(quiz_get_quiz_list)

    login.init_app(app)
    login.login_view = 'frontend.login'

    # Bootstrap(app)
    CORS(app)

    return app


@login.user_loader
def load_user(user_id):
    try:
        return User.get_by_id(int(user_id))
    except RuntimeError as err:
        logger.write(message=str(err), level=log_tools.Levels.failure)
