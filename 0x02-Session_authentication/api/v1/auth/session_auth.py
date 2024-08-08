#!/usr/bin/env python3
"""Module for session Authentication
"""
import uuid
from .auth import Auth


class SessionAuth(Auth):
    """class to manage Session authentication
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """creates a Session ID for a user_id

        Args:
            user_id (str): user id
        Returns:
            str: users session id
        """
        if type(user_id) is str:
            session_id = str(uuid.uuid4())
            self.user_id_by_session_id[session_id] = user_id
            return session_id
