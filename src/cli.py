from .task import Task
from .database import TaskDatabase
from .api import WeatherAPI

def main():
    db = TaskDatabase()
    weather_api = WeatherAPI("YOUR_API_KEY")  # 替换为你的API密钥
    while True:
        print("\n1. Add Task\n2. View Tasks\n3. Complete Task\n4. Get Weather\n5. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            title = input("Title: ")
            description = input("Description: ")
            priority = int(input("Priority (1-5): "))
            due_date = input("Due date (YYYY-MM-DD): ")
            task = Task(title, description, priority, due_date)
            db.add_task(task)
            print("Task added!")
        elif choice == "2":
            tasks = db.get_all_tasks()
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
        elif choice == "3":
            task_id = int(input("Task ID to complete: "))
            db.update_task_status(task_id, "completed")
            print("Task marked as completed!")
        elif choice == "4":
            city = input("Enter city: ")
            print(weather_api.get_weather(city))
        elif choice == "5":
            break

if __name__ == "__main__":
    main()