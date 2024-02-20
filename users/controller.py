from flask import request
import uuid

from .. import db
from .model import User


def get_all_users_controller():
    users = User.query.all()

    response = []
    for user in users:
        response.append(user.to_dictionary())

    return response


def create_user_controller():
    body = request.get_json()

    id = str(uuid.uuid4())
    new_user = User(id=id, username=body["username"])

    db.session.add(new_user)
    db.session.commit()

    response = User.query.get(id).to_dictionary()

    return response
