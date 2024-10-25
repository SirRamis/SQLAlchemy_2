from sqlalchemy import create_engine, text
from dotenv import load_dotenv

from connector.decorator_connect import db_url_creator

load_dotenv()


@db_url_creator
def get_filtered_employee_data(url):
    engine = create_engine(url, echo=False)
    with engine.connect() as con:
        print("Подключение успешно!")

        # Пример запроса с WHERE, ORDER BY, GROUP BY, DISTINCT
        select_query = text('''
            SELECT DISTINCT name, surname, job_title, COUNT(*) as employee_count
            FROM employees
            WHERE birthday > '1985-01-01'  -- Условие фильтрации по дате рождения
            GROUP BY name, surname, job_title  -- Группировка по имени, фамилии и должности
            HAVING COUNT(*) > 1  -- Фильтр после группировки, чтобы выбрать те, у кого больше одного совпадения
            ORDER BY surname ASC, name DESC;  -- Сортировка по фамилии (по возрастанию) и имени (по убыванию)
        ''')

        result = con.execute(select_query)

        # Вывод результатов запроса
        for row in result:
            print(
                f"Name: {row['name']}, Surname: {row['surname']}, Job Title: {row['job_title']}, Employee Count: {row['employee_count']}")


get_filtered_employee_data()
