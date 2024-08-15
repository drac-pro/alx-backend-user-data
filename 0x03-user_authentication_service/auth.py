#!/usr/bin/env python3
""" auth module
"""
import bcrypt
from user import User
from db import DB
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    """hashes a user password

    Args:
        password (str): user's password
    Returns:
        bytes: bcrypt hashed string
    """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        """initializes an Auth object
        """
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Registers a new user and save to the database

        Args:
            email (str): user's email
            password (str): user's password
        Returns:
            User: the newly created User object
        """
        try:
            self._db.find_user_by(**{'email': email})
        except NoResultFound:
            return self._db.add_user(email, _hash_password(password))
        else:
            raise ValueError(f'User {email} already exists')

    def valid_login(self, email: str, password: str) -> bool:
        """ validates if a user's login credentials

        Args:
            email (str): user's email
            password (str): user's password
        Returns:
            bool: True if user exist and password match.. otherwise False
        """
        try:
            user = self._db.find_user_by(**{'email': email})
            return bcrypt.checkpw(password.encode(), user.hashed_password)
        except Exception:
            return False
