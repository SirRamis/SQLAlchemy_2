from sqlalchemy import create_engine, text
from dotenv import load_dotenv
from faker import Faker
from connector.decorator_connect import db_url_creator

# Загрузка переменных окружения
load_dotenv()

# Инициализация Faker для генерации данных
fake = Faker()

@db_url_creator
def insert_inside(url):
    engine = create_engine(url, echo=False)
    with engine.connect() as con:
        print("Подключение успешно!")

        # Вставка 10 строк с фейковыми данными в таблицу Employees
        for i in range(10):
            family = fake.first_name()
            name = fake.first_name()
            surname = fake.last_name()
            job_title = fake.random_int(min=100000, max=999999)
            address = fake.address().replace("\n", ", ")  # Заменяем перенос строки запятой
            home_phone = fake.random_number(digits=9)
            birthday = fake.date_of_birth(minimum_age=18, maximum_age=65).strftime('%Y-%m-%d')

            insert_query = text('''
                INSERT INTO employees (family, name, surname, job_title, address, home_phone, birthday) 
                VALUES (:family, :name, :surname, :job_title, :address, :home_phone, :birthday);
            ''')

            # Выполняем вставку данных
            con.execute(insert_query, {
                'family': family,
                'name': name,
                'surname': surname,
                'job_title': job_title,
                'address': address,
                'home_phone': home_phone,
                'birthday': birthday
            })

        con.commit()
        print("Данные успешно вставлены в таблицу Employees.")

insert_inside()
