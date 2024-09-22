from connection import connection
from decimal import Decimal


def create_employee(id: int, first_name: str, last_name: str, age: int, department: str, salary: Decimal):
    """
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
        query = "INSERT INTO employees(id, first_name, last_name, age, department, salary) VALUES (%s, %s, %s, %s, %s, %s) COMMIT;"
        cursor.execute(query, (id, first_name, last_name, age, department, salary))
        cursor.execute('COMMIT;')

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
        return cursor.fetchall()  # можно заменить на fetchmany(), у которого можно указать, сколько строк выводить

def update_data_employee(id: int, dates: [dict]):
    """
    Обновляет данные сотрудника, принимая на вход его id и список из словарей {'column': 'value'}

    Args:
        id(int): уникальный id сотрудника
        dates([dict]): список словарей {'column': 'value'}
    """
    with connection.cursor() as cursor:
        # Проверка существует ли в БД пользователь с таким id
        cursor.execute(
           f"""
           SELECT id
           FROM employees
           WHERE id = %s;
           """, (id,)
        )
        if cursor.fetchone():
            for data in dates:
                for key, value in data.items():
                    # Обновление данных
                    update = f"UPDATE employees SET {key} = %s WHERE id = %s"
                    cursor.execute(update, (value, id,))
                    cursor.execute('COMMIT;')
        else:
            print("Сотрудника с таким id не существует")


def delete_employee(id: int):
    """
    Удаляет сотрудника из БД по его уникальному id

    Args:
        id(int): уникальный id сотрудника
    """
    with connection.cursor() as cursor:
        # Проверка существует ли в БД пользователь с таким id
        cursor.execute(
            f"""
            SELECT id
            FROM employees
            WHERE id = %s;
            """, (id,)
        )
        if cursor.fetchone():
            delete = "DELETE FROM employees WHERE id = %s;"
            cursor.execute(delete, (id,))
            cursor.execute('COMMIT;')
        else:
            print("Сотрудника с таким id не существует")