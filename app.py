from flask import Flask, redirect, url_for, render_template
from task import Task

app = Flask(__name__)

first = Task('First Task', 'This is my first task')
second = Task('Second Task', 'This is my second task')
third = Task('Third Task', 'This is my third task')

tasks = [first, second, third]

@app.route('/')
def root():
    return redirect(url_for('index'))

@app.route('/tasks')
def index():
    return render_template('index.html', tasks = tasks)

@app.route('/tasks/<int:id>', methods=["GET"])
def get_task(id):
    task = [task for task in tasks if task.id == id]
    return render_template('show.html', task = task[0])




if __name__ == '__main__':
    app.run(debug=True)
