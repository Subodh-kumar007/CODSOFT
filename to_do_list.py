class ToDoList:
    def __init__(self):
        self.tasks = {}

    def add_task(self, task):
        task_id = len(self.tasks) + 1
        self.tasks[task_id] = {'task': task, 'completed': False}
        print(f"Task added: {task} (ID: {task_id})")

    def update_task(self, task_id, updated_task):
        if task_id in self.tasks:
            self.tasks[task_id]['task'] = updated_task
            print(f"Task updated: {updated_task} (ID: {task_id})")
        else:
            print(f"Task ID {task_id} not found.")

    def complete_task(self, task_id):
        if task_id in self.tasks:
            self.tasks[task_id]['completed'] = True
            print(f"Task ID {task_id} marked as completed.")
        else:
            print(f"Task ID {task_id} not found.")

    def delete_task(self, task_id):
        if task_id in self.tasks:
            deleted_task = self.tasks.pop(task_id)
            print(f"Task deleted: {deleted_task['task']} (ID: {task_id})")
        else:
            print(f"Task ID {task_id} not found.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            for task_id, details in self.tasks.items():
                status = "Completed" if details['completed'] else "Pending"
                print(f"ID: {task_id}, Task: {details['task']}, Status: {status}")

def main():
    todo_list = ToDoList()
    while True:
        print("To-Do List Application")
        print("1. Add Task")
        print("2. Update Task")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. View Tasks")
        print("6. Exit")
        choice = input("Enter your choice (1/2/3/4/5/6): ")

        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == '2':
            task_id = int(input("Enter the task ID to update: "))
            updated_task = input("Enter the updated task: ")
            todo_list.update_task(task_id, updated_task)
        elif choice == '3':
            task_id = int(input("Enter the task ID to mark as completed: "))
            todo_list.complete_task(task_id)
        elif choice == '4':
            task_id = int(input("Enter the task ID to delete: "))
            todo_list.delete_task(task_id)
        elif choice == '5':
            todo_list.view_tasks()
        elif choice == '6':
            print("Exiting the To-Do List application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
