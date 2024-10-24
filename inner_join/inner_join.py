from sqlalchemy import create_engine, text
from dotenv import load_dotenv

from connector.decorator_connect import db_url_creator

load_dotenv()


@db_url_creator
def perform_joins(url):
    engine = create_engine(url, echo=False)
    with engine.connect() as con:
        print("Подключение успешно!")

        # 1. Получаем заказы вместе с информацией о сотрудниках
        result = con.execute(text('''
            SELECT orders.id_order, employees.family, employees.name, employees.surname, orders.posting_date
            FROM orders
            INNER JOIN employees ON orders.id_employee = employees.id_employee;
        '''))
        orders_with_employees = result.fetchall()
        print("Заказы и сотрудники:")
        for row in orders_with_employees:
            print(row)

        print("\n")

        # 2. Получаем продукты и их поставщиков
        result = con.execute(text('''
            SELECT products.name_of_product, provider.name_of_provider
            FROM products
            INNER JOIN supply ON products.id_supply = supply.id_supply
            INNER JOIN provider ON supply.id_provider = provider.id_provider;
        '''))
        products_with_providers = result.fetchall()
        print("Продукты и их поставщики:")
        for row in products_with_providers:
            print(row)

        print("\n")

        # 3. Получаем заказы вместе с информацией о клиентах
        result = con.execute(text('''
            SELECT orders.id_order, client.full_name, orders.posting_date
            FROM orders
            INNER JOIN client ON orders.id_client = client.id_client;
        '''))
        orders_with_clients = result.fetchall()
        print("Заказы и клиенты:")
        for row in orders_with_clients:
            print(row)


perform_joins()
