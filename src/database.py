import sqlite3
from .task import Task

class TaskDatabase:
    def __init__(self, db_name="tasks.db"):
        self.db_name = db_name
        self._init_db()

    def _init_db(self):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS tasks (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    description TEXT,
                    priority INTEGER,
                    due_date TEXT,
                    status TEXT,
                    created_at TEXT
                )
            """)
            conn.commit()

    def add_task(self, task):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO tasks (title, description, priority, due_date, status, created_at)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (
                task.title,
                task.description,
                task.priority,
                task.due_date.strftime("%Y-%m-%d"),
                task.status,
                task.created_at.strftime("%Y-%m-%d %H:%M:%S")
            ))
            conn.commit()

    def get_all_tasks(self):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM tasks")
            rows = cursor.fetchall()
            tasks = []
            for row in rows:
                task = Task(
                    title=row[1],
                    description=row[2],
                    priority=row[3],
                    due_date=row[4],
                    status=row[5]
                )
                tasks.append(task)
            return tasks

    def update_task_status(self, task_id, status):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE tasks SET status = ? WHERE id = ?", (status, task_id))
            conn.commit()