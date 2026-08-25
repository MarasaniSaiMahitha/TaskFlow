from pythonfiles.databasesql import conn, cursor


def login_user(user_name, password):

    query = """
    SELECT * FROM users
    WHERE user_name = %s
    """

    values = (user_name,)

    try:
        cursor.execute(query, values)

        user = cursor.fetchone()

        if user is None:
            return False, "User does not exist.", None

        if password == user[5]:
            return True, f"Welcome {user[2]}!", user

        return False, "Invalid Password.", None

    except Exception as e:
        return False, str(e), None