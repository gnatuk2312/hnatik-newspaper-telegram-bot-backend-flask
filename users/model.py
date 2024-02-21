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

    def to_dictionary(self):
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}
