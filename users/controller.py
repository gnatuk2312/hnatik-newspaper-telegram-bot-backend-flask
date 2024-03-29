from flask import request

from ..app import app
from .service import UserService

user_service = UserService()


class UserController:
    @staticmethod
    @app.get("/users/<id>")
    def get_user_by_id(id):
        return user_service.get_by_id(id)

    @staticmethod
    @app.get("/users/chat/<chat_id>")
    def get_user_by_chat_id(chat_id):
        return user_service.get_by_chat_id(chat_id)

    @staticmethod
    @app.get("/users")
    def get_all_users():
        return user_service.get_all()

    @staticmethod
    @app.post("/users")
    def create_user():
        body = request.get_json()

        return user_service.create(body)
