# config.py
class Config:
    SECRET_KEY = 'your_secret_key'
    MONGO_URI = 'mongodb://mongodb-host:27017/home_chores'

class TestConfig(Config):
    MONGO_URI = 'mongodb://localhost:27017/test_database'
