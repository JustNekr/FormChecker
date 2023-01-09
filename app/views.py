from flask import request, jsonify
from tinydb import TinyDB

from app import app
from test_requests import run_test
from utils import type_form, form_checker


@app.route("/get_form", methods=['POST'])
def form_analyzer():
    db = TinyDB('db.json')
    typed_form = None
    result = None
    if request.method == 'POST':
        data = request.args
        typed_form = type_form(data)
        result = form_checker(db, typed_form)
    if result:
        return result
    else:
        return typed_form


@app.route("/db_all")
def db_test():
    db = TinyDB("db.json")
    info = db.all()
    return jsonify(info)


@app.route("/test")
def test():
    result = run_test()
    return jsonify(result)
