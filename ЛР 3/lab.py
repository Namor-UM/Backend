from jinja2 import Template
import math


def length(cur_list):
    return len(cur_list)


def is_correct_amount(n):
    return n == int(n) and n > 0

def ceiled(n):
    return math.ceil(n)


if __name__ == '__main__':
    f_template = open('template.html', 'r', encoding='utf-8-sig')
    html = f_template.read()
    f_template.close()

    template = Template(html)

    template.globals['length'] = length
    template.globals['is_correct_amount'] = is_correct_amount
    template.globals['ceiled'] = ceiled

    result_html = template.render(
        radio_list = ['Синий', 'Зелёный', 'Красный'],
        checked_num = 1,
        group_name = 'color',
        table_list = [
            {"title" : "Мастер и Маргарита", "author": "Булгаков М.А.", "price": 581.50},
            {"title" : "Белая гвардия","author": "Булгаков М.А.", "price": 600.00},
            {"title" : "Война и мир", "author": "Толстой Л.Н.", "price": 899.99},
            {"title" : "Анна Каренина", "author": "Толстой Л.Н.", "price": 450.10},
            {"title" : "Игрок", "author": "Достоевский Ф.М.", "price":  234.55}
        ],
        n = 5
    )

    f = open('lab.html', 'w', encoding='utf-8-sig')
    f.write(result_html)
    f.close()