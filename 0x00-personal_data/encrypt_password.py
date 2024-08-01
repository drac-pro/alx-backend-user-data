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


def is_valid(hashed_password: bytes, password: str) -> bool:
    """checks if a password is a valid password that was hashed

    Args:
        hashed_password(byte): bcrypt hash byte string

        password(str): password string
    Returns:
        True if password is correct or false other wise
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
