# $env:FLASK_APP="app"
# python -m flask run

from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

##
# API routes
##

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/api/products/<product_id>')
def get_product(product_id):
  return jsonify({"result": "You requested jsonld for " + product_id})