from connection import connection, cursor

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
        average_salary = list(cursor.fetchone())[0]
        cursor.execute(
            f"""
            SELECT *
            FROM employees
            WHERE salary > %s;
            """, (average_salary,)
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
            f"""
            SELECT *
            FROM employees
            WHERE department = %s;
            """, (department,)
        )
        return cursor.fetchall()