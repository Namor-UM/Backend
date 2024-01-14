from app import app
from flask import render_template, request
from . import constants


@app.route('/index', methods=['GET'])
def index():
    name = ""
    gender = ""
    program_id = 0
    subjects_id = []
    subjects_select = []
    action=""

    if request.values.get('username') is not None:
        name = request.values.get('username')
        gender = request.values.get("gender")
        program_id = request.values.get("program")
        subject_id = request.values.getlist('subject[]')
        subjects_select = [constants.subjects[int(i)] for i in subject_id]
        action = request.values.get("action")
    

    html = render_template(
        'index.html',
        name = name,
        gender = gender,
        program = constants.programs[int(program_id)],
        program_list=constants.programs,
        subjects_select = subjects_select,
        subjects_list = constants.subjects,
        action = action,
        len = len)
    return html