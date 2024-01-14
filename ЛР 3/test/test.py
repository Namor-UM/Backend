from jinja2 import Template


students = [
    {
        'name': 'Алина',
        'program': 'Бизнес-информатика',
        'subjects': ['База данных', 'Программирование', 'Статистика'],
        'gender': 'ж'
    },
    {
        'name': 'Вадим',
        'program': 'Экономика',
        'subjects': ['Информатика', 'Теория игр', 'Статистика'],
        'gender': 'м' 
    },
    {
        'name': 'Ксения',
        'program': 'Экономика',
        'subjects': ['Информатика', 'Теория игр', 'Статистика'],
        'gender': 'ж' 
    }
]

template_path = 'test_template.html'
f_template = open(template_path, 'r', encoding='utf-8-sig')
html = f_template.read()
f_template.close()

template = Template(html)

result_html = template.render(
    users = students,
    ind = 2
)

f = open('test.html', 'w', encoding='utf-8-sig')

f.write(result_html)
f.close()