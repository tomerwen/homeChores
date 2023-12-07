from flask import Flask, render_template, request, redirect, url_for
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
    available_chores = set(list_of_chores)

    if daily_chore_assignments["Jaanuk"] is not None and daily_chore_assignments["Jaanuk"]["chores"] is not None:
        available_chores -= set(daily_chore_assignments["Jaanuk"]["chores"])
    if daily_chore_assignments["Peach"] is not None and daily_chore_assignments["Peach"]["chores"] is not None:
        available_chores -= set(daily_chore_assignments["Peach"]["chores"])

    return random.sample(available_chores, 2)


def update_daily_chore_assignments():
    today = datetime.now().date()
    two_days_ago = today - timedelta(days=2)
    
    for person in daily_chore_assignments:
        if daily_chore_assignments[person] is not None and daily_chore_assignments[person]["date"] >= two_days_ago:
            continue  # Skip if assigned in the last two days
        
        daily_chore_assignments[person] = {"chores": choose_random_chores(person), "date": today}


@app.route('/')
def choose_user():
    return render_template('index.html')

@app.route('/set_user', methods=['POST'])
def set_user():
    user = request.form.get('user')
    if user in daily_chore_assignments:
        return redirect(url_for('show_chores', user=user))
    else:
        return "Invalid user"

@app.route('/chores/<user>')
def show_chores(user):
    update_daily_chore_assignments()

    if user not in daily_chore_assignments:
        return "Invalid user"

    user_chores = daily_chore_assignments[user].get("chores")  # Use .get to handle None

    if user_chores is None:
        return "No chores assigned for today."

    return render_template('chores.html', user=user, chores=user_chores)

if __name__ == '__main__':
    app.run(debug=True)
