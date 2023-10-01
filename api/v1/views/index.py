#!/usr/bin/python3
"""JSON file status """

from api.v1.views import app_views
from flask import jsonify


@app_views.route("/status", methods=["GET"])
def status():
    '''
    Returns a JSON response for RESTful API health.
    '''
    return jsonify({"status": "OK"})
