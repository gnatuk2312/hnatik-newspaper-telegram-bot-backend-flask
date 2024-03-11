import uuid

from .. import db
from .model import NewspaperSubscription


class NewspaperSubscriptionService:
    def __get_by_subscription_type_and_params(self, subscription_type, params):
        newspaper_subscription = NewspaperSubscription.query.filter_by(
            subscription_type=subscription_type, params=params
        ).one_or_none()

        return newspaper_subscription

    def get_by_id(self, id):
        newspaper_subscription = NewspaperSubscription.query.get(id)

        return newspaper_subscription.to_dict()

    def get_all(self):
        newspaper_subscriptions = NewspaperSubscription.query.all()
        print(newspaper_subscriptions)

        return [ns.to_dict() for ns in newspaper_subscriptions]

    def create(self, body):
        subscription_type = body["subscriptionType"]
        params = body["params"]
        user_id = body["userId"]

        already_exists = self.__get_by_subscription_type_and_params(
            subscription_type, params
        )
        if already_exists:
            return already_exists.to_dict()

        id = str(uuid.uuid4())
        newspaper_subscription = NewspaperSubscription(
            id=id, subscription_type=subscription_type, params=params, user_id=user_id
        )

        db.session.add(newspaper_subscription)
        db.session.commit()

        response = self.get_by_id(id)
        print("response")
        return response

    def delete_all_by_user_id(self, user_id):
        NewspaperSubscription.query.filter(
            NewspaperSubscription.user_id == user_id
        ).delete()

        db.session.commit()
        return "DONE"
