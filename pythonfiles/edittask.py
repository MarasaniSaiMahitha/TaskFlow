from pythonfiles.databasesql import conn, cursor

def edit_task(user_id):
    print("==== Edit Your Task ====")

    task_id = input("Enter Task Id to edit : ")

    query = """SELECT * FROM tasks
    WHERE id = %s"""
    values = (task_id,)
    cursor.execute(query, values)
    task = cursor.fetchone()
    if task is None:
        print("Task not found")
    else:
                print("-" * 30)
                print("Task ID      :", task[0])
                print("Title        :", task[2])
                print("Description  :", task[3])
                print("Due Date     :", task[4])
                print("Priority     :", task[5])
                print("-" * 30)

    title = input("Enter New title: ")
    description = input("Enter New description: ")
    due_date = input("Enter New due date: ")
    priority = input("Enter New priority: ")

    query = """
    UPDATE tasks 
    SET 
        title = %s,
        description = %s,
        due_date = %s,
        priority = %s
    WHERE id = %s """
    values = (
            title,
            description,
            due_date,
            priority,
            task_id
    )
    try:
        cursor.execute(query, values)
        conn.commit()
        print("\nTask Updated Successfully.")
    except Exception as e:
            print("Update Failed:", e)
