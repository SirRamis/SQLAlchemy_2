from sqlalchemy import create_engine, text
from faker import Faker
from connector.decorator_connect import db_url_creator


fake = Faker()

@db_url_creator
def populate_products(url):
    engine = create_engine(url, echo=False)
    with engine.connect() as con:
        print("Подключение успешно!")


        for i in range(10):
            id_supply = fake.random_int(22, 31)
            name_of_product = fake.word()
            specification = fake.text(max_nb_chars=100)
            description = fake.text(max_nb_chars=200)
            image = bytes.fromhex('89504e470d0a1a0a0000000d49484452')
            purchase_cost = fake.random_int(min=100, max=10000)
            availability = fake.random_int(min=1, max=11)
            quantity = fake.random_int(min=1, max=100)
            selling_price = fake.random_int(min=500, max=15000)

            insert_query = text('''
                INSERT INTO products (id_supply, name_of_product, specification, description, image, purchase_cost,availability, quantity, selling_price) 
                VALUES (:id_supply, :name_of_product, :specification, :description, :image, :purchase_cost,:availability, :quantity, :selling_price);
            ''')


            con.execute(insert_query, {
                'id_supply': id_supply,
                'name_of_product': name_of_product,
                'specification': specification,
                'description': description,
                'image': image,
                'purchase_cost': purchase_cost,
                'availability': availability,
                'quantity': quantity,
                'selling_price': selling_price
            })
        con.commit()
        print("Данные успешно вставлены в таблицу Products.")

populate_products()
