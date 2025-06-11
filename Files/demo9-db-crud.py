import mysql.connector
def connect():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='ChrisMySQL@2006',
        database='customer_db',
        port=3306
    )
def create_customer(name, email, phone,city):
    conn = connect()
    cursor = conn.cursor()
    sql = "INSERT INTO customers (name, email, phone, city) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (name, email, phone, city))
    conn.commit()
    print(f"Customer {name} created successfully.")
    cursor.close()
    conn.close()
    