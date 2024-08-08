#!/usr/bin/env python3
"""Module for API authentication
"""
from os import getenv
from flask import request
from typing import List, TypeVar


class Auth:
    """class to manage the API authentication.
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """checks if path is found in the list of excluded paths
        Args:
            path(str): path
            excluded_paths(list): list of paths
        Return:
            False if path in excluded_paths other wise True
        """
        if path is None or excluded_paths is None or excluded_paths == []:
            return True
        path = path if path.endswith('/') else path + '/'
        for excluded in excluded_paths:
            if excluded.endswith('*'):
                if path.startswith(excluded[:-1]):
                    return False
            elif path.startswith(excluded) or path == excluded:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """gets the Authorization header value in a request

        Args:
            request: The request object from which to get the header.
        Returns:
            The value of the Authorization header if it exists, otherwise None.
        """
        if request is None:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):  # type: ignore
        """
        Return:
            None
        """
        return None

    def session_cookie(self, request=None):
        """returns a cookie value from a request

        Args:
            request (request obj): a request object
        Returns:
            any: the value of a request cookie specified in SESSION_NAME
        """
        if request:
            return request.cookies.get(getenv('SESSION_NAME'))
