import psycopg2

#Подключение к БД, предварительно созданной в SQL Shell
connection = psycopg2.connect(
    host = '127.0.0.1',
    user = 'postgres',
    password = 'zxcvb',
    database = 'company_db'
)
#Автоматическое внесение изменений в БД
connection.autocommit = True

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
def create_employee(id, first_name, last_name, age, department, salary):
    with connection.cursor() as cursor:
        query = "INSERT INTO employees(id, first_name, last_name, age, department, salary) VALUES (%s);"
        cursor.execute(query, (id, first_name, last_name, age, department, salary))
create_employee(1, 'sf', 'sdf', 4, 'sdf', 6)