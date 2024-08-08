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

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """returns a User ID based on a Session ID

        Args:
            session_id (str): the session id
        Returns:
            str: the user id that has that session
        """
        if type(session_id) is str:
            return self.user_id_by_session_id.get(session_id)
