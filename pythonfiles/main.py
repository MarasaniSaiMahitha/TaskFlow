from pythonfiles.register import register
from pythonfiles.login import login
from pythonfiles.addtask import add_task
from pythonfiles.viewtask import view_task
from pythonfiles.edittask import edit_task
from pythonfiles.deletetask import delete_task

while True:

    print("\n" + "=" * 40)
    print("       TASKFLOW MANAGEMENT")
    print("=" * 40)
    print("1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter your choice: ")
    if choice == "1":
        register()
    elif choice == "2":

        logged_user = login()

        if logged_user:

            user_id = logged_user[0]
            user_name = logged_user[2]
            while True:

                print("\n" + "=" * 40)
                print(f"Welcome {user_name}")
                print("=" * 40)
                print("1. Add Task")
                print("2. View Tasks")
                print("3. Edit Task")
                print("4. Delete Task")
                print("5. Logout")

                option = input("Enter your choice: ")

                if option == "1":
                    add_task(user_id)

                elif option == "2":
                    view_task(user_id)

                elif option == "3":
                    edit_task(user_id)

                elif option == "4":
                    delete_task(user_id)

                elif option == "5":
                    print("\nLogged Out Successfully.")
                    break
                elif option == "6":
                    print("\nThank you for using TaskFlow.")
                    exit()
                else:
                    print("\nInvalid Choice.")
                    
    elif choice == "3":
        print("\nThank you for using TaskFlow.")
        break

    else:
        print("\nInvalid Choice.")