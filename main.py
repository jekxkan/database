from searches import Searches
from service_functions import Service_functions
from disconnection import putconn, finaly
from create_table import create_table
from decimal import Decimal

if __name__ == '__main__':
    try:
        create_table()

        Service_functions.create_employee(0, 'Peter', 'Vnukov', 34, 'sales', Decimal(80000))
        Service_functions.create_employee(1, 'Sasha', 'Pupkin', 22, 'manager', Decimal(60000))
        Service_functions.create_employee(2, 'Lucia', 'Takayato', 19, 'robotics', Decimal(90000))
        print('Полный список сотрудников:', Service_functions.get_full_list_employees(3, 0))
        Service_functions.update_data_employee(0, [{'salary': Decimal(100000), 'first_name': 'Петя'}])
        print('Список с обновленнымии данными сотрудника 0:', Service_functions.get_full_list_employees(3, 0))
        print('Поиск сотрудника, являющегося меннеджером:', Searches.search_by_department('manager'))
        print('Поиск Пети Внукова:', Searches.search_by_name_and_surname('Петя', 'Vnukov'))
        print('Поиск у кого зарплата выше среднего:', Searches.search_above_average_salary())
        Service_functions.delete_employee(2)
        print('Список без удаленного сотрудника 2:', Service_functions.get_full_list_employees(3, 0))

        putconn()
    except Exception as e:
        print(f'Error {e}')

    finally:
        finaly()




