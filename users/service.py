import uuid

from .. import db
from .model import User


class UserService:
    def get_by_id(self, id):
        user = User.query.get(id).to_dictionary()

        return user

    def get_all(self):
        users = User.query.all()

        response = []
        for user in users:
            response.append(user.to_dictionary())

        return response

    def create(self, body):
        id = str(uuid.uuid4())
        user = User(
            id=id,
            username=body["username"],
            first_name=body["firstName"],
            last_name=body["lastName"],
            chat_id=body["chatId"],
        )

        db.session.add(user)
        db.session.commit()

        response = self.get_by_id(id)

        return response
