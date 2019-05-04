from typing import List
import json


class Task:
    def __init__(self, id: int = 0, text: str = "", done: bool = False):
        self.id: int = id
        self.text: str = text
        self.done: bool = done


def serialize_tasks(tasks: List[Task]) -> str:
    return json.dumps([t.__dict__ for t in tasks])


def deserialize_tasks(j: str) -> List[Task]:
    return [Task(**d) for d in json.loads(j)]


def serialize_task(task: Task) -> str:
    return json.dumps(task.__dict__)


def deserialize_task(j: str) -> Task:
    d: dict = json.loads(j)
    return Task(**d)
