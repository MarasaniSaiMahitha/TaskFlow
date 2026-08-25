from pythonfiles.databasesql import cursor

def get_dashboard_data(user_id):
    # Total tasks
    cursor.execute(
        "SELECT COUNT(*) FROM tasks WHERE user_id=%s",
        (user_id,)
    )
    total_tasks = cursor.fetchone()[0]

    # Pending tasks
    cursor.execute(
        "SELECT COUNT(*) FROM tasks WHERE user_id=%s AND status='Pending'",
        (user_id,)
    )
    pending_tasks = cursor.fetchone()[0]

    # Completed tasks
    cursor.execute(
        "SELECT COUNT(*) FROM tasks WHERE user_id=%s AND status='Completed'",
        (user_id,)
    )
    completed_tasks = cursor.fetchone()[0]

    # All tasks
    cursor.execute(
        """
        SELECT id, title, priority, due_date, status
        FROM tasks
        WHERE user_id=%s
        ORDER BY due_date
        """,
        (user_id,)
    )
    task_list = cursor.fetchall()

    return total_tasks, pending_tasks, completed_tasks, task_list