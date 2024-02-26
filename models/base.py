"""Base Module
"""
import uuid
import datetime
import mongoengine as me


class Base:
    """Base Model
    Attributes:
        id (string): generate with uuid
        created_at (datetime): create datetime
        updated_at (datetime): update datetime
    """
    id = me.UUIDField(binary=False, primary_key=True, default=uuid.uuid4())
    created_at = me.DateTimeField(default=datetime.datetime.utcnow)
    updated_at = me.DateTimeField(default=datetime.datetime.utcnow)
