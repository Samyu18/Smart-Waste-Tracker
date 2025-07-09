from models import db, User
from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/samyukthajakkula/Desktop/pythonprojects/Smart Waste Tracker 2/instance/waste_tracker.db'
app.config['SECRET_KEY'] = 'supersecretkey'
db.init_app(app)

with app.app_context():
    users = User.query.all()
    if not users:
        print('No users found in the database.')
    else:
        print('User list:')
        for user in users:
            print(f'ID: {user.id}, Username: {user.username}, Email: {user.email}') 