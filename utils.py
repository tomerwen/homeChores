from datetime import date, timedelta
from .models import Chore


def run_bi_weekly_cycle():
    # Mark all chores as inactive
    Chore.query.update({"active": False})

    # Select two random chores and activate them
    inactive_chores = Chore.query.filter_by(active=False).all()
    random_chores = random.sample(inactive_chores, 2)
    for chore in random_chores:
        chore.active = True

    # Create daily tasks for the next two weeks
    two_weeks_from_now = date.today() + timedelta(days=14)
    for day in range(14):
        current_date = date.today() + timedelta(days=day)
        for chore in random_chores:
            daily_task = DailyTask(chore_id=chore.id, date=current_date)
            db.session.add(daily_task)

    # Reset completed flag for daily tasks
    DailyTask.query.update({"completed": False})

    # Commit changes to the database
    db.session.commit()
