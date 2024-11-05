class TodoList:
    class InvalidArgumentError(Exception):
        pass

    class InvalidStatusError(Exception):
        pass

    class Task:
        def __init__(self, id, description, status='todo'):
            self.id = id
            self.description = description
            self.status = status

    def __init__(self):
        self.tasks = {}
        self.next_id = 1
        self.valid_statuses = {'todo', 'inProgress', 'done'}

    def add_task(self, description, status='todo'):
        if not isinstance(description, str) or not description.strip():
            return "Error: INVALID_ARGUMENT (description cannot be empty)"
        if status is not None and not isinstance(status, str):
            return "Error: INVALID_ARGUMENT (status must be a string)"
        if status and status not in self.valid_statuses:
            return "Error: INVALID_STATUS"

        if status is None:
            status = 'todo'

        # Добавление задачи
        self.tasks[self.next_id] = self.Task(self.next_id, description, status)
        self.next_id += 1
        return "Task added successfully"

    def delete_task(self, id):
        if id in self.tasks:
            del self.tasks[id]
            return True
        return False

    def change_status(self, id, status):
        if id not in self.tasks:
            return "Error: TASK_NOT_FOUND"
        if status not in self.valid_statuses:
            return "Error: INVALID_STATUS"
        if self.tasks[id].status == status:
            return "Error: STATUS_ALREADY_SET"
        self.tasks[id].status = status
        return "Status changed successfully"

    def show_list(self):
        statuses = {'todo': [], 'inProgress': [], 'done': []}
        for task in self.tasks.values():
            statuses[task.status].append(f'{task.id} "{task.description}"')

        for status, tasks in statuses.items():
            print(f"{status.capitalize()}:")
            if tasks:
                print(",\n  ".join(tasks))
            else:
                print('-')


todo_list = TodoList()

print(todo_list.add_task('create a task'))
print(todo_list.add_task('make a bed', 'todo'))
print(todo_list.add_task('write a post', 'inProgress'))
print(todo_list.add_task(''))
print(todo_list.add_task('descr', None))

print(todo_list.change_status(1, 'done'))
print(todo_list.change_status(2, 'inProgress'))
print(todo_list.change_status(2, 'inProgress'))
print(todo_list.change_status(1, 'notTodo'))

print(todo_list.delete_task(2))
print(todo_list.delete_task(2))


todo_list.show_list()

