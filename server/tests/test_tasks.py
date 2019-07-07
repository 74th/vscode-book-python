from typing import List
import unittest
from model import tasks


class TestTasks(unittest.TestCase):
    def test_serialize_task(self):
        task = tasks.Task(100, "task1", True)

        j = tasks.serialize_task(task)
        self.assertGreater(len(j), 0)

        result = tasks.deserialize_task(j)
        self.assertEqual(task.id, result.id)
        self.assertEqual(task.text, result.text)
        self.assertEqual(task.done, result.done)

    def test_serialize_tasks(self):
        task1 = tasks.Task(0, "task1", False)
        task2 = tasks.Task(100, "task2", True)
        task_list: List[tasks.Task] = [task1, task2]

        j = tasks.serialize_tasks(task_list)
        self.assertGreater(len(j), 0)

        result = tasks.deserialize_tasks(j)
        self.assertEqual(len(result), 2)
        self.assertEqual(task1.id, result[0].id)
        self.assertEqual(task1.text, result[0].text)
        self.assertEqual(task1.done, result[0].done)
        self.assertEqual(task2.id, result[1].id)
        self.assertEqual(task2.text, result[1].text)
        self.assertEqual(task2.done, result[1].done)
