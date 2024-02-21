from . import create_app

app = create_app()


@app.route("/")
def hello():
    return "Hello world"


from .users.controller import UserController
from .newspaper_subscription.controller import NewspaperSubscriptionController
