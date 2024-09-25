from connection import connection
from decimal import Decimal


def check_if_employee_exists(id: int) -> bool:
    """
    Проверяет существует ли в БД сотрудник с таким id

    Args:
        id(int): id сотрудника

    Returns:
        bool: True - если сотрудник с таким id существует, иначе False
    """
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT
            EXISTS(SELECT 1
            FROM employees
            WHERE id = %s);
            """, (id,)
                       )
        return cursor.fetchone()[0]


class Service_functions:
    """
    Класс с методами для сервисной работы с БД
    """
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
            if not(check_if_employee_exists(id)):
                query = "INSERT INTO employees(id, first_name, last_name, age, department, salary) VALUES (%s, %s, %s, %s, %s, %s)"
                cursor.execute(query, (id, first_name, last_name, age, department, salary))
                connection.commit()
            #else:
                #print('Сотрудник с таким id уже существует')

    def get_full_list_employees(per_page: int, offset: int) -> [tuple]:
        """
        Печатает список всех сотрудников

        Args:
            per_page(int): сколько строк вывести
            offset(int): сколько строк пропустить от начала списка и затем начать выводить строки
        Return:
            list of tuples - список кортежей с данными о сотрудниках
        """
        with connection.cursor() as cursor:
            cursor.execute(
                """ 
                SELECT * 
                FROM employees
                ORDER BY id
                LIMIT %s OFFSET %s;
                """, (per_page, offset,))
            return cursor.fetchall()

    def update_data_employee(id: int, dates: [dict]):
        """
        Обновляет данные сотрудника, принимая на вход его id и список из словарей {'column': 'value'}

        Args:
            id(int): уникальный id сотрудника
            dates([dict]): список словарей {'column': 'value'}
        """
        with connection.cursor() as cursor:
            if check_if_employee_exists(id):
                for data in dates:
                    for key, value in data.items():
                        # Обновление данных
                        update = f"UPDATE employees SET {key} = %s WHERE id = %s"
                        cursor.execute(update, (value, id,))
                        connection.commit()
            else:
                print('Сотрудника с таким id не существует')

    def delete_employee(id: int):
        """
        Удаляет сотрудника из БД по его уникальному id

        Args:
            id(int): уникальный id сотрудника
        """
        with connection.cursor() as cursor:
            if check_if_employee_exists(id):
                delete = "DELETE FROM employees WHERE id = %s;"
                cursor.execute(delete, (id,))
                connection.commit()
            else:
                print('Сотрудника с таким id не существует')


