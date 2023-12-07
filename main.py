from flask import Flask, render_template
import random
from datetime import datetime, timedelta

app = Flask(__name__)

list_of_chores = {
    "Dusting study", "Organizing study", "Empty garbage cans", "Put shoes back in place",
    "Clean Fridge", "Clean Coffee machine", "Clean air fryer", "Clean Tami4", "Clean stove",
    "Clean kitchen table", "Wipe cabinet exterior", "Clean cabinet interior", "Clean oven",
    "Scrub kitchen surfaces", "Declutter dining table", "Wipe brown console", "Wipe dining table",
    "Wipe tv console", "Clean living room tables", "Organize couch", "Dust liquor cabinet",
    "Fold laundry", "Clean mirrors", "Clean guest toilet", "Clean guest bathroom sink",
    "Clean guest bathroom shower", "Clean makeup table", "Clean bedside tables",
    "Clean dryer and washing machine exterior", "Scrub kitchen floor", "Scrub entrance floor",
    "Clean bedroom toilet", "Clean bedroom sink", "Clean bedroom shower",
    "Setup environment and activate herbert", "Clean balcony fridge exterior",
    "Clean study window", "Clean kitchen window", "Clean living room window",
    "Clean guestroom window", "Clean bedroom window", "Clean bedroom bathroom window"
}

daily_chore_assignments = {"Jaanuk": None, "Peach": None}

# Keep track of completed chores and scores
completed_chores = {"Jaanuk": 0, "Peach": 0}

def choose_random_chores(person):
    available_chores = list(list_of_chores - daily_chore_assignments["Jaanuk"] - daily_chore_assignments["Peach"])
    return random.sample(available_chores, 2)

def update_daily_chore_assignments():
    today = datetime.now().date()
    two_days_ago = today - timedelta(days=2)
    
    for person in daily_chore_assignments:
        if daily_chore_assignments[person] is not None and daily_chore_assignments[person]["date"] >= two_days_ago:
            continue  # Skip if assigned in the last two days
        
        daily_chore_assignments[person] = {"chores": choose_random_chores(person), "date": today}

@app.route('/')
def index():
    update_daily_chore_assignments()
    return render_template('index.html', assignments=daily_chore_assignments, scores=completed_chores)

if __name__ == '__main__':
    app.run(debug=True)
