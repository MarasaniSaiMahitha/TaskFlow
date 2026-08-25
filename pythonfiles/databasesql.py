import mysql.connector
conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Mahitha@22",
        database="taskflow_db"
    )
cursor = conn.cursor()