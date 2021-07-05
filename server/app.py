# https://flask.palletsprojects.com/en/2.0.x/quickstart/
# pip3 install flask
# pip3 install flask_cors
#
#   - powershell -
#
#   $env:FLASK_APP="app"
#   python -m flask run
#
#   - Bash -
#
#   export FLASK_APP=app
#   flask run

from flask import Flask, jsonify, request
from flask_cors import CORS
from services.requestExecuter import RequestExecuter

app = Flask(__name__)
CORS(app)

##
# API routes
##

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/api/products/<product_id>', methods=['POST'])
def get_product(product_id):
  if request.method == 'POST':
    body = request.get_json()

    print(body)
    result = RequestExecuter().executeRequest(product_id, body["username"], body["password"], bool(body["isSentinel5P"]))
    response = {
      "result": result
    }

    return jsonify(response)
