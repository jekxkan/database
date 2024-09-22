from searches import search_by_department, search_by_name_and_surname, search_above_average_salary
from service_functions import create_employee, get_full_list_employees, delete_employee, update_data_employee
import connection
from disconection import putconn, finaly
from create_table import create_table
from decimal import Decimal

if __name__ == '__main__':
    try:
        create_table()



        putconn()
    except Exception as e:
        print(f'Error {e}')

    finally:
        finaly()




