"""User Module
"""
import mongoengine as me
from models.base import Base


me.connect(db="db_bp", host='127.0.0.1', port=27017)


class User(me.Document, Base):
    """User Model
    Attributes:
        id (string): generate with uuid
        tel (string): telephone
        email (string): user email
        city (string): user residence city
        first_name (string): user first name
        last_name (string): user last name
        hashed_password (string): user hashed password
    """
    tel = me.StringField(required=True, unique=True)
    email = me.EmailField(required=True, unique=True)
    city = me.StringField(required=True)
    first_name = me.StringField(required=True, max_length=255)
    last_name = me.StringField(required=True, max_length=255)
    hashed_password = me.StringField(required=True)
    session_id = me.UUIDField(binary=False)
    reset_token = me.UUIDField(binary=False)

    meta = {'collection': 'users'}
