from flask import Blueprint, jsonify
from .models import Chore

chores_bp = Blueprint("chores", __name__)


@chores_bp.route("/chores/active")
def get_active_chores():
    active_chores = Chore.query.filter_by(active=True).all()
    return jsonify({"chores": [chore.serialize for chore in active_chores]})
