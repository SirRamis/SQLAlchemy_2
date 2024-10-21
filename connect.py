from sqlalchemy import create_engine, select, Table, MetaData
from sqlalchemy.engine import URL

url = URL.create(
        drivername="postgresql+psycopg2",
        username="postgres",
        password="171217",
        host="localhost",
        port=5432,
        database="Store_1"
    )
engine = create_engine(url)
connection = engine.connect()
print("Подключение успешно!")