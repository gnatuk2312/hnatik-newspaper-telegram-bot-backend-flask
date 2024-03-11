from flask import request

from ..app import app
from .service import NewspaperSubscriptionService

newspaper_subscription_service = NewspaperSubscriptionService()


class NewspaperSubscriptionController:
    @staticmethod
    @app.get("/newspaper-subscriptions/<id>")
    def get_newspaper_subscription_by_id(id):
        return newspaper_subscription_service.get_by_id(id)

    @staticmethod
    @app.get("/newspaper-subscriptions")
    def get_all_newspaper_subscriptions():
        return newspaper_subscription_service.get_all()

    @staticmethod
    @app.post("/newspaper-subscriptions")
    def create_newspaper_subscription():
        body = request.get_json()

        return newspaper_subscription_service.create(body)

    @staticmethod
    @app.delete("/newspaper-subscriptions/<user_id>")
    def delete_all_newspaper_subscriptions_by_user_id(user_id):
        return newspaper_subscription_service.delete_all_by_user_id(user_id)
