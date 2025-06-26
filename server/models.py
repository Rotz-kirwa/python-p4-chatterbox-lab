from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData, DateTime, func
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class Message(db.Model, SerializerMixin):
    __tablename__ = 'messages'

    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String, nullable=False)
    username = db.Column(db.String, nullable=False)
    created_at = db.Column(DateTime, server_default=func.now())
    updated_at = db.Column(DateTime, onupdate=func.now())

    # Optional: to prevent circular reference errors
    serialize_rules = ('-created_at', '-updated_at')  # you can remove this if you want those fields

    def __repr__(self):
        return f"<Message #{self.id} from {self.username}>"
