#!/usr/bin/env python3
"""Module for API Basic authentication
"""
from .auth import Auth


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
