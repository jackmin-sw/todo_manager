from datetime import datetime

class Task:
    def __init__(self, title, description, priority, due_date, status="pending"):
        self.title = title
        self.description = description
        self.priority = priority  # 1（低）到5（高）
        self.due_date = datetime.strptime(due_date, "%Y-%m-%d")
        self.status = status
        self.created_at = datetime.now()

    def mark_complete(self):
        self.status = "completed"

    def to_dict(self):
        return {
            "title": self.title,
            "description": self.description,
            "priority": self.priority,
            "due_date": self.due_date.strftime("%Y-%m-%d"),
            "status": self.status,
            "created_at": self.created_at.strftime("%Y-%m-%d %H:%M:%S")
        }

    def __str__(self):
        return f"{self.title} (Priority: {self.priority}, Due: {self.due_date.strftime('%Y-%m-%d')}, Status: {self.status})"