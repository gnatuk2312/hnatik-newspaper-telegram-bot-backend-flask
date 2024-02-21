from sqlalchemy import inspect
from datetime import datetime

from .. import db


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.String(50), primary_key=True, nullable=False, unique=True)
    created = db.Column(db.DateTime(timezone=True), default=datetime.now)
    updated = db.Column(
        db.DateTime(timezone=True), default=datetime.now, onupdate=datetime.now
    )

    username = db.Column(db.String(100), nullable=False)
    first_name = db.Column(db.String(200), nullable=False)
    last_name = db.Column(db.String(200), nullable=False)
    chat_id = db.Column(db.Integer, nullable=False, unique=True)

    newspaper_subscriptions = db.relationship("NewspaperSubscription", backref="users")

    def __repr__(self):
        return f'<User "{self.username}">'

    def to_dict(self):
        user_dict = {c.name: getattr(self, c.name) for c in self.__table__.columns}
        user_dict["newspaper_subscriptions"] = [
            ns.to_dict() for ns in self.newspaper_subscriptions
        ]
        return user_dict
