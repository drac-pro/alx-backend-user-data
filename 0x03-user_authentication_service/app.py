#!/usr/bin/env python3
""" flask app module
"""
from flask import Flask, jsonify, request
from auth import Auth


app = Flask(__name__)
AUTH = Auth()


@app.route('/', strict_slashes=False)
def index():
    """ index route
    """
    return jsonify({'message': 'Bienvenue'})


@app.route('/users', methods=['POST'], strict_slashes=False)
def users():
    """ route to register a new user
    """
    try:
        AUTH.register_user(request.form.get('email'),
                           request.form.get('password'))
        return jsonify({'email': request.form.get('email'),
                        'message': 'user created'})
    except Exception:
        return jsonify({'message': 'email already registered'}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
