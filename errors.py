from flask import make_response, jsonify
from flask import Blueprint

app = Blueprint("errors", __name__)


@app.app_errorhandler(404)
def not_found():
    return make_response(jsonify({'error': 'Not found', 'status_code': 404}), 404)


@app.errorhandler(400)
def bad_request():
    return make_response(jsonify({'error': 'Bad request', 'status_code': 400}), 400)
