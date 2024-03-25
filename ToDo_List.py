class Task:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.done = False

    def completed(self):
        self.done = True

    def incomplete(self):
        self.done = False

    def edit_task(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        status = 'Completed' if self.done else 'Incomplete'
        return f'Task {self.name}\nDescription: {self.description}\nStatus: {status}'
class ToDO_List:
    def __init__(self):
        self.task_list = []

    def add_task(self, task):
        self.task_list.append(task)

    def remove_task(self, task):
        self.task_list.remove(task)

    def complete_tasks(self):
        return [task for task in self.task_list if task.completed]

    def incomplete_tasks(self):
        return [task for task in self.task_list if task.incompleted]