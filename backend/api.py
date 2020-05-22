from flask import Blueprint, jsonify, request
from random import *

from backend import app, db
from backend.models import Task

api = Blueprint('api', __name__)

@api.route('/hello/<string:name>/')
def say_hello(name):
    response = { 'msg': "Hello {}".format(name) }
    return jsonify(response)

@api.route('/random')
def random_number():
    response = {
            'randomNumber': randint(1, 100)
            }
    return jsonify(response)

@api.route('/get', methods=['GET'])
def get_task():
    tasks = Task.query.order_by(Task.id.desc()).all()
    task_dict = [task.to_dict() for task in tasks]
    return jsonify(task_dict)

@api.route('/add', methods=['POST'])
def add_task():
    task = Task(
            title=request.form['title'],
            text=request.form['text']
            )
    db.session.add(task)
    db.session.commit()
    task = Task.query.order_by(Task.id.desc()).first()
    id = str(task.id)
    r = make_response(task.id)
    return r
