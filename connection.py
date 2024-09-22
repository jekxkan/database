import psycopg2
from psycopg2 import pool

#Подключение к БД, предварительно созданной в SQL Shell, и создание пула соединений
postgresql_pool = psycopg2.pool.SimpleConnectionPool(1, 20,
    host = '127.0.0.1',
    user = 'postgres',
    password = 'zxcvb',
    database = 'company_db'
)

#Получаем соединение из пула соединений
connection = postgresql_pool.getconn()

cursor = connection.cursor()



