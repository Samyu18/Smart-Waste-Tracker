# Smart Waste Tracker

A web app for retail stores to track, predict, and minimize inventory waste using Python, Flask, and data structures.

## Features
- Track spoilage by category and shelf life
- Predict surplus items using demand forecasting (sliding window)
- Suggest donation, repurposing, or recycling plans
- Optimize storage using space-time efficiency (hash maps, priority queues)

## Setup
1. **Clone the repo**
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Initialize the database:**
   ```bash
   python
   >>> from app import db
   >>> db.create_all()
   >>> exit()
   ```
4. **Run the app:**
   ```bash
   python app.py
   ```
5. **Open in browser:**
   Visit [http://127.0.0.1:5000](http://127.0.0.1:5000)

## File Structure
- `app.py` - Main Flask app and routes
- `models.py` - SQLAlchemy models
- `templates/` - HTML templates
- `requirements.txt` - Python dependencies

## Notes
- Uses Bootstrap for styling
- Demo thresholds are set for surplus prediction (can be tuned)
- For production, use a more robust database and authentication 