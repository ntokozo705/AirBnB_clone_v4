#!/usr/bin/python3
'''Python Interpreter'''

from api.v1.views import app_views
from flask import Flask, Blueprint, jsonify
from models import storage


classes = {
        'Amenities': 'Amenity',
        'Cities': 'City',
        'Places': 'Place',
        'Reviews': 'Review',
        'States': 'State',
        'Users': 'User'
}


@app_views.route('/status', strict_slashes=False)
def app_status:
    '''Function to return route status.

    Returns:
        JSON: "status": "OK"
    '''
    return jsonify({"status": "OK"})
