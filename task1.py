import pickle
import os

TASKS_FILE = 'tasks.pkl'

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'rb') as file:
            return pickle.load(file)
    return {}

def save_tasks(tasks):
    with open(TASKS_FILE, 'wb') as file:
        pickle.dump(tasks, file)

def add_task(tasks, task):
    task_id = len(tasks) + 1
    tasks[task_id] = task
    print(f"Task added with ID: {task_id}")

def update_task(tasks, task_id, new_task):
    if task_id in tasks:
        tasks[task_id] = new_task
        print(f"Task {task_id} updated.")
    else:
        print("Task ID not found.")

def delete_task(tasks, task_id):
    if task_id in tasks:
        del tasks[task_id]
        print(f"Task {task_id} deleted.")
    else:
        print("Task ID not found.")

def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        for task_id, task in tasks.items():
            print(f"ID: {task_id}, Task: {task}")

def main():
    tasks = load_tasks()
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. Update Task")
        print("3. Delete Task")
        print("4. View Tasks")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            task = input("Enter the task description: ")
            add_task(tasks, task)
            save_tasks(tasks)
        elif choice == '2':
            task_id = int(input("Enter the task ID to update: "))
            new_task = input("Enter the new task description: ")
            update_task(tasks, task_id, new_task)
            save_tasks(tasks)
        elif choice == '3':
            task_id = int(input("Enter the task ID to delete: "))
            delete_task(tasks, task_id)
            save_tasks(tasks)
        elif choice == '4':
            view_tasks(tasks)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
