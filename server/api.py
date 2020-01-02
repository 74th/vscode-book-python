import json
import flask
from model import tasks

app = flask.Flask(__name__)

rep = tasks.Repository()

@app.route("/api/tasks", methods=["GET"])
def list_tasks():
    task_list = rep.list()
    return tasks.serialize_tasks(task_list)

@app.route("/api/tasks", methods=["POST"])
def create_task():
    task = tasks.deserialize_task(flask.request.data)
    id = rep.add(task)
    return json.dumps({"id":id})

@app.route("/api/tasks/<int:id>/done", methods=["POST"])
def done_tasks(id: int):
    rep.done(id)
    return ""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
