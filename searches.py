from connection import connection

class Searches:
    """
    Класс с методами для поиска информации в БД
    """
    def search_by_name_and_surname(self, name: str, surname: str) -> [tuple]:
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


    def search_above_average_salary(self) -> [tuple]:
        """
        Выводит информацию о сотрудниках, чья зарплата выше среднего

        Returns:
            список кортежей, в которых содержится информация о сотрудниках с зарплатой выше среднего
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
                """
                SELECT *
                FROM employees
                WHERE salary > %s
                ORDER by id;
                """, (average_salary,)
            )
            return cursor.fetchall()


    def search_by_department(self, department: str) -> [tuple]:
        """
        Выводит сотрудников, которые работают в отделе

        Args:
            department(str): отдел

        Returns:
            список кортежей, в которых содержится информация о сотрудниках, работающих в отделе
        """
        with connection.cursor() as cursor:
            cursor.execute(
                """
                SELECT *
                FROM employees
                WHERE department = %s
                ORDER BY id;
                """, (department,)
            )
            return cursor.fetchall()