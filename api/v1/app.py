#!/usr/bin/python3
"""Flask web application"""

from flask import Flask, jsonify, make_response
from flask_cors import CORS
from models import storage
from api.v1.views import app_views
import os


app = Flask(__name__)

# Enable CORS and allow requests from any orgin:
CORS(app, resources={r'/*': {'origins': '0.0.0.0'}})
# Register the app_views blueprint:
app.register_blueprint(app_views)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown_db(exception):
    """
    Calls storage.close() at the end of the request
    """
    storage.close()


@app.errorhandler(404)
def handle_404_error(error):
    """Handler for Not Found errors"""
    return make_response(jsonify({"error": "Not found"}), 404)


if __name__ == "__main__":
    host = os.getenv("HBNB_API_HOST", "0.0.0.0")
    port = os.getenv("HBNB_API_PORT", 5000)
    app.run(host=host, port=port, threaded=True)
