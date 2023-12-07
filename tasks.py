from flask import Blueprint, jsonify, request

from .models import DailyTask

tasks_bp = Blueprint("tasks", __name__)


@tasks_bp.route("/tasks/<int:task_id>/complete", methods=["PUT"])
def mark_task_complete(task_id):
    task = DailyTask.query.get(task_id)
    task.completed = True
    db.session.commit()
    return jsonify({"message": "Task marked as completed"})
