# импортируем необходимые модули
from jinja2 import Template
import sqlite3
from library_model import get_table

# устанавливаем соединение с базой данных (базу данных взять из ЛР 1)
conn = sqlite3.connect("library.db")

# выбираем записи из таблицы publisher
df_publisher = get_table(conn, 'publisher')
df_genre = get_table(conn, 'genre')

# закрываем соединение с базой
conn.close()

# открываем шаблон из файла library_templ.html и читаем информацию
f_template = open('library_temp.html', 'r')
html = f_template.read()
f_template.close()

# создаем объект-шаблон
template = Template(html)

# генерируем результат на основе шаблона
result_html = template.render(
    tables = {
        "publisher": df_publisher,
        "genre": df_genre
    },
    len = len
)

#создаем файл для HTML-страницы
f = open('library.html', 'w', encoding ='utf-8-sig')

# выводим сгенерированную страницу в файл
f.write(result_html)
f.close()