"""
To-Do List Application
Module 7B Final Project
This command-line app allows users to add, view, and delete tasks.
"""

tasks = []

def show_menu():
    """Displays the main menu options to the user."""
    print("\n TO-DO LIST MENU")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Quit")

def add_task():
    """Prompts the user to enter a task and adds it to the list if valid."""
    task = input("Enter the task to add: ").strip()
    if task:
        tasks.append(task)
        print(f"Task added: '{task}'")
    else:
        print("Task cannot be empty.")

def view_tasks():
    """Displays all current tasks or notifies the user if the list is empty."""
    if not tasks:
        print("No tasks to show.")
    else:
        print("\n Your Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def delete_task():
    """Allows the user to delete a task by its number in the list."""
    if not tasks:
        print("No tasks to delete.")
        return

    view_tasks()
    try:
        index = int(input("Enter the number of the task to delete: "))
        if 1 <= index <= len(tasks):
            removed = tasks.pop(index - 1)
            print(f"Task deleted: '{removed}'")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    """Main function to run the To-Do List app with user interaction loop."""
    print("\nWelcome to the To-Do List App! ")
    while True:
        show_menu()
        try:
            choice = input("\nChoose an option (1-4): ").strip()
            if choice == "1":
                add_task()
            elif choice =="2":
                view_tasks()
            elif choice == "3":
                delete_task()
            elif choice == "4":
                print("Exiting the app. Goodbye!")
                break
            else:
                print("Invalid selection. Please choose 1, 2, 3, or 4.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        finally:
            print("---")

if __name__ == "__main__":
    main()      