#!/usr/bin/env python3
"""Module for session Authentication expiration
"""
from os import getenv
from datetime import datetime, timedelta
from .session_auth import SessionAuth


class SessionExpAuth(SessionAuth):
    """class to manage expiration of Session authentication
    """
    def __init__(self) -> None:
        """initializes a SessionExpAuth object
        """
        super().__init__()
        self.session_duration = int(getenv('SESSION_DURATION', 0))

    def create_session(self, user_id=None):
        """creates a Session ID for a user_id and store it as key in
        the user_id_by_session_id dict with values user_id and created_at

        Args:
            user_id (str): user id
        Returns:
            str: created session_id
        """
        session_id = super().create_session(user_id)
        if session_id is None:
            return None
        session_dict = {'user_id': user_id,
                        'created_at': datetime.now()}
        self.user_id_by_session_id[session_id] = session_dict
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """returns a User ID based on a Session ID

        Args:
            session_id (str): the session id
        Returns:
            str: the user id that has that session
        """
        if session_id not in self.user_id_by_session_id:
            return None
        session_dict = self.user_id_by_session_id[session_id]
        if self.session_duration <= 0:
            return session_dict['user_id']
        if 'created_at' not in session_dict.keys():
            return None
        time_span = timedelta(seconds=self.session_duration)
        if (session_dict['created_at'] + time_span) < datetime.now():
            return None
        return session_dict['user_id']
