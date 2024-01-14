from app import app
from flask import render_template, request
from . import constants


@app.route('/index', methods=['GET'])
def index():
    action = ""
    inputs = ""
    x1, x2 = "", ""
    chosen_outputs = []

    if request.values.get('action') is not None:
        action = request.values.get('action')
        inputs = request.values.get('inputs')

        if request.values.get('x1') is not None:
            x1 = request.values.get("x1")
            x2 = request.values.get("x2")
            chosen_outputs = [constants.output_names[int(i)] for i in request.values.getlist("outputs")]

    html = render_template(
        "index.html",
        action = action,
        inputs = inputs,
        x1 = x1,
        x2 = x2,
        output_names = constants.output_names,
        output_funcs = constants.output_funcs,
        chosen_outputs = chosen_outputs,
        len = len)
    
    return html