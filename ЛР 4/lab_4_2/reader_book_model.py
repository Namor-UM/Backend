from pandas import read_sql


def get_reader(conn):
    return read_sql("SELECT * FROM reader", conn)


def get_book_reader(conn, reader_id):
    return read_sql(
        f'''
        SELECT 
            title as "Название книги", 
            GROUP_CONCAT(author_name, ", ") as "Авторы", 
            borrow_date as "Дата выдачи", 
            return_date as "Дата возврата"
            FROM book_reader
        NATURAL JOIN book
        NATURAL JOIN book_author
        NATURAL JOIN author
        WHERE reader_id = {reader_id}
        GROUP BY title
        ''', conn
    )