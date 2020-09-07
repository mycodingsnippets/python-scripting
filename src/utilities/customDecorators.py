from functools import wraps
from flask import request, jsonify
import jwt
import os

def verifyToken(f):
    @wraps(f)
    def wrapped(*args, **kwargs):
        print(os.getenv('SECRETKEY'))
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'message': 'Token is missing'}), 403

        token = token.split()[1]
        try:
            data = jwt.decode(token, 'dotcomengineer')
        except:
            return jsonify({'message':'Token is invalid'}), 403  
        return f(*args, **kwargs)
        
    return wrapped
