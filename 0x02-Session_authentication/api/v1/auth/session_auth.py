#!/usr/bin/env python3
"""Module for session Authentication
"""
import uuid
from .auth import Auth
from models.user import User


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

    def current_user(self, request=None):
        """returns a User instance based on a cookie value

        Args:
            request (request obj): A request obj
        Returns:
            User obj: returns a user object
        """
        session_id = self.session_cookie(request)
        user_id = self.user_id_for_session_id(session_id)
        return User.get(user_id)
