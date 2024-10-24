from sqlalchemy import create_engine, text
from dotenv import load_dotenv
from faker import Faker
from connector.decorator_connect import db_url_creator

load_dotenv()
fake = Faker()

@db_url_creator
def insert_inside(url):
    engine = create_engine(url, echo=False)
    with engine.connect() as con:
        print("Подключение успешно!")
        for i in range(10):
            full_name = fake.name()
            address = fake.address().replace("\n", ", ")  # Заменяем перенос строки запятой
            phone = fake.random_number(digits=9)

            insert_query = text('''
                INSERT INTO client (full_name, address, phone) 
                VALUES (:full_name, :address, :phone);
            ''')

            con.execute(insert_query, {
                'full_name': full_name,
                'address': address,
                'phone': phone,
            })

        con.commit()
        print("Данные успешно вставлены в таблицу.")

insert_inside()
