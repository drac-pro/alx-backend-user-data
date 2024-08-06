#!/usr/bin/env python3
"""Module for API Basic authentication
"""
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
