"""
Created on Wed Jan  1 20:40:17 2025
Author: @csesohag02
GitHub: https://github.com/csesohag02
"""

import json

# File to store tasks
tasks_file = "tasks.json"

# Load tasks from file or initialize an empty list
def load_tasks():
    try:
        with open(tasks_file, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save tasks to file
def save_tasks(tasks):
    with open(tasks_file, "w") as file:
        json.dump(tasks, file, indent=4)

# Add a new task
def add_task(description):
    tasks = load_tasks()
    tasks.append({"description": description, "completed": False})
    save_tasks(tasks)
    print(f"Task added: {description}")

# List all tasks
def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks available.")
    else:
        for i, task in enumerate(tasks, start=1):
            status = "Done" if task["completed"] else "Pending"
            print(f"{i}. {task['description']} [{status}]")

# Mark a task as completed
def mark_task_done(task_number):
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1]["completed"] = True
        save_tasks(tasks)
        print(f"Task {task_number} marked as done.")
    else:
        print("Invalid task number.")

# Delete a task
def delete_task(task_number):
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        save_tasks(tasks)
        print(f"Task deleted: {removed_task['description']}")
    else:
        print("Invalid task number.")

# Main menu
def main():
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option: ")
        if choice == "1":
            description = input("Enter task description: ")
            add_task(description)
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            try:
                task_number = int(input("Enter task number to mark as done: "))
                mark_task_done(task_number)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "4":
            try:
                task_number = int(input("Enter task number to delete: "))
                delete_task(task_number)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


"""
Created and maintained by @csesohag02
GitHub: https://github.com/csesohag02
"""
