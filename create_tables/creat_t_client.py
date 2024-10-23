from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL
from dotenv import load_dotenv
import os

from decorator_connect import db_url_creator

load_dotenv()
@db_url_creator
def create_tab_employees(url):
    engine = create_engine(url, echo=False)
    with engine.connect() as con:
        print("Подключение успешно!")
        con.execute(text("""
            CREATE TABLE IF NOT EXISTS client (
                id SERIAL PRIMARY KEY ,
                full_name VARCHAR(50),
                address VARCHAR(255),
                phone BIGINT
            )
        """))
        con.commit()
        print("Таблицу создал.")

create_tab_employees()