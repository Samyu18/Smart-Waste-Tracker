from models import db, User, Item
from flask import Flask
from datetime import datetime, timedelta

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/samyukthajakkula/Desktop/pythonprojects/Smart Waste Tracker 2/instance/waste_tracker.db'
app.config['SECRET_KEY'] = 'supersecretkey'
db.init_app(app)

with app.app_context():
    users = User.query.all()
    if not users:
        print('No users found. Please create users first.')
    else:
        for user in users:
            items = [
                # Dairy
                Item(name='Milk', category='Dairy', quantity=10, shelf_life=7, location='Fridge', added_date=datetime.now()-timedelta(days=2), expiry_date=datetime.now()+timedelta(days=5), user_id=user.id),
                Item(name='Cheese', category='Dairy', quantity=2, shelf_life=30, location='Fridge', added_date=datetime.now()-timedelta(days=10), expiry_date=datetime.now()+timedelta(days=20), user_id=user.id),
                # Bakery
                Item(name='Bread', category='Bakery', quantity=5, shelf_life=3, location='Pantry', added_date=datetime.now()-timedelta(days=1), expiry_date=datetime.now()+timedelta(days=2), user_id=user.id),
                Item(name='Croissant', category='Bakery', quantity=12, shelf_life=2, location='Pantry', added_date=datetime.now()-timedelta(days=1), expiry_date=datetime.now()+timedelta(days=1), user_id=user.id),
                # Produce
                Item(name='Apples', category='Produce', quantity=20, shelf_life=14, location='Fruit Basket', added_date=datetime.now()-timedelta(days=3), expiry_date=datetime.now()+timedelta(days=11), user_id=user.id),
                Item(name='Bananas', category='Produce', quantity=6, shelf_life=5, location='Fruit Basket', added_date=datetime.now()-timedelta(days=4), expiry_date=datetime.now()+timedelta(days=1), user_id=user.id),
                # Meat
                Item(name='Chicken', category='Meat', quantity=2, shelf_life=5, location='Freezer', added_date=datetime.now()-timedelta(days=4), expiry_date=datetime.now()+timedelta(days=1), user_id=user.id),
                Item(name='Beef', category='Meat', quantity=1, shelf_life=10, location='Freezer', added_date=datetime.now()-timedelta(days=5), expiry_date=datetime.now()+timedelta(days=5), user_id=user.id),
                # Frozen
                Item(name='Frozen Peas', category='Frozen', quantity=15, shelf_life=180, location='Freezer', added_date=datetime.now()-timedelta(days=30), expiry_date=datetime.now()+timedelta(days=150), user_id=user.id),
                # Canned
                Item(name='Canned Beans', category='Canned', quantity=25, shelf_life=365, location='Pantry', added_date=datetime.now()-timedelta(days=100), expiry_date=datetime.now()+timedelta(days=265), user_id=user.id),
                # Beverages
                Item(name='Juice', category='Beverages', quantity=8, shelf_life=30, location='Fridge', added_date=datetime.now()-timedelta(days=10), expiry_date=datetime.now()+timedelta(days=20), user_id=user.id),
                Item(name='Soda', category='Beverages', quantity=24, shelf_life=180, location='Pantry', added_date=datetime.now()-timedelta(days=20), expiry_date=datetime.now()+timedelta(days=160), user_id=user.id),
                # Snacks
                Item(name='Chips', category='Snacks', quantity=30, shelf_life=60, location='Pantry', added_date=datetime.now()-timedelta(days=5), expiry_date=datetime.now()+timedelta(days=55), user_id=user.id),
                # Expiring soon
                Item(name='Yogurt', category='Dairy', quantity=3, shelf_life=10, location='Fridge', added_date=datetime.now()-timedelta(days=9), expiry_date=datetime.now()+timedelta(days=1), user_id=user.id),
                # Surplus
                Item(name='Tomatoes', category='Produce', quantity=50, shelf_life=7, location='Fridge', added_date=datetime.now()-timedelta(days=1), expiry_date=datetime.now()+timedelta(days=6), user_id=user.id),
            ]
            db.session.add_all(items)
        db.session.commit()
        print('Expanded sample items added for all users.') 