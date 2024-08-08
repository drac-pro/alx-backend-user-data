#!/usr/bin/env python3
"""Module for session Authentication using session id
stored in database
"""
from datetime import datetime, timedelta
from models.user_session import UserSession
from .session_exp_auth import SessionExpAuth


class SessionDBAuth(SessionExpAuth):
    """class to manage expiration of Session authentication
    using database
    """
    def create_session(self, user_id=None):
        """creates a Session ID for a user_id and store it as key in
        the user_id_by_session_id dict with values user_id and created_at
        and saves it to the database

        Args:
            user_id (str): user id
        Returns:
            str: created session_id
        """
        session_id = super().create_session(user_id)
        if type(session_id) is str:
            kwargs = {'user_id': user_id, 'session_id': session_id}
            user_session = UserSession(**kwargs)
            user_session.save()
            return session_id

    def user_id_for_session_id(self, session_id=None):
        """returns a User ID based on a Session ID

        Args:
            session_id (str): the session id
        Returns:
            str: the user id that has that session
        """
        if type(session_id) is str:
            user_sessions = UserSession.search({'session_id': session_id})
            if len(user_sessions) == 0:
                return None
            time_span = timedelta(seconds=self.session_duration)
            if (user_sessions[0].created_at + time_span) < datetime.now():
                return None
            return user_sessions[0].user_id

    def destroy_session(self, request=None):
        """deletes the user session / logout

        Args:
            request (request obj): A user logout request
        """
        session_id = self.session_cookie(request)
        if session_id is not None:
            user_sessions = UserSession.search({'session_id': session_id})
            if len(user_sessions) > 0:
                user_sessions[0].remove()
                return True
        return False
