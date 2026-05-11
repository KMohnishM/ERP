import os
import sys
from werkzeug.security import generate_password_hash
from datetime import datetime, timedelta
import uuid
import random

# Add the parent directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))

# Import the app and models
from app import create_app, db
from app.models.models import (User, Student, Staff, Course, FeeStructure, 
                              FeePayment, Hostel, HostelAllocation, 
                              Examination, ExamResult)

def initialize_db():
    app = create_app()
    
    with app.app_context():
        # Drop all tables to start fresh
        db.drop_all()
        # Create all tables
        db.create_all()
        
        print("Database initialized successfully!")
        
def create_admin():
    app = create_app()
    
    with app.app_context():
        # Check if admin already exists
        existing_admin = User.query.filter_by(username='admin').first()
        if existing_admin:
            print("Admin user already exists!")
            return
            
        # Create admin user
        admin_user = User(
            username='admin',
            email='admin@college.edu',
            password=generate_password_hash('admin123'),
            role='admin'
        )
        db.session.add(admin_user)
        db.session.commit()
        
        print("Admin user created successfully!")
        print("Username: admin@college.edu")
        print("Password: admin123")

if __name__ == '__main__':
    print("Initializing database...")
    initialize_db()
    print("Creating admin user...")
    create_admin()
    print("Done! You can now run the application with: flask run")