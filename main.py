from searches import Searches
from service_functions import Service_functions
from disconnection import putconn, finaly
from create_table import create_table
from decimal import Decimal


class All_functions(Service_functions, Searches):
    """
    Создаем класс с методами классов Searches, Service_functions при помощи многокрастного наследования
    """
    def __init__(self):
        pass


if __name__ == '__main__':
    try:
        create_table()

        table = All_functions()
        table.create_employee(0, 'Peter', 'Vnukov', 34, 'sales', Decimal(80000))
        table.create_employee(1, 'Sasha', 'Pupkin', 22, 'manager', Decimal(60000))
        table.create_employee(2, 'Lucia', 'Takayato', 19, 'robotics', Decimal(90000))
        print('Полный список сотрудников:', table.get_full_list_employees(3, 0))

        table.update_data_employee(0, [{'salary': Decimal(100000), 'first_name': 'Петя'}])
        print('Список с обновленнымии данными сотрудника 0:', table.get_full_list_employees(3, 0))

        print('Поиск сотрудника, являющегося менеджером:', table.search_by_department('manager'))
        print('Поиск Пети Внукова:', table.search_by_name_and_surname('Петя', 'Vnukov'))
        print('Поиск у кого зарплата выше среднего:', table.search_above_average_salary())

        table.delete_employee(2)
        print('Список без удаленного сотрудника 2:', table.get_full_list_employees(3, 0))

        putconn()
    except Exception as e:
        print(f'Error {e}')

    finally:
        finaly()




