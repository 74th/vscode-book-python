from typing import List
import unittest
from model import todo


class TestRepository(unittest.TestCase):

    def test_list(self):
        rep = todo.Repository()

        l = rep.list()
        self.assertEqual(len(l), 2)
        self.assertNotEqual(l[0].id, l[1].id)
        self.assertNotEqual(l[0].text, l[1].text)
        self.assertEqual(l[0].done, False)
        self.assertEqual(l[1].done, False)

        rep._tasks[0].done = True
        l = rep.list()
        self.assertEqual(len(l), 1)
        self.assertEqual(l[0].id, 2)
        self.assertEqual(l[0].done, False)

    def test_add(self):
        rep = todo.Repository()

        task = todo.Task(100, "new task")
        rep.add(task)

        l = rep.list()

        self.assertEqual(len(l), 3)
        self.assertEqual(l[2].id, 3)
        self.assertEqual(l[2].text, "new task")
        self.assertEqual(l[2].done, False)

    def test_done(self):
        rep = todo.Repository()

        rep.done(1)

        l = rep.list()
        self.assertEqual(len(l), 1)
        self.assertEqual(l[0].id, 2)
        self.assertEqual(l[0].done, False)