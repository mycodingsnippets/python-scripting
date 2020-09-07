from flask import Flask, request, jsonify, make_response
import jwt
import datetime
from functools import wraps
from data.names import secretData
import os
from utilities.customDecorators import verifyToken

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRETKEY')

@app.after_request
def add_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With'
    response.headers['Access-Control-Allow-Methods'] = 'POST,GET,PUT,DELETE,OPTIONS'
    return response

@app.route('/login')
def login():
    auth = request.authorization
    if auth and auth.username=='aditya' and auth.password=='abcde123':
        token = jwt.encode({'user': auth.username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])
        return jsonify({'token': token.decode('UTF-8')})
    return make_response("Couldn't verify", 401, {'WWW-Authenticate':'Basic realm="Login Required"'})
    
@app.route('/', methods=['GET'])
@verifyToken
def names():
    return jsonify({'names':secretData()})

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8888)