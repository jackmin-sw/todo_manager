import unittest
from src.task import Task
from src.database import TaskDatabase
import os

class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.db = TaskDatabase("test_tasks.db")
        self.task = Task("Test Task", "Description", 3, "2025-12-31")

    def test_task_creation(self):
        self.assertEqual(self.task.title, "Test Task1")
        self.assertEqual(self.task.status, "pending")

    def test_mark_complete(self):
        self.task.mark_complete()
        self.assertEqual(self.task.status, "completed")

    def test_add_task_to_db(self):
        self.db.add_task(self.task)
        tasks = self.db.get_all_tasks()
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0].title, "Test Task")

    def tearDown(self):
        os.remove("test_tasks.db")

if __name__ == "__main__":
    unittest.main()