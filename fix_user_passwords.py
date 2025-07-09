from models import db, User
from flask import Flask
from werkzeug.security import check_password_hash

# Setup Flask app and DB context
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/samyukthajakkula/Desktop/pythonprojects/Smart Waste Tracker 2/instance/waste_tracker.db'
app.config['SECRET_KEY'] = 'supersecretkey'
db.init_app(app)

def is_hashed(pw_hash):
    # Werkzeug hashes start with 'pbkdf2:'
    return pw_hash.startswith('pbkdf2:')

with app.app_context():
    users = User.query.all()
    updated = 0
    for user in users:
        if not is_hashed(user.password_hash):
            # You can set a default password for all affected users
            user.set_password(user.password_hash)  # Re-hash the old plain password
            updated += 1
    if updated > 0:
        db.session.commit()
        print(f"Updated {updated} user(s) with hashed passwords.")
    else:
        print("All users already have hashed passwords.") 