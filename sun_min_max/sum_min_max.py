from sqlalchemy import create_engine, text
from dotenv import load_dotenv
from connector.decorator_connect import db_url_creator

load_dotenv()


@db_url_creator
def get_aggregated_employee_data(url):
    engine = create_engine(url, echo=False)
    with engine.connect() as con:
        print("Подключение успешно!")

        result = con.execute(text("""
            SELECT COUNT(*) AS total_employees,
                   MAX(job_title) AS max_salary,
                   MIN(job_title) AS min_salary,
                   AVG(job_title) AS avg_salary
            FROM employees;
        """)).fetchall()  # Получаем результат запроса как список кортежей

        # Проход по строкам результата
        for row in result:
            print(f"Total Employees: {row[0]}")  # Доступ к данным через индексы
            print(f"Max Salary: {row[1]}")
            print(f"Min Salary: {row[2]}")
            print(f"Average Salary: {row[3]}")


get_aggregated_employee_data()
