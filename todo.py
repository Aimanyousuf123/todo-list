print("📋 Welcome to To-Do List App")

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Exit")

    choice = input("Choose an option (1/2/3/4): ")

    if choice == "1":
        task = input("Enter new task: ")
        with open("tasks.txt", "a") as file:
            file.write(task + "\n")
        print("✅ Task added.")

    elif choice == "2":
        try:
            with open("tasks.txt", "r") as file:
                tasks = file.readlines()
                if not tasks:
                    print("No tasks yet.")
                else:
                    print("\nYour Tasks:")
                    for idx, task in enumerate(tasks, start=1):
                        print(f"{idx}. {task.strip()}")
        except FileNotFoundError:
            print("Task file not found.")

    elif choice == "3":
        try:
            with open("tasks.txt", "r") as file:
                tasks = file.readlines()

            if not tasks:
                print("No tasks to complete.")
                continue

            print("\nTasks:")
            for idx, task in enumerate(tasks, start=1):
                print(f"{idx}. {task.strip()}")

            task_num = int(input("Enter task number to mark as complete: "))

            if 1 <= task_num <= len(tasks):
                tasks.pop(task_num - 1)
                with open("tasks.txt", "w") as file:
                    file.writelines(tasks)
                print("✅ Task completed and removed.")
            else:
                print("Invalid task number.")
        except FileNotFoundError:
            print("Task file not found.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid option. Try again.")
