from pythonfiles.databasesql import conn, cursor


def add_task(user_id, title, description, due_date, priority):

    query = """
    INSERT INTO tasks
    (user_id, title, description, due_date, priority)
    VALUES (%s, %s, %s, %s, %s)
    """

    values = (
        user_id,
        title,
        description,
        due_date,
        priority
    )

    try:
        cursor.execute(query, values)
        conn.commit()

        return True, "Task Added Successfully"

    except Exception as e:
        return False, str(e)