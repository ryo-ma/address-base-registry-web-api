import json
from flask import abort, Flask, Blueprint, jsonify, request
from flask_cors import cross_origin


app = Flask(__name__)

apiv1 = Blueprint('apiv1', __name__, url_prefix='/api/v1')

@app.route('/')
def index():
    return jsonify({'message': 'Web API to get base registry'})

app.register_blueprint(apiv1)

