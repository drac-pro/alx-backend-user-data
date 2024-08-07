#!/usr/bin/env python3
"""Module for API Basic authentication
"""
from models.user import User
from typing import TypeVar
from .auth import Auth
import base64


class BasicAuth(Auth):
    """class to manage the API Basic authentication.
    """
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """returns the Base64 part of the Authorization header for a
        Basic Authentication

        Args:
            authorization_header (str): authorization header

        Returns:
            str: Base64 part of the Authorization header
        """
        if type(authorization_header) is str:
            if authorization_header.startswith('Basic '):
                return authorization_header.split(' ')[1]
        return None

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """returns the decoded value of a Base64 string
        base64_authorization_header

        Args:
            base64_authorization_header (str): base64 encoded string

        Returns:
            str: a utf-8 decoded base64 encoded string
        """
        if type(base64_authorization_header) is str:
            try:
                decoded_bytes = base64.b64decode(base64_authorization_header,
                                                 validate=True)
                return decoded_bytes.decode('utf-8')
            except Exception:
                return None
        return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """returns the user email and password from the Base64 decoded value

        Args:
            decoded_base64_authorization_header (str): \
                decoded base64 authorization header
        Returns:
            tuple(str, str): tuple with user email and password
        """
        if type(decoded_base64_authorization_header) is str and \
                ':' in decoded_base64_authorization_header:
            return tuple(decoded_base64_authorization_header.split(':'))
        return (None, None)

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """returns the User instance based on his email and password.

        Args:
            user_email (str): user email
            user_pwd (str): user password

        Returns:
            User: a user object
        """
        if user_email and type(user_email) is str:
            try:
                users = User.search({'email': user_email})
                if len(users) > 0:
                    if users[0].is_valid_password(user_pwd):
                        return users[0]
            except Exception:
                return None
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """overloads Auth and retrieves the User instance for a request

        Args:
            request: a request object
        Returns:
            a user object
        """
        auth_header = self.authorization_header(request)
        b64_auth_str = self.extract_base64_authorization_header(auth_header)
        auth_str = self.decode_base64_authorization_header(b64_auth_str)
        email, password = self.extract_user_credentials(auth_str)
        return self.user_object_from_credentials(email, password)
