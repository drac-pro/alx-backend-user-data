#!/usr/bin/env python3
""" user session module
"""
from .base import Base


class UserSession(Base):
    """ UserSession class
    Authenticates user based on session ID stored in database
    """
    def __init__(self, *args: list, **kwargs: dict):
        super().__init__(*args, **kwargs)
        self.user_id = kwargs.get('user_id')
        self.session_id = kwargs.get('session_id')
