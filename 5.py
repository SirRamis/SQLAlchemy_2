from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from dotenv import load_dotenv
import os

# Загрузка переменных окружения из .env файла
load_dotenv()

try:
    url = URL.create(
        drivername=os.getenv("DB_DRIVER"),
        username=os.getenv("DB_USERNAME"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        database=os.getenv("DB_NAME")
    )

    engine = create_engine(url)
    connection = engine.connect()
    print("Подключение успешно!")

except Exception as e:
    print(f"Ошибка подключения: {e}")
