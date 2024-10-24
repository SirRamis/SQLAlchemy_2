from sqlalchemy import create_engine, text
from faker import Faker
from connector.decorator_connect import db_url_creator


fake = Faker()

@db_url_creator
def insert_inside_supply(url):
    engine = create_engine(url, echo=False)
    with engine.connect() as con:
        print("Подключение успешно!")


        for i in range(10):
            id_provider = fake.random_int(1, 11)
            data_of_supply = fake.date()



            insert_query = text('''
                INSERT INTO supply (id_provider, data_of_supply) 
                VALUES (:id_provider, :data_of_supply);
            ''')


            con.execute(insert_query, {
                'id_provider': id_provider,
                'data_of_supply': data_of_supply,
            })
        con.commit()
        print("Данные успешно вставлены в таблицу Products.")

insert_inside_supply()
