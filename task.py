class Task(object):
    id = 1

    def __init__(self, title, description):
        self.id = Task.id
        self.title = title
        self.description = description
        self.completed = False
        Task.id += 1