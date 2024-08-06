#!/usr/bin/env python3
"""Module for API authentication
"""
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
            if path.startswith(excluded) or path == excluded:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """
        Return:
            None
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Return:
            None
        """
        return None
