import sqlite3
import pandas as pd

pd.set_option('display.max_colwidth', 100)


def task_1(base):
    df = pd.read_sql(
        """
        SELECT room_name AS 'Номер', T.type_room_name AS 'Тип_номера', T.price AS 'Цена' FROM room
            NATURAL JOIN type_room T
            WHERE room_name LIKE '__09__' OR room_name LIKE '__10__'
            ORDER BY T.price, room_name
        """, base
        )

    print(df)


def task_2(base):
    df = pd.read_sql(
        """
        SELECT 'Количество гостей' AS 'Характеристика', COUNT(DISTINCT guest_id) AS 'Результат' FROM room_booking
        UNION ALL
        SELECT 'Количество номеров', COUNT(DISTINCT room_id) FROM room
        UNION ALL
        SELECT 'Сумма за проживание', SUM((julianday(check_out_date) - julianday(check_in_date)) * price) FROM room_booking
            NATURAL JOIN room
            NATURAL JOIN type_room
        UNION ALL
        SELECT 'Количество услуг', COUNT(DISTINCT service_id) FROM service     
        UNION ALL
        SELECT 'Сумма за услуги', SUM(price) FROM service_booking
        """, base)

    print(df)


def task_3(base):
    df = pd.read_sql(
        """
        WITH guest_data(guest_id, amount, type, max_amount) AS(
            SELECT guest_id, COUNT(*), GROUP_CONCAT(DISTINCT type_room_name) FROM room_booking
                NATURAL JOIN room
                NATURAL JOIN type_room
                GROUP BY guest_id
        )
        SELECT G.guest_name AS 'Гость', amount AS 'Количество', type AS 'Типы номеров'
            FROM guest G
            NATURAL JOIN guest_data
            GROUP BY 1
            ORDER BY 2 DESC, 1
        """, base
    )

    print(df)


def task_4(base):
    df = pd.read_sql(
        """
        SELECT type_room_name || ' ' || room_name || ' ' || check_in_date || '/' || check_out_date AS 'Пункт оплаты', 
            (julianday(check_out_date) - julianday(check_in_date)) * price AS 'Стоимость' FROM room_booking
            NATURAL JOIN room
            NATURAL JOIN type_room
            WHERE check_in_date == '2020-11-04' AND room_name == "С-0226"
        UNION
        SELECT service_name || ' ' || GROUP_CONCAT(service_start_date, ', '),
            SUM(price)
            FROM service_booking
            NATURAL JOIN service
            NATURAL JOIN room_booking
            NATURAL JOIN room
                WHERE check_in_date == '2020-11-04' AND room_name == "С-0226"
        """, base
    )

    print(df)


def task_5(base):
    df = pd.read_sql(
        """
        SELECT 
            strftime('%m', service_start_date) AS 'Месяц',
            service_start_date AS 'Дата',
            service_name AS 'Услуга',
            price AS 'Сумма',
            SUM(price) OVER part_by_date AS 'Сумма с накоплением'
            FROM service_booking
            NATURAL JOIN service
            WHERE strftime('%Y', service_start_date) = '2020'
        WINDOW part_by_date AS (
            PARTITION BY strftime('%m', service_start_date)
            ORDER BY service_start_date, service_name ASC
        )
        """, base
    )

    print(df)


if __name__ == '__main__':
    base = sqlite3.connect('booking.db')

    tasks = {'Задание №1': task_1, 
             'Задание №2': task_2, 
             'Задание №3': task_3, 
             'Задание №4' :task_4, 
             'Задание №5': task_5}
    for task_name in tasks:
        try:
            print(task_name)
            tasks[task_name](base)
        except Exception as xcept:
            print(f'Не выполнено из-за следующей ошибки: \n{str(xcept)}')
        finally:
            print('\n---//---//---//---\n')

    base.close()
