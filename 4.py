from sqlalchemy import create_engine
from sqlalchemy.engine import URL

try:
    # Создание URL с правильными параметрами
    url = URL.create(
        drivername="postgresql+psycopg2",  # Обязательно строка
        username="postgres",
        password="171217",
        host="localhost",
        port=5432,
        database="Store_1"
    )
    engine = create_engine(url)  # Создание движка с URL
    connection = engine.connect()  # Подключение к базе данных
    print("Подключение успешно!")

    # Пример простого запроса (проверьте синтаксис SQL)
    result = connection.execute("SELECT * FROM employees")
    for row in result:
        print(row)

except Exception as e:
    print(f"Ошибка подключения: {e}")
