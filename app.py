import os
import json
from collections import Counter
from datetime import datetime

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.default_file = "tasks.json"

    @staticmethod
    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')

    def display_tasks(self):
        self.clear_screen()
        if not self.tasks:
            print("No tasks added yet.")
        else:
            print("Tasks:")
            for idx, task in enumerate(self.tasks, start=1):
                status = "Completed" if task["completed"] else "Pending"
                print(f"{idx}. {task['task']} - {status}")
                
    def show_task_details(self):
        self.clear_screen()
        self.display_tasks()
        if not self.tasks:
            print("No tasks to show details.")
            return

        try:
            task_index = int(input("Enter the task number to view details: ")) - 1
            if 0 <= task_index < len(self.tasks):
                task = self.tasks[task_index]
                print("Task Details:")
                print(f"Task: {task['task']}")
                print(f"Priority: {task.get('priority', 'Not set')}")
                print(f"Completed: {'Yes' if task['completed'] else 'No'}")
                reminder = task.get('reminder')
                if reminder:
                    print(f"Reminder: {reminder}")
                tags = task.get('tags')
                if tags:
                    print(f"Tags: {', '.join(tags)}")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid task number.")


    def add_task(self):
        self.clear_screen()
        task = input("Enter the task: ")
        self.tasks.append({"task": task, "completed": False})
        print("Task added successfully!")

    def mark_completed(self):
        self.display_tasks()
        if not self.tasks:
            print("No tasks to mark as completed.")
            return

        try:
            task_index = int(input("Enter the task number to mark as completed: ")) - 1
            if 0 <= task_index < len(self.tasks):
                self.tasks[task_index]["completed"] = True
                print("Task marked as completed!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid task number.")

    def remove_task(self):
        self.display_tasks()
        if not self.tasks:
            print("No tasks to remove.")
            return

        try:
            task_index = int(input("Enter the task number to remove: ")) - 1
            if 0 <= task_index < len(self.tasks):
                del self.tasks[task_index]
                print("Task removed successfully!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid task number.")

    def save_tasks_to_file(self):
        if not self.tasks:
            return

        default_choice = input(f"Do you want to save tasks to the default file '{self.default_file}'? (yes/no): ").lower()
        if default_choice == "yes":
            file_name = self.default_file
        else:
            file_name = input("Enter file name to save tasks (e.g., tasks.json): ")
        try:
            with open(file_name, "w") as file:
                json.dump(self.tasks, file)
            print("Tasks saved to file successfully!")
        except Exception as e:
            print(f"Error saving tasks to file: {e}")
    
    def load_tasks_from_file(self):
        file_name = input("Enter file name to load tasks from (e.g., tasks.json): ")
        try:
            with open(file_name, "r") as file:
                self.tasks = json.load(file)
            print("Tasks loaded from file successfully!")
        except FileNotFoundError:
            print("File not found.")
        except json.decoder.JSONDecodeError:
            print("Invalid JSON format in the file.")
        except Exception as e:
            print(f"Error loading tasks from file: {e}")

    def search_task(self):
        self.clear_screen()
        if not self.tasks:
            print("No tasks to search.")
            return

        search_term = input("Enter the task to search: ").lower()
        found_tasks = [task for task in self.tasks if search_term in task['task'].lower()]
        if found_tasks:
            print("Matching Tasks:")
            for idx, task in enumerate(found_tasks, start=1):
                status = "Completed" if task["completed"] else "Pending"
                print(f"{idx}. {task['task']} - {status}")
        else:
            print("No matching tasks found.")

    def sort_tasks(self):
        self.clear_screen()
        if not self.tasks:
            print("No tasks to sort.")
            return

        sorted_tasks = sorted(self.tasks, key=lambda x: x['task'].lower())
        self.tasks = sorted_tasks
        print("Tasks sorted successfully!")

    def display_statistics(self):
        self.clear_screen()
        if not self.tasks:
            print("No tasks added yet.")
            return

        task_statuses = [task['completed'] for task in self.tasks]
        task_counter = Counter(task_statuses)
        completed_tasks = task_counter[True]
        pending_tasks = task_counter[False]
        print(f"Completed Tasks: {completed_tasks}")
        print(f"Pending Tasks: {pending_tasks}")

    def clear_all_tasks(self):
        self.clear_screen()
        if not self.tasks:
            print("No tasks to clear.")
            return

        confirm_clear = input("Are you sure you want to clear all tasks? (yes/no): ").lower()
        if confirm_clear == "yes" or confirm_clear == "y" :
            self.tasks = []
            print("All tasks cleared successfully!")
        else:
            print("Operation cancelled.")

    def edit_task(self):
        self.display_tasks()
        if not self.tasks:
            print("No tasks to edit.")
            return

        try:
            task_index = int(input("Enter the task number to edit: ")) - 1
            if 0 <= task_index < len(self.tasks):
                new_task = input("Enter the new task: ")
                self.tasks[task_index]["task"] = new_task
                print("Task edited successfully!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid task number.")

    def view_completed_tasks(self):
        completed_tasks = [task for task in self.tasks if task["completed"]]
        if not completed_tasks:
            print("No completed tasks.")
        else:
            print("Completed Tasks:")
            for idx, task in enumerate(completed_tasks, start=1):
                print(f"{idx}. {task['task']}")

    def view_pending_tasks(self):
        pending_tasks = [task for task in self.tasks if not task["completed"]]
        if not pending_tasks:
            print("No pending tasks.")
        else:
            print("Pending Tasks:")
            for idx, task in enumerate(pending_tasks, start=1):
                print(f"{idx}. {task['task']}")

    def count_tasks(self):
        total_tasks = len(self.tasks)
        print(f"Total number of tasks: {total_tasks}")

    def undo_marked_task(self):
        self.display_tasks()
        if not self.tasks:
            print("No tasks to undo.")
            return

        try:
            task_index = int(input("Enter the task number to mark as pending again: ")) - 1
            if 0 <= task_index < len(self.tasks):
                self.tasks[task_index]["completed"] = False
                print("Task marked as pending again!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid task number.")
    
    def set_priority(self):
        self.display_tasks()
        if not self.tasks:
            print("No tasks to set priority.")
            return

        try:
            task_index = int(input("Enter the task number to set priority: ")) - 1
            if 0 <= task_index < len(self.tasks):
                priority = input("Enter priority level (Low/Medium/High): ").capitalize()
                if priority in ["Low", "Medium", "High"]:
                    self.tasks[task_index]["priority"] = priority
                    print("Priority set successfully!")
                else:
                    print("Invalid priority level. Please enter Low, Medium, or High.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid task number.")

    def show_task_details(self):
        self.display_tasks()
        if not self.tasks:
            print("No tasks to show details.")
            return

        try:
            task_index = int(input("Enter the task number to view details: ")) - 1
            if 0 <= task_index < len(self.tasks):
                task = self.tasks[task_index]
                print("Task Details:")
                print(f"Task: {task['task']}")
                print(f"Priority: {task.get('priority', 'Not set')}")
                print(f"Completed: {'Yes' if task['completed'] else 'No'}")
                # Add more details as needed (e.g., due date, tags, etc.)
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid task number.")

    def archive_tasks(self):
        completed_tasks = [task for task in self.tasks if task["completed"]]
        if not completed_tasks:
            print("No completed tasks to archive.")
            return

        archive_name = "archive.json"  
        try:
            with open(archive_name, "a") as file:
                for task in completed_tasks:
                    json.dump(task, file)
                    file.write("\n")
            print("Completed tasks archived successfully!")
        except Exception as e:
            print(f"Error archiving tasks: {e}")
    
    def set_reminder(self):
        self.display_tasks()
        if not self.tasks:
            print("No tasks to set reminders.")
            return

        try:
            task_index = int(input("Enter the task number to set a reminder: ")) - 1
            if 0 <= task_index < len(self.tasks):
                reminder_date = input("Enter the reminder date (YYYY-MM-DD): ")
                try:
                    reminder_datetime = datetime.strptime(reminder_date, "%Y-%m-%d")
                    self.tasks[task_index]["reminder"] = reminder_datetime.strftime("%Y-%m-%d")
                    print("Reminder set successfully!")
                except ValueError:
                    print("Invalid date format. Please enter in YYYY-MM-DD format.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid task number.")

    def set_task_tags(self):
        self.display_tasks()
        if not self.tasks:
            print("No tasks to add tags/categories.")
            return

        try:
            task_index = int(input("Enter the task number to add tags/categories: ")) - 1
            if 0 <= task_index < len(self.tasks):
                tags = input("Enter tags/categories separated by commas: ")
                tag_list = [tag.strip() for tag in tags.split(",")]
                self.tasks[task_index]["tags"] = tag_list
                print("Tags/categories added successfully!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid task number.")
    
    def show_menu(self):
        print("\nTask Manager")
        print("1. Add Task: Adds a new task to the list.")
        print("2. List Tasks: Displays the list of tasks.")
        print("3. Mark Task as Completed: Marks a task as completed.")
        print("4. Remove Task: Removes a task from the list.")
        print("5. Save Tasks to File: Saves tasks to a file.")
        print("6. Load Tasks from File: Loads tasks from a file.")
        print("7. Search Task: Searches for tasks containing a specific term.")
        print("8. Sort Tasks: Sorts tasks alphabetically.")
        print("9. Display Statistics: Displays statistics for completed and pending tasks.")
        print("10. Clear All Tasks: Clears all tasks.")
        print("11. Edit Task: Edits an existing task.")
        print("12. View Completed Tasks: Displays completed tasks.")
        print("13. View Pending Tasks: Displays pending tasks.")
        print("14. Count Tasks: Displays the total number of tasks.")
        print("15. Undo Marked Task: Reverts a completed task to pending.")
        print("16. Set Priority: Sets priority for a task.")
        print("17. Show Task Details: Displays detailed information about a task.")
        print("18. Set Reminder: Sets a reminder for a task.")
        print("19. Set Task Tags: Adds tags/categories to a task.")
        print("20. Archive Completed Tasks: Archives completed tasks.")
        print("21. Exit: Exits the Task Manager.")

    def start(self):
        while True:
            self.show_menu()
            choice = input("Enter your choice: ")

            match choice:
                case "1":
                    self.add_task()
                    print("Task added successfully!")
                case "2":
                    self.display_tasks()
                case "3":
                    self.mark_completed()
                    print("Task marked as completed!")
                case "4":
                    self.remove_task()
                    print("Task removed successfully!")
                case "5":
                    self.save_tasks_to_file()
                    print("Tasks saved to file successfully!")
                case "6":
                    self.load_tasks_from_file()
                    print("Tasks loaded from file successfully!")
                case "7":
                    self.search_task()
                case "8":
                    self.sort_tasks()
                    print("Tasks sorted successfully!")
                case "9":
                    self.display_statistics()
                case "10":
                    self.clear_all_tasks()
                    print("All tasks cleared successfully!")
                case "11":
                    self.edit_task()
                    print("Task edited successfully!")
                case "12":
                    self.view_completed_tasks()
                case "13":
                    self.view_pending_tasks()
                case "14":
                    self.count_tasks()
                case "15":
                    self.undo_marked_task()
                    print("Task marked as pending again!")
                case "16":
                    self.set_priority()
                    print("Priority set successfully!")
                case "17":
                    self.show_task_details()
                case "18":
                    self.set_reminder()
                case "19":
                    self.set_task_tags()
                case "20":
                    self.archive_tasks()
                case "21":
                    print("Exiting Task Manager. Goodbye!")
                    break
                case _:
                    self.clear_screen()
                    print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    task_manager = TaskManager()
    task_manager.start()