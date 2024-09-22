from connection import connection, cursor

def create_table():
    with connection.cursor() as cursor:
        "Создание таблицы работников"

        cursor.execute(
            """CREATE TABLE IF NOT EXISTS employees(
                id SERIAL PRIMARY KEY,
                first_name VARCHAR(50),
                last_name VARCHAR(50),
                age INT,
                department VARCHAR(50),
                salary NUMERIC);
            """
        )

        # Индексируем колонки first_name, last_name, department в таблице employees для увеличения производительности
        cursor.execute(
            """
            CREATE INDEX IF NOT EXISTS index_name_surname
            ON employees(first_name, last_name);
            """
        )
        cursor.execute(
            """
            CREATE INDEX IF NOT EXISTS index_department
            ON employees(department);
            """
        )