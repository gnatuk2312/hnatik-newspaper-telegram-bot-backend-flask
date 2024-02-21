import uuid

from .. import db
from .model import NewspaperSubscription


class NewspaperSubscriptionService:
    def get_by_id(self, id):
        newspaper_subscription = NewspaperSubscription.query.get(id)

        return newspaper_subscription.to_dict()

    def get_all(self):
        newspaper_subscriptions = NewspaperSubscription.query.all()

        return [ns.to_dict() for ns in newspaper_subscriptions]

    def create(self, body):
        id = str(uuid.uuid4())
        newspaper_subscription = NewspaperSubscription(
            id=id, subscription_type=body["subscriptionType"], user_id=body["userId"]
        )

        db.session.add(newspaper_subscription)
        db.session.commit()

        response = self.get_by_id(id)
        return response
