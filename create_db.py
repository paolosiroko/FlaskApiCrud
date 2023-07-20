from app import app, db

# This block creates the application context
with app.app_context():
    # Now you can call db.create_all() within the context
    db.create_all()
