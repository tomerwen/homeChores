from flask import Flask
from .models import db
from .utils import run_bi_weekly_cycle
from .chores import chores_bp
from .tasks import tasks_bp

listOfChores={
    "Dusting study",
    "Organizing study",
    "Empty garbage cans",
    "Put shoes back in place",
    "Clean Fridge",
    "Clean Coffee machine",
    "Clean air fryer",
    "Clean Tami4",
    "Clean stove",
    "Clean kitchen table",
    "Wipe cabinet exterior",
    "Clean cabinet interior",
    "Clean oven",
    "Scrub kitchen surfaces",
    "Declutter dining table",
    "Wipe brown consule",
    "Wipe dining table",
    "Wipe tv console",
    "Clean living room tables",
    "Organize couch",
    "Dust liquer cabinet",
    "Fold laundry",
    "Clean mirrors",
    "Clean guest toilet",
    "Clean guest bathroom sink",
    "Clean guest bathroom shower",
    "Clean makeup table",
    "Clean bedside tables",
    "Clean dryer and washing machine exterior",
    "Scrub kitchen floor",
    "Scrub entrance floor",
    "Clean bedroom toilet",
    "Clean bedroom sink",
    "Clean bedroom shower",
    "Setup environment and activate herbert",
    "Clean balcony fridge exterior",
    "Clean study window",
    "Clean kitchen window",
    "Clean living room window",
    "Clean guestroom window",
    "Clean bedroom window",
    "Clean bedroom bathroom window"
}

app = Flask(__name__)

# Configure database connection
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:password@localhost/chores"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

# Register blueprints
app.register_blueprint(chores_bp)
app.register_blueprint(tasks_bp)

# Schedule bi-weekly cycle
from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler()
scheduler.add_job(func=run_bi_weekly_cycle, trigger="interval", days=14)
scheduler.start()

if __name__ == "__main__":
    app.run(debug=True)
