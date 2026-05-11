import os
import sys

# Try to import the full ERP system
try:
    from app import create_app, db
    from app.models.models import User
    from flask_login import current_user

    app = create_app()

    # Add a root route handler for debugging
    @app.route('/check')
    def check_system():
        """Diagnostic route to check system status."""
        return """
        <h1>ERP System Status Check</h1>
        <p>The ERP system is running correctly.</p>
        <p><a href="/">Go to Home Page</a></p>
        <p><a href="/login">Go to Login Page</a></p>
        <p><a href="/dashboard">Go to Dashboard</a></p>
        """

    if __name__ == '__main__':
        print("=" * 50)
        print("Starting the complete College ERP System...")
        print("Access the system at: http://127.0.0.1:5000/")
        print("Default admin login: admin@college.edu / admin123")
        print("=" * 50)
        app.run(debug=True)
except ImportError as e:
    print("=" * 50)
    print(f"ERROR: Failed to import required modules: {e}")
    print("\nThis is likely due to missing dependencies. Please run:")
    print("pip install -r requirements.txt")
    print("\nIf you're using a virtual environment, make sure it's activated.")
    print("=" * 50)
except Exception as e:
    print("=" * 50)
    print(f"ERROR: An unexpected error occurred: {e}")
    print("\nPlease check that:")
    print("1. All dependencies are installed correctly")
    print("2. Database initialization has been completed")
    print("3. The application structure is intact")
    print("\nYou can initialize the database with: python init_db.py")
    print("=" * 50)