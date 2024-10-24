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
        database=os.getenv("DB_NAME"),

    )

    engine = create_engine(url, echo=False)

    with engine.connect() as con:
        print("Подключение успешно!")
        res = con.execute(text("SELECT VERSION()"))
        print(f"{res.all()}")
except Exception as e:
    print(f"Ошибка подключения: {e}")
