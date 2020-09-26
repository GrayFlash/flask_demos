from flask import Flask, render_template, request

app = Flask(__name__)

todos = []
@app.route("/")
def tasks():
    todo = request.args.get("task")
    if todo:
        todos.append(todo)
    return render_template("tasks.html", todos=todos)

@app.route("/addTask")
def addTasks():
    return render_template("addTask.html")
