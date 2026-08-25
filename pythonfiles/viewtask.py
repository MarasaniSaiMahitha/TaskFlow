from pythonfiles.databasesql import conn, cursor

def view_task(user_id):
    print("=== Your Task ===")

    query = """
    SELECT * FROM tasks WHERE user_id = %s
    """
    values = (user_id,)
    cursor.execute(query, values)
    tasks = cursor.fetchall()
    for task in tasks:
        print("-" * 30)
        print("Task ID      :", task[0])
        print("Title        :", task[2])
        print("Description  :", task[3])
        print("Due Date     :", task[4])
        print("Priority     :", task[5])
        print("-" * 30)
