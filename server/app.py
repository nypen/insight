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

@app.route('/api/products/<product_id>', methods=['GET'])
def getProduct(product_id):
  isSentinel5P = False
  if(request.args.get('issentinel5p')):
    isSentinel5P = request.args.get('issentinel5p').lower() == 'true'

  username = request.authorization.username
  password = request.authorization.password
  
  result = RequestExecuter().executeRequest(product_id, isSentinel5P, username, password)

  response = {
    "result": result
  }

  return jsonify(response)

@app.route('/api/products/<product_id>/attributes', methods=['POST'])
def getallAttributes(product_id):
  if request.method == 'POST':
    body = request.get_json()

    print(body)
    result = RequestExecuter().executeRequest(product_id, bool(body["isSentinel5P"]), body["username"], body["password"], True)
    response = {
      "result": result
    }

    return jsonify(response)
