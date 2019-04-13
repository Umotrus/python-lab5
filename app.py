from flask import Flask, render_template, redirect, url_for, request
import db_interaction

app = Flask(__name__)


@app.route('/')
def index():
    task_list = db_interaction.get_sorted_tasks_list()
    return render_template("index.html", tasks=task_list)


@app.route("/index.html")
def index_redirect():
    return redirect('/')


@app.route('/insert_task', methods=['POST'])
def insert_new_task():
    db_interaction.db_insert_task(request.form['text'])
    return redirect(url_for('index'))


@app.route('/delete/<int:id_task>')
def delete_task(id_task):
    db_interaction.db_remove_task(id_task)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()
