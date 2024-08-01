#!/usr/bin/env python3
"""defines a function filter_datum"""
import re
import logging
import mysql.connector
from os import getenv
from typing import List


PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """returns the log message obfuscated"""
    pattern = r'({})=.*?{}'.format('|'.join(fields), separator)
    return re.sub(pattern, r'\1={}{}'.format(redaction, separator), message)


def get_logger() -> logging.Logger:
    """Creates and returns a new logger for user data

    Returns:
        A new logger object
    """
    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    logger.propagate = False
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(RedactingFormatter(list(PII_FIELDS)))
    logger.addHandler(stream_handler)
    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """ Creates a connection to a secure mysql database

    Returns:
        A MySQLConnection object that was created use to manage the connection
    """
    user = getenv('PERSONAL_DATA_DB_USERNAME') or "root"
    passwd = getenv('PERSONAL_DATA_DB_PASSWORD') or ""
    host = getenv('PERSONAL_DATA_DB_HOST') or "localhost"
    db_name = getenv('PERSONAL_DATA_DB_NAME')
    connection = mysql.connector.connect(user=user,
                                   password=passwd,
                                   host=host,
                                   database=db_name)
    return connection


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """formats the logged message to be redacted
        using filter_datum fuction
        """
        record.msg = filter_datum(self.fields, self.REDACTION,
                                  record.getMessage(), self.SEPARATOR)
        return super(RedactingFormatter, self).format(record)
