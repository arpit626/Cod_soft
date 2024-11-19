import json
import os

# File to save tasks
TASK_FILE = "tasks.json"

# Function to load tasks from the file
def load_tasks():
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as file:
            return json.load(file)
    return []

# Function to save tasks to the file
def save_tasks(tasks):
    with open(TASK_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

# Display the menu
def display_menu():
    print("\nTo-Do List Application")
    print("-----------------------")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Task as Completed")
    print("6. Exit")

# Function to view tasks
def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks available!")
        return

    print("\nTasks:")
    for idx, task in enumerate(tasks, start=1):
        status = "✓" if task["completed"] else "✗"
        print(f"{idx}. {task['title']} [Status: {status}]")

# Function to add a task
def add_task(tasks):
    title = input("\nEnter the task title: ").strip()
    if title:
        tasks.append({"title": title, "completed": False})
        save_tasks(tasks)
        print("Task added successfully!")
    else:
        print("Task title cannot be empty!")

# Function to update a task
def update_task(tasks):
    view_tasks(tasks)
    try:
        task_no = int(input("\nEnter the task number to update: "))
        if 1 <= task_no <= len(tasks):
            new_title = input("Enter the new title: ").strip()
            if new_title:
                tasks[task_no - 1]["title"] = new_title
                save_tasks(tasks)
                print("Task updated successfully!")
            else:
                print("Task title cannot be empty!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

# Function to delete a task
def delete_task(tasks):
    view_tasks(tasks)
    try:
        task_no = int(input("\nEnter the task number to delete: "))
        if 1 <= task_no <= len(tasks):
            tasks.pop(task_no - 1)
            save_tasks(tasks)
            print("Task deleted successfully!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

# Function to mark a task as completed
def mark_task_completed(tasks):
    view_tasks(tasks)
    try:
        task_no = int(input("\nEnter the task number to mark as completed: "))
        if 1 <= task_no <= len(tasks):
            tasks[task_no - 1]["completed"] = True
            save_tasks(tasks)
            print("Task marked as completed!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

# Main program loop
def main():
    tasks = load_tasks()
    while True:
        display_menu()
        try:
            choice = int(input("\nEnter your choice: "))
            if choice == 1:
                view_tasks(tasks)
            elif choice == 2:
                add_task(tasks)
            elif choice == 3:
                update_task(tasks)
            elif choice == 4:
                delete_task(tasks)
            elif choice == 5:
                mark_task_completed(tasks)
            elif choice == 6:
                print("Exiting the application. Goodbye!")
                break
            else:
                print("Invalid choice! Please try again.")
        except ValueError:
            print("Please enter a valid number!")

if __name__ == "__main__":
    main()
