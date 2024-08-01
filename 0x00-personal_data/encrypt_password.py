#!/usr/bin/env python3
"""defines a hash_password function"""
import bcrypt


def hash_password(password: str) -> bytes:
    """hashes a password
    Args:
        password(str): a string password
    Returns:
        a byscript hash byte string
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
