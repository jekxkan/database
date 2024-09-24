import psycopg2
from psycopg2 import pool

#Подключение к БД после docker-compose
postgresql_pool = psycopg2.pool.SimpleConnectionPool(1, 20,
    host = 'localhost',
    user = 'admin',
    port = '5432',
    password = 'root',
    dbname = 'company_db'
)

#Получаем соединение из пула соединений
connection = postgresql_pool.getconn()

cursor = connection.cursor()



