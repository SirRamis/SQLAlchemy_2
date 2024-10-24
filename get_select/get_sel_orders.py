from sqlalchemy import create_engine, text
from dotenv import load_dotenv

from connector.decorator_connect import db_url_creator

load_dotenv()


@db_url_creator
def get_sel_orders(url):
    engine = create_engine(url, echo=False)
    with engine.connect() as con:
        print("Подключение успешно!")
        result = con.execute(text("SELECT * FROM orders;"))
        orders = result.fetchall()

        for order in orders:
            print(order)

        print("Данные успешно получены.")


get_sel_orders()
