from sqlalchemy import create_engine, text
from dotenv import load_dotenv

from connector.decorator_connect import db_url_creator

load_dotenv()


@db_url_creator
def update_client_data(url):
    engine = create_engine(url, echo=False)
    with engine.connect() as con:
        print("Подключение успешно!")

        # Обновим телефон клиента с id 1
        update_query = text('''
            UPDATE client
            SET phone = :new_phone
            WHERE id_client = :client_id;
        ''')

        # Пример обновления телефона клиента с id = 1
        con.execute(update_query, {'new_phone': 123456789, 'client_id': 1})

        con.commit()  # Подтверждаем изменения в базе данных
        print("Данные клиента успешно обновлены.")


update_client_data()
