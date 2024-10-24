from sqlalchemy import create_engine, text
from faker import Faker
from connector.decorator_connect import db_url_creator


fake = Faker()

@db_url_creator
def insert_inside_orders(url):
    engine = create_engine(url, echo=False)
    with engine.connect() as con:
        print("Подключение успешно!")


        for i in range(10):
            id_employee = fake.random_int(21, 30)
            id_product = fake.random_int(3, 13)
            id_client = fake.random_int(1, 10)
            posting_date = fake.date()
            execution_date = fake.date()



            insert_query = text('''
                INSERT INTO orders (id_employee, id_product, id_client, posting_date, execution_date) 
                VALUES (:id_employee, :id_product, :id_client, :posting_date, :execution_date);
            ''')


            con.execute(insert_query, {
                'id_employee': id_employee,
                'id_product': id_product,
                'id_client': id_client,
                'posting_date': posting_date,
                'execution_date': execution_date,
            })
        con.commit()
        print("Данные успешно вставлены в таблицу Products.")

insert_inside_orders()
