from pythonfiles.databasesql import conn, cursor

def delete_task(user_id):
    print("==== Delete Your Task ====")

    task_id = input("Enter Task ID to delete: ")


    query = """
    SELECT * FROM tasks
    WHERE id = %s AND user_id = %s;
    """

    values = (task_id, user_id)

    cursor.execute(query, values)
    task = cursor.fetchone()

    if task is None:
        print("\nTask not found.")
        return


    print("-" * 30)
    print("Task ID      :", task[0])
    print("Title        :", task[2])
    print("Description  :", task[3])
    print("Due Date     :", task[4])
    print("Priority     :", task[5])
    print("Status       :", task[6])
    print("-" * 30)

    choice = input("Are you sure you want to delete this task? (Y/N): ")

    if choice.upper() == "Y":

        query = """
        DELETE FROM tasks
        WHERE id = %s;
        """

        values = (task_id,)

        cursor.execute(query, values)
        conn.commit()

        print("\nTask Deleted Successfully.")

    else:
        print("\nDeletion Cancelled.")


