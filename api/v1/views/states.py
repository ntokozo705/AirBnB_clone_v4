#!/usr/bin/python3
'''Python Interpreter.'''

from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from models import storage
from models.state import State


@app_views.route('/states', methods=['GET'], strict_slashes=False)
def get_states():
    '''Retrieves the lists of all State objects.'''
    states = []
    for state in storage.all("State").values():
        states.append(state.to_dict())
    return jsonify(states)

@app_views.route('/states/<state_id>', methods=['GET'], strict_slashes=False)
def get_state(state_id):
    '''Retrieves a State object.'''
    state = storage.get("State", state_id)
    if state is None:
        abort(404)
    else:
        return jsonify(state.to_dict())

@app_views.route('/states/<states_id>', methods=['DELETE'], strict_slashes=False)
def delete_state(state_id):
    '''Deletes a State object.'''
    state = storage.get("State", state_id)
    if state is None:
        abort(404)
    else:
        storage.delete(state)
        return jsonify(({}), 200)
