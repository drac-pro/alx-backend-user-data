#!/usr/bin/env python3
""" Module for session authentication view
"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models.user import User
from os import getenv


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    """logs in a user to a session
    """
    from api.v1.app import auth

    email = request.form.get(email)
    password = request.form.get(password)
    if email is None or email == '':
        return jsonify({"error": "email missing"}), 400
    if password is None or password == '':
        return jsonify({"error": "password missing"}), 400
    users = User.search({'email': email})
    if len(users) == 0:
        return jsonify({"error": "no user found for this email"}), 404
    if not users[0].is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    session_id = auth.create_session(users[0].id)
    resp = jsonify(users[0].to_json())
    cookie_name = getenv('SESSION_NAME')
    resp.set_cookie(cookie_name, session_id)
    return resp
