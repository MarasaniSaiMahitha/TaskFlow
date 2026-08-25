from pythonfiles.databasesql import conn, cursor


def register_user(user_name, first_name, last_name, email, password):

    if user_name == "":
        return False, "Username cannot be empty"

    if first_name == "":
        return False, "First name cannot be empty"

    query = """
    INSERT INTO users
    (user_name, first_name, last_name, email, password)
    VALUES (%s, %s, %s, %s, %s)
    """

    values = (
        user_name,
        first_name,
        last_name,
        email,
        password
    )

    try:
        cursor.execute(query, values)
        conn.commit()

        return True, "Registration Successful"

    except Exception as e:
        return False, str(e)