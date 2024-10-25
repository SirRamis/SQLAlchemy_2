from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

from connector.decorator_connect import db_url_creator

load_dotenv()

@db_url_creator
def delete_and_select_providers(url):
    engine = create_engine(url, echo=False)
    with engine.connect() as con:
        print("Подключение успешно!")

        # Удаляем записи из таблицы supply, которые ссылаются на provider с id меньше 5
        delete_supply_query = text("DELETE FROM supply WHERE id_provider < 5;")
        con.execute(delete_supply_query)

        # Затем удаляем записи из provider
        delete_provider_query = text("DELETE FROM provider WHERE id_provider < 5;")
        con.execute(delete_provider_query)

        # Получаем оставшиеся данные в provider
        select_query = text("SELECT * FROM provider;")
        result = con.execute(select_query)

        print("Оставшиеся строки в таблице 'provider':")
        for row in result:
            print(row)

delete_and_select_providers()
