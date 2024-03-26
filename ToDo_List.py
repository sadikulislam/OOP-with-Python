class Task:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def mark_incomplete(self):
        self.completed = False

    def edit_task(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        status = 'Completed' if self.completed else 'Incomplete'
        return f'Task {self.name}\nDescription: {self.description}\nStatus: {status}'


class ToDo_List:
    def __init__(self):
        self.task_list = []

    def add_tasks(self, task):
        self.task_list.append(task)

    def remove_task(self, index):
        try:
            del self.task_list[index]
            print("Task removed.")
        except IndexError:
            print("Invalid task index.")

    def mark_task_completed(self, index, completed=True):
        try:
            task = self.task_list[index]
            task.completed = completed
            print("Task marked as completed." if completed else "Task marked as incomplete.")
        except IndexError:
            print("Invalid task index.")

    def edit_task(self, index, name, description):
        try:
            task = self.task_list[index]
            task.name = name
            task.description = description
            print("Task edited.")
        except IndexError:
            print("Invalid task index.")

    def display_tasks(self):
        if len(self.task_list) == 0:
            print("No tasks found")
        else:
            for index, task in enumerate(self.task_list):
                print(f"{index}. {task}")
        print()


t1 = ToDo_List()
t1.add_tasks(Task("Task1", "I have to complete task1"))
t1.add_tasks(Task("Task2", "I have to complete task within 2 days"))
t1.display_tasks()

t1.mark_task_completed(0)

t1.edit_task(0,"Update task 1", "Task completed.")
t1.mark_task_completed(0)
t1.display_tasks()
t1.remove_task(0)
t1.display_tasks()