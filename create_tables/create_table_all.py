from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL
from dotenv import load_dotenv
import os
from decorator_connect import db_url_creator


load_dotenv()

@db_url_creator
def create_tables(url):
    engine = create_engine(url, echo=False)
    with engine.connect() as con:
        print("Подключение успешно!")
        con.execute(text("""
            CREATE TABLE IF NOT EXISTS Provider (
                id_provider SERIAL PRIMARY KEY,
                name_of_provider VARCHAR(50) NOT NULL,
                representative TEXT NOT NULL,
                speak_to TEXT NOT NULL,
                phone BIGINT NOT NULL,
                address TEXT NOT NULL
            );
        """))
        con.execute(text("""
            CREATE TABLE IF NOT EXISTS Supply (
                id_supply SERIAL PRIMARY KEY,
                id_provider INT REFERENCES Provider(id_provider),
                data_of_supply DATE NOT NULL
            );
        """))
        con.execute(text("""
            CREATE TABLE IF NOT EXISTS Products (
                id_product SERIAL PRIMARY KEY,
                id_supply INT REFERENCES Supply(id_supply),
                name_of_product TEXT NOT NULL,
                specification TEXT,
                description TEXT,
                image BYTEA,
                purchase_cost INT,
                availability INT,
                quantity INT,
                selling_price INT
            );
        """))
        con.execute(text("""
            CREATE TABLE IF NOT EXISTS Employees (
                id_employee SERIAL PRIMARY KEY,
                family VARCHAR(50) NOT NULL,
                name VARCHAR(50) NOT NULL,
                surname VARCHAR(50) NOT NULL,
                job_title INT,
                address TEXT NOT NULL,
                home_phone BIGINT NOT NULL,
                birthday DATE NOT NULL
            );
        """))
        con.execute(text("""
            CREATE TABLE IF NOT EXISTS Client (
                id_client SERIAL PRIMARY KEY,
                full_name VARCHAR(50) NOT NULL,
                address TEXT NOT NULL,
                phone BIGINT NOT NULL
            );
        """))
        con.execute(text("""
            CREATE TABLE IF NOT EXISTS Orders (
                id_order SERIAL PRIMARY KEY,
                id_employee INT REFERENCES Employees(id_employee),
                id_product INT REFERENCES Products(id_product),
                id_client INT REFERENCES Client(id_client),
                posting_date DATE,
                execution_date DATE
            );
        """))
        con.commit()
        print("Базовые таблицы успешно созданы.")


create_tables()
