from flask import request

from ..app import app
from .controller import get_all_users_controller, create_user_controller


@app.route("/users", methods=["GET", "POST"])
def users_controller():
    if (request.method) == "GET":
        return get_all_users_controller()
    if request.method == "POST":
        return create_user_controller()
    return "HTTP method is not allowed in this controller"
