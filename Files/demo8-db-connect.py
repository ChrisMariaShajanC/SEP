import mysql.connector
conn=mysql.connector.connect(
    host='localhost',
    user='root',
    password='ChrisMySQL@2006',
    database='customer_db'
)
if conn.is_connected():
    print('Connected to MySQL database')
conn.close()
