from sqlalchemy import create_engine, text, select, Table, MetaData
from dotenv import load_dotenv

from connector.decorator_connect import db_url_creator

load_dotenv()


@db_url_creator
def get_sel_products(url):
    engine = create_engine(url, echo=False)
    with engine.connect() as con:
        print("Подключение успешно!")
        metadata = MetaData()
        products = Table('products', metadata, autoload_with=engine)

        query = select(products)
        result = con.execute(query)


        for product in result:
            print(product)

        print("Данные успешно получены.")


get_sel_products()
