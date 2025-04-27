from flask import Flask, request, render_template,redirect
from .database import TaskDatabase
from .task import Task

app = Flask(__name__)
db = TaskDatabase()

@app.route("/")
def index():
    tasks = db.get_all_tasks()
    return render_template("index.html", tasks=tasks)

@app.route("/add", methods=["POST"])
def add_task():
    title = request.form["title"]
    description = request.form["description"]
    priority = int(request.form["priority"])
    due_date = request.form["due_date"]
    task = Task(title, description, priority, due_date)
    db.add_task(task)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)