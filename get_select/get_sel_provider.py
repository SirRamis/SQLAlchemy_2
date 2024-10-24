from sqlalchemy import create_engine, text
from dotenv import load_dotenv

from connector.decorator_connect import db_url_creator

load_dotenv()


@db_url_creator
def get_sel_provider(url):
    engine = create_engine(url, echo=False)
    with engine.connect() as con:
        print("Подключение успешно!")
        result = con.execute(text("SELECT * FROM provider;"))
        providers = result.fetchall()

        for provider in providers:
            print(provider)

        print("Данные успешно получены.")


get_sel_provider()
