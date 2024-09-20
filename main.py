import psycopg2
from decimal import Decimal
from psycopg2 import pool

try:
    #Подключение к БД, предварительно созданной в SQL Shell, и создание пула соединений
    postgresql_pool = psycopg2.pool.SimpleConnectionPool(1, 20,
        host = '127.0.0.1',
        user = 'postgres',
        password = 'zxcvb',
        database = 'company_db'
    )
    #Получаем соединение из пула соединений
    connection = postgresql_pool.getconn()

    #Автоматическое внесение изменений в БД
    #connection.autocommit = True

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


        #Индексируем колонки first_name, last_name, department в таблице employees для увеличения производительности
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

    def create_employee(id: int, first_name: str, last_name: str, age: int, department: str, salary: Decimal):
        """#прописать return
        Добавление нового сотрудника в БД

        Args:
            id(int) : уникальный id сотрудника
            first_name(str): имя сотрудника
            last_name(str): фамилия сотрудника
            age(int): возраст сотрудника
            department(str): подразделение, в котором работает сотрудник
            salary(Decimal): зарплата сотрудника
        """
        with connection.cursor() as cursor:
            query = "INSERT INTO employees(id, first_name, last_name, age, department, salary) VALUES (%(int)s, %(str)s, %(str)s, %(int)s, %(str)s, %(Decimal)s);"
            cursor.execute(query, (id, first_name, last_name, age, department, salary))

    def get_full_list_employees():
        """
        Печатает список всех сотрудников

        Return:
            list of tuples - список кортежей с данными о сотрудниках
        """
        with connection.cursor() as cursor:
            cursor.execute(
                """ 
                SELECT * 
                FROM employees
                ORDER BY id;
                """)
            return cursor.fetchall() #добавить флаг,,,
    get_full_list_employees()
    def update_data_employee(id: int, *new_data):
        """
        Обновляет данные сотрудника, принимая на вход его id и новые значения вида 'column: value'

        Args:
            id(int): уникальный id сотрудника
            *new_data: пара 'столбец: значение'
        """
        with connection.cursor() as cursor:
            #Проверка существует ли в БД пользователь с таким id
            cursor.execute(
               f"""
               SELECT id
               FROM employees
               WHERE id = {id};
               """
            )
            if cursor.fetchone():
                #Создаем массив, в котором будут списки, состоящие из пар столбец-новое значение
                new_data = [[pair.split(':')[0].strip(), pair.split(':')[1].strip()] for pair in new_data] #передать dict
                for i in range(len(new_data)):
                    update = "UPDATE employees SET '%s' = '%s' WHERE id = %s;"
                    cursor.execute(update, (new_data[i][0], new_data[i][1]), id)
            else:
                print("Сотрудника с таким id не существует")

    def delete_employee(id: int):
        """
        Удаляет сотрудника из БД по его уникальному id

        Args:
            id(int): уникальный id сотрудника
        """
        with connection.cursor() as cursor:
            #Проверка существует ли в БД пользователь с таким id
            cursor.execute(
                """
                SELECT id
                FROM employees
                WHERE id = %s;
                """, id #Error 'int' object does not support indexing
            )
            if cursor.fetchone():
                delete = "DELETE FROM employees WHERE id = %s;"
                return cursor.execute(delete, id)
            else:
                print("Сотрудника с таким id не существует")

#SELECTS
    def search_by_name_and_surname(name: str, surname: str):
        """
        Выводит информацию о сотруднике по имени и фамилии

        Args:
            name(str): имя сотрудника
            surname(str): фамилия сотруника

        Returns:
            список кортежей, в которых содержится информация о сотрудниках с введенными именем и фамилией
        """
        with connection.cursor() as cursor:
            cursor.execute(
                """
                SELECT * 
                FROM employees
                WHERE first_name = %s 
                AND last_name = %s;
                """, (name, surname)
            )
            return cursor.fetchall()

    def search_above_average_salary():
        """
        Выводит информацию о сотрудниках, чья зарплата выше среднего

        """
        with connection.cursor() as cursor:
            cursor.execute(
                """
                SELECT AVG(salary)
                FROM employees;
                """
            )
            average_salary = cursor.fetchone()[0]
            cursor.execute(
                """
                SELECT *
                FROM employees
                WHERE salary > %s;
                """, (average_salary)
            )
            return cursor.fetchall()

    def search_by_department(department: str):
        """
        Выводит сотрудников, которые работают в отделе

        Args:
            department(str): отдел
        """
        with connection.cursor() as cursor:
            cursor.execute(
                """
                SELECT *
                FROM employees
                WHERE department = %s;
                """, (department)
            )
            return cursor.fetchall()


    #Отправляем объект соединения в пул соединений
    postgresql_pool.putconn(connection)


except Exception as e:
    print(f"Error {e}")

finally:
    if postgresql_pool:
        cursor.close()
        postgresql_pool.closeall()
        print("Connection closed")
