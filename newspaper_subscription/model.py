from sqlalchemy import inspect
from datetime import datetime

from .. import db


class SubscriptionTypeEnum:
    WEATHER = "WEATHER"
    CRYPTOCURRENCY = "CRYPTOCURRENCY"


class NewspaperSubscription(db.Model):
    __tablename__ = "newspaper_subscription"

    id = db.Column(db.String(50), primary_key=True, nullable=False, unique=True)
    created = db.Column(db.DateTime(timezone=True), default=datetime.now)
    updated = db.Column(
        db.DateTime(timezone=True), default=datetime.now, onupdate=datetime.now
    )

    subscription_type = db.Column(db.String(50), nullable=False)
    params = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.String(50), db.ForeignKey("users.id"))

    def __repr__(self):
        return f'<NewspaperSubscription "{self.subscription_type} {self.user_id}">'

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
