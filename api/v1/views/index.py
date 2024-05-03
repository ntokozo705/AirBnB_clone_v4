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


@app_views.route('/stats', strict_slashes=False)
def app_stats():
    '''Endpoint to retrieve the number of each objects by type.'''
    obj_counts = {}
    for cls, value in classes.items():
        obj_counts[cls] = storage.coumt(value)
    return jsonify(obj_counts)


if __name__ == "__main__":
    pass
