import psycopg2


try:
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
        """
        Добавление нового сотрудника в БД

        Args:
            id(int) : уникальный id сотрудника
            first_name(str): имя сотрудника
            last_name(str): фамилия сотрудника
            age(int): возраст сотрудника
            department(str): подразделение, в котором работает сотрудник
            salary: зарплата сотрудника
        """
        with connection.cursor() as cursor:
            keys = 'id, first_name, last_name, age, department, salary'
            query = f"INSERT INTO employees({keys}) VALUES ({id}, '{first_name}', '{last_name}', {age}, '{department}', {salary});"
            cursor.execute(query, (id, first_name, last_name, age, department, salary))
except Exception as e:
    print(f"Error {e}")

finally:
    if connection:
        cursor.close()
        connection.close()
        print("Connection closed")
