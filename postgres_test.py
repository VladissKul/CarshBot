import psycopg2

try:
    conn = psycopg2.connect(dbname='test_db', user='postgres', password='9414', host='127.0.0.1')
except:
    print('Can`t establish connection to database')

cursor = conn.cursor()
cursor.execute('SELECT * FROM employee')
all_users = cursor.fetchone()
print(all_users)
cursor.close()  # закрываем курсор
conn.close()  # закрываем соединение
