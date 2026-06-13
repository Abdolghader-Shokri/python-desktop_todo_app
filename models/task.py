from datetime import datetime


class Task:
    def __init__(self, title, completed=False, task_id=None):
        self.id = task_id or int(datetime.now().timestamp())
        self.title = title
        self.completed = completed
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def toggle(self):
        self.completed = not self.completed

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "completed": self.completed,
            "created_at": self.created_at
        }
