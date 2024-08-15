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
            raise ValueError(f'User {email} already exists')
        except NoResultFound:
            hashed_password = _hash_password(password)
            user = User(email=email, hashed_password=hashed_password)
            self._db._session.add(user)
            self._db._session.commit()
            return user
