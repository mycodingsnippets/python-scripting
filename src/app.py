from flask import Flask, request, jsonify
from data.test import dummy_list

app = Flask(__name__)

@app.after_request
def add_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With'
    response.headers['Access-Control-Allow-Methods'] = 'POST,GET,PUT,DELETE,OPTIONS'
    return response

@app.route('/', methods=['GET'])
def hello():
    #return jsonify(request.get_json())
    return jsonify(dummy_list())

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8888)