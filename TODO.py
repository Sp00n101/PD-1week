class TodoList:
    class InvalidArgumentError(Exception):
        def __init__(self, argument):
            super().__init__(f"INVALID_ARGUMENT: '{argument}' is not valid.")
            self.argument = argument

    class InvalidStatusError(Exception):
        def __init__(self, status):
            super().__init__(f"INVALID_STATUS: '{status}' is not a valid status.")
            self.status = status

    class TaskNotFoundError(Exception):
        def __init__(self, task_id):
            super().__init__(f"TASK_NOT_FOUND: No task found with ID '{task_id}'.")
            self.task_id = task_id

    class StatusAlreadySetError(Exception):
        def __init__(self, status):
            super().__init__(f"STATUS_ALREADY_SET: Task status is already '{status}'.")
            self.status = status

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
            raise self.InvalidArgumentError(description)
        if status is not None and not isinstance(status, str):
            raise self.InvalidArgumentError(status)
        if status and status not in self.valid_statuses:
            raise self.InvalidStatusError(status)

        if status is None:
            status = 'todo'

        self.tasks[self.next_id] = self.Task(self.next_id, description, status)
        self.next_id += 1
        return "Task added successfully"

    def delete_task(self, id):
        if id not in self.tasks:
            raise self.TaskNotFoundError(id)
        del self.tasks[id]
        return "Task deleted successfully"

    def change_status(self, id, status):
        if id not in self.tasks:
            raise self.TaskNotFoundError(id)
        if status not in self.valid_statuses:
            raise self.InvalidStatusError(status)
        if self.tasks[id].status == status:
            raise self.StatusAlreadySetError(status)
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

try:
    print(todo_list.add_task('create a task'))
    print(todo_list.add_task('make a bed', 'todo'))
    print(todo_list.add_task('write a post', 'inProgress'))
    print(todo_list.add_task(''))
except TodoList.InvalidArgumentError as e:
    print(e)

try:
    print(todo_list.add_task('descr', None))
except TodoList.InvalidArgumentError as e:
    print(e)

try:
    print(todo_list.change_status(1, 'done'))
    print(todo_list.change_status(2, 'inProgress'))
    print(todo_list.change_status(2, 'inProgress'))
except (TodoList.TaskNotFoundError, TodoList.InvalidStatusError, TodoList.StatusAlreadySetError) as e:
    print(e)

try:
    print(todo_list.change_status(1, 'notTodo'))
except (TodoList.TaskNotFoundError, TodoList.InvalidStatusError, TodoList.StatusAlreadySetError) as e:
    print(e)

try:
    print(todo_list.delete_task(2))
    print(todo_list.delete_task(2))
except TodoList.TaskNotFoundError as e:
    print(e)

todo_list.show_list()