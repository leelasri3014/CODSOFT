import os

# Function to display the menu
def display_menu():
    print("\n===== To-Do List App =====")
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Mark Task as Done")
    print("4. Clear Completed Tasks")
    print("5. Exit")

# Function to view the to-do list
def view_todo_list():
    if os.path.exists("todo.txt"):
        with open("todo.txt", "r") as file:
            tasks = file.readlines()
            if tasks:
                print("\n=== To-Do List ===")
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task.strip()}")
            else:
                print("\nYour to-do list is empty.")
    else:
        print("\nYour to-do list is empty.")

# Function to add a task to the to-do list
def add_task():
    task = input("\nEnter the task: ")
    with open("todo.txt", "a") as file:
        file.write(task + "\n")
    print("Task added successfully!")

# Function to mark a task as done
def mark_task_done():
    view_todo_list()
    tasks = read_tasks_from_file()
    if tasks:
        try:
            task_number = int(input("\nEnter the task number to mark as done: "))
            if 1 <= task_number <= len(tasks):
                tasks[task_number - 1] = f"[Done] {tasks[task_number - 1]}"
                write_tasks_to_file(tasks)
                print("Task marked as done!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input. Please enter a valid task number.")
    else:
        print("No tasks to mark as done.")

# Function to clear completed tasks
def clear_completed_tasks():
    tasks = read_tasks_from_file()
    if tasks:
        tasks = [task for task in tasks if not task.startswith("[Done]")]
        write_tasks_to_file(tasks)
        print("Completed tasks cleared.")
    else:
        print("No tasks to clear.")

# Function to read tasks from the file
def read_tasks_from_file():
    if os.path.exists("todo.txt"):
        with open("todo.txt", "r") as file:
            return file.readlines()
    return []

# Function to write tasks to the file
def write_tasks_to_file(tasks):
    with open("todo.txt", "w") as file:
        file.writelines(tasks)

# Main function
def main():
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-5): ")
        if choice == "1":
            view_todo_list()
        elif choice == "2":
            add_task()
        elif choice == "3":
            mark_task_done()
        elif choice == "4":
            clear_completed_tasks()
        elif choice == "5":
            print("Exiting the To-Do List App. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()