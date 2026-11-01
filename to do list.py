
tasks = []

while True:
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter your task: ")
        tasks.append({"task": task, "completed": False})
        print("Task added successfully!")

    elif choice == "2":
        print("\nYour Tasks:")
        if not tasks:
            print("No tasks available.")
        for i, task in enumerate(tasks, start=1):
            status = "Completed" if task["completed"] else "Pending"
            print(i, ".", task["task"], "-", status)

    elif choice == "3":
        num = int(input("Enter task number: "))
        if 1 <= num <= len(tasks):
            tasks[num - 1]["completed"] = True
            print("Task completed!")
        else:
            print("Invalid task number.")

    elif choice == "4":
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            tasks.pop(num - 1)
            print("Task deleted!")
        else:
            print("Invalid task number.")

    elif choice == "5":
        print("Thank you for using To-Do List!")
        break

    else:
        print("Invalid choice. Try again.")
