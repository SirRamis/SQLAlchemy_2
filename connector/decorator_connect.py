from sqlalchemy.engine import URL
from dotenv import load_dotenv
import os

load_dotenv()

def db_url_creator(func):
    def wrapper(*args):
        url = URL.create(
            drivername=os.getenv("DB_DRIVER"),
            username=os.getenv("DB_USERNAME"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            database=os.getenv("DB_NAME2"),
        )
        return func(url, *args)
    return wrapper
@db_url_creator
def connect_to_db(url):
    print(f"URL для подключения: {url}")

connect_to_db()
