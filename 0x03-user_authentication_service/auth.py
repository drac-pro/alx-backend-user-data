#!/usr/bin/env python3
""" auth module
"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """hashes a user password

    Args:
        password (str): user's password
    Returns:
        bytes: bcrypt hashed string
    """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())
