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
#   export FLASK_APP=hello
#   flask run

from flask import Flask, jsonify, request
from flask_cors import CORS

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
    credentials = request.get_json()

    response = {
      "result": {
        "id": product_id,
        "username": credentials["username"],
        "password": credentials["password"]
      }
    }

    return jsonify(response)
