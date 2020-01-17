import hashlib
import os
from typing import Union

from flask_login import UserMixin
from peewee import *
from werkzeug.security import generate_password_hash, check_password_hash


db = PostgresqlDatabase(database=os.environ['POSTGRES_DB'],
                        autocommit=True,
                        autorollback=True,
                        user=os.environ['POSTGRES_USER'],
                        password=os.environ['POSTGRES_PASSWORD'],
                        host=os.environ['POSTGRES_DB_HOST_NAME'],
                        port=os.environ['POSTGRES_DB_PORT'])


class BaseModel(Model):
    """A base model that will use our database."""
    class Meta:
        database = db

    @classmethod
    def recreate_tables(cls):
        db.connect(reuse_if_open=True)
        table_list = db.get_tables()
        for model in cls.__subclasses__():
            if model.__name__.lower() not in table_list:
                db.create_tables([model])
                print(f'Table {model} was not found in DB. New table was created to fix that.')


class User(UserMixin, BaseModel):
    id = PrimaryKeyField(index=True)
    username = CharField(unique=True)
    password_hash = CharField()
    email = CharField(unique=True)
    gender = CharField()
    age = CharField()
    religion = CharField()
    authenticated = BooleanField(default=False)
    admin = BooleanField(default=False)

    @classmethod
    def add(cls, username: str, email: str, password: str, gender: str, age: str, religion: str) -> Union['User', None]:
        try:
            return cls.get(cls.username == username)
        except cls.DoesNotExist:  # If user is not created - create it in db
            user = cls.create(
                username=username,
                email=email,
                password_hash=hashlib.sha256(password.encode('UTF-8')).hexdigest(),
                gender=gender,
                age=age,
                religion=religion
                )
            user.save()
            return None


class Sessions(BaseModel):
    id = PrimaryKeyField(index=True)
    user = ForeignKeyField(User)
    result = IntegerField()


class QuizNames(BaseModel):
    id = PrimaryKeyField(index=True)
    quiz_name = CharField(unique=True)
    description = TextField()

    @classmethod
    def add(cls, quiz_name: str, description: str) -> Union['QuizNames', None]:
        try:
            return cls.get(cls.quiz_name == quiz_name)
        except cls.DoesNotExist:
            quiz = cls.create(
                quiz_name=quiz_name,
                description=description,
                )
            quiz.save()
            return None


class QuizQuestions(BaseModel):
    id = PrimaryKeyField(index=True)
    quiz_id = ForeignKeyField(QuizNames)
    question_text = TextField(unique=True)

    @classmethod
    def add(cls, quiz_id: int, question_text: str) -> Union['QuizQuestions', None]:
        try:
            return cls.get(cls.question_text == question_text)
        except cls.DoesNotExist:
            question = cls.create(
                quiz_id=quiz_id,
                question_text=question_text
                )
            question.save()
            return None


class Choices(BaseModel):
    id = PrimaryKeyField(index=True)
    question_id = ForeignKeyField(QuizQuestions)
    choice_text = CharField()
    is_correct = BooleanField(default=False)

    @classmethod
    def add(cls, question_id: int, choice_text: str) -> Union['Choices', None]:
        try:
            return cls.get((cls.choice_text == choice_text) & (cls.question_id == question_id))
        except cls.DoesNotExist:
            quiz = cls.create(
                question_id=question_id,
                choice_text=choice_text
                )
            quiz.save()
            return None
