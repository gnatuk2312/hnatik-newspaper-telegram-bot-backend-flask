import uuid

from .. import db
from .model import User


class UserService:
    def get_by_id(self, id):
        user = User.query.get(id)

        return user.to_dict()

    def get_by_chat_id(self, chat_id):
        user = User.query.filter(User.chat_id == chat_id).one_or_404()

        return user.to_dict()

    def get_all(self):
        users = User.query.all()

        return [user.to_dict() for user in users]

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
