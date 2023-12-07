from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey
from sqlalchemy.orm import relationship

from .db import Base


class Chore(Base):
    __tablename__ = "chores"
    id = Column(Integer, primary_key=True)
    chore_name = Column(String(100), nullable=False)
    points = Column(Integer)
    category = Column(String(50))
    active = Column(Boolean, default=False)

    tasks = relationship("DailyTask", backref="chore")
    user_chores = relationship("UserChore", backref="chore")


class DailyTask(Base):
    __tablename__ = "daily_tasks"
    id = Column(Integer, primary_key=True)
    chore_id = Column(Integer, ForeignKey("chores.id"))
    date = Column(Date)
    completed = Column(Boolean, default=False)


class UserChore(Base):
    __tablename__ = "user_chores"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    chore_id = Column(Integer, ForeignKey("chores.id"))
    points_earned = Column(Integer, default=0)
    last_completed_date = Column(Date)
