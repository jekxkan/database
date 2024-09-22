from connection import *

def putconn():
    """
    Отправляет объект соединения в пул соединений
    """
    postgresql_pool.putconn(connection)


def finaly():
    """
    Закрывает БД
    """
    if postgresql_pool:
        cursor.close()
        postgresql_pool.closeall()
        print("Connection closed")