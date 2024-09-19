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
            salary(int/float): зарплата сотрудника
        """
        with connection.cursor() as cursor:
            keys = 'id, first_name, last_name, age, department, salary'
            query = f"INSERT INTO employees({keys}) VALUES ({id}, '{first_name}', '{last_name}', {age}, '{department}', {salary});"
            cursor.execute(query, (id, first_name, last_name, age, department, salary))

    def get_full_list_employees():
        """
        Печатает список всех сотрудников

        Return:
            list of tuples - список кортежей с данными о сотрудниках
        """

        with connection.cursor() as cursor:
            cursor.execute(
                """SELECT * 
                   FROM employees
                   ORDER BY id;
                """)
            print(cursor.fetchall())
    get_full_list_employees()
    def update_data_employee(id, *new_data):
        """
        Обновляет данные сотрудника, принимая на вход его id и новые значения вида 'column: value'

        Args:
            id(int): уникальный id сотрудника
            *new_data: пара столбец: значение
        """

        with connection.cursor() as cursor:
            #Проверка существует ли в БД пользователь с таким id
            cursor.execute(
               f"""SELECT id
               FROM employees
               WHERE id = {id};"""
            )
            if cursor.fetchone():

                #Создаем массив, в котором будут списки, состоящие из пар столбец-новое значение
                new_data = [[pair.split(':')[0].strip(), pair.split(':')[1].strip()] for pair in new_data]
                for i in range(len(new_data)):
                    update = f"UPDATE employees SET {new_data[i][0]} = '{new_data[i][1]}' WHERE id = {id};"
                    cursor.execute(update)
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
               f"""SELECT id
               FROM employees
               WHERE id = {id};"""
            )
            if cursor.fetchone():
                delete = f'DELETE FROM employees WHERE id = {id};'
                cursor.execute(delete)
            else:
                print("Сотрудника с таким id не существует")



except Exception as e:
    print(f"Error {e}")

finally:
    if connection:
        cursor.close()
        connection.close()
        print("Connection closed")
