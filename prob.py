from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL
from dotenv import load_dotenv
import os


load_dotenv()

try:

    url = URL.create(
        drivername=os.getenv("DB_DRIVER"),
        username=os.getenv("DB_USERNAME"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        database=os.getenv("DB_NAME2"),
    )

    engine = create_engine(url, echo=False)

    with engine.connect() as con:
        print("Подключение успешно!")
        con.execute(text("""
            CREATE TABLE IF NOT EXISTS employees (
                id SERIAL PRIMARY KEY,
                family VARCHAR(50),
                name VARCHAR(50),
                surname VARCHAR(50),  
                job_title INT,
                address VARCHAR(255),
                home_phone BIGINT,
                birthday DATE
            )
        """))
        print("Таблица успешно создана или уже существует.")
except Exception as e:
    print(f"Ошибка подключения: {e}")
