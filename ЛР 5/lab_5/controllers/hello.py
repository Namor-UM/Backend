from app import app
from flask import render_template, request
from . import constants


@app.route('/hello', methods=['GET'])


def hello():
    # для каждого передаваемого параметра формы нужно установить
    # значение по умолчание, на случай если пользователь ничего не введет
    name = ""
    gender = ""
    program_id = 0
    subjects_id = []
    subjects_select = []

    # получаем параметр из формы
    name = request.values.get('username')
    gender = request.values.get("gender")
    program_id = request.values.get("program")
    subject_id = request.values.getlist('subject[]')
    subjects_select = [constants.subjects[int(i)] for i in subject_id]

    html = render_template(
        'hello.html',
        name = name,
        gender = gender,
        program = constants.programs[int(program_id)],
        program_list = constants.programs,
        subjects_select = subjects_select,
        subjects_list = constants.subjects,
        len=len
    )
    return html