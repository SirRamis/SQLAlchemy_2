from sqlalchemy import create_engine, text
from faker import Faker
from connector.decorator_connect import db_url_creator


fake = Faker()

@db_url_creator
def insert_inside_provider(url):
    engine = create_engine(url, echo=False)
    with engine.connect() as con:
        print("Подключение успешно!")


        for i in range(10):
            name_of_provider = fake.text(max_nb_chars=5)
            representative = fake.text(max_nb_chars=5)
            speak_to = fake.text(max_nb_chars=5)
            phone = fake.random_number(digits=9)
            address = fake.address().replace("\n", ", ")

            insert_query = text('''
                INSERT INTO provider (name_of_provider, representative, speak_to, phone, address) 
                VALUES (:name_of_provider, :representative, :speak_to, :phone, :address);
            ''')


            con.execute(insert_query, {
                'name_of_provider': name_of_provider,
                'representative': representative,
                'speak_to': speak_to,
                'phone': phone,
                'address': address,
            })
        con.commit()
        print("Данные успешно вставлены в таблицу.")

insert_inside_provider()
