from sqlalchemy import create_engine, select, Table, MetaData
from sqlalchemy.engine import URL

try:
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
    metadata = MetaData()

    employees = Table('employees', metadata, autoload_with=engine)

    query = select(employees)
    result = connection.execute(query)

    for row in result:
        print(row)
except Exception as e:
    print(f"Ошибка подключения: {e}")