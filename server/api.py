import argparse
import json
import flask
from model import todo

app = flask.Flask(__name__)

rep = todo.Repository()

@app.route("/api/tasks", methods=["GET"])
def list_tasks():
    tasks = rep.list()
    return todo.serialize_tasks(tasks)

@app.route("/api/tasks", methods=["POST"])
def create_tasks():
    dict_task = json.loads(flask.request.data)
    task = todo.Task(**dict_task)
    id = rep.add(task)
    return json.dumps({"id":id})

@app.route("/api/tasks/<int:id>/done", methods=["POST"])
def done_tasks(id: int):
    rep.done(id)
    return ""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
