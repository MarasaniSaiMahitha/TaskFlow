import mysql.connector

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Mahitha@22",
        database="taskflow_db"
    )

    if conn.is_connected():
        print("MySQL Database Connected Successfully")

except mysql.connector.Error as error:
    print("Database Connection Failed:", error)

finally:
    if 'conn' in locals() and conn.is_connected():
        conn.close()
        print("Connection Closed")