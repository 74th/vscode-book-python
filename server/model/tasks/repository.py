from typing import List
from .tasks import Task


class Repository:
    def __init__(self):
        self._tasks: List[Task] = [Task(1, "task1", False), Task(2, "task2", False)]

    def list(self) -> List[Task]:
        return list(filter(lambda t: not t.done, self._tasks))

    def add(self, task: Task) -> int:
        task.id = len(self._tasks) + 1
        self._tasks.append(task)
        return task.id

    def done(self, id: int):
        for t in self._tasks:
            if t.id == id:
                t.done = True
