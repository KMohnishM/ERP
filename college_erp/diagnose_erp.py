import os
import sys
import importlib
import sqlite3
import traceback

def print_header(title):
    print("\n" + "=" * 60)
    print(f"{title:^60}")
    print("=" * 60)

def check_python_version():
    print(f"Python version: {sys.version}")
    print(f"Python executable: {sys.executable}")
    
def check_dependencies():
    print_header("Checking Dependencies")
    
    required_packages = [
        "flask==2.0.1", 
        "werkzeug==2.0.1", 
        "sqlalchemy==1.4.23", 
        "flask-sqlalchemy==2.5.1",
        "flask-migrate==3.1.0", 
        "flask-login==0.5.0", 
        "flask-wtf==0.15.1", 
        "flask-bcrypt==0.7.1"
    ]
    
    for package in required_packages:
        package_name = package.split("==")[0]
        required_version = package.split("==")[1]
        
        try:
            module = importlib.import_module(package_name.replace("-", "_"))
            version = getattr(module, "__version__", "unknown")
            
            status = "OK" if version == required_version else f"WARNING: expected {required_version}, found {version}"
            print(f"{package_name:.<30} {status}")
        except ImportError:
            print(f"{package_name:.<30} NOT FOUND")

def check_directory_structure():
    print_header("Checking Directory Structure")
    
    expected_dirs = [
        "app",
        "app/models",
        "app/routes",
        "app/static",
        "app/templates",
        "venv"
    ]
    
    expected_files = [
        "app/__init__.py",
        "app/models/models.py",
        "run.py",
        "init_db.py",
        "requirements.txt"
    ]
    
    for directory in expected_dirs:
        if os.path.isdir(directory):
            print(f"{directory:.<40} OK")
        else:
            print(f"{directory:.<40} MISSING")
    
    print("\nChecking key files:")
    for file in expected_files:
        if os.path.isfile(file):
            print(f"{file:.<40} OK")
        else:
            print(f"{file:.<40} MISSING")

def check_database():
    print_header("Checking Database")
    
    db_path = "app/college_erp.sqlite"
    
    if not os.path.isfile(db_path):
        print(f"Database file {db_path} not found!")
        return
        
    print(f"Database file found: {db_path}")
    
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Get list of tables
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        
        print(f"\nFound {len(tables)} tables in the database:")
        for table in tables:
            cursor.execute(f"SELECT COUNT(*) FROM {table[0]}")
            count = cursor.fetchone()[0]
            print(f"  - {table[0]}: {count} records")
            
        # Check specifically for User table and admin user
        if ('user',) in tables:
            cursor.execute("SELECT COUNT(*) FROM user WHERE role='admin'")
            admin_count = cursor.fetchone()[0]
            print(f"\nAdmin users found: {admin_count}")
        else:
            print("\nUser table not found in database!")
            
        conn.close()
    except Exception as e:
        print(f"Error accessing database: {e}")

def run_app_import_test():
    print_header("Testing Application Import")
    
    try:
        from app import create_app
        print("Successfully imported create_app function")
        
        try:
            app = create_app()
            print("Successfully created app instance")
            
            # Check registered blueprints
            if hasattr(app, 'blueprints'):
                print(f"\nRegistered blueprints: {len(app.blueprints)}")
                for name in app.blueprints:
                    print(f"  - {name}")
        except Exception as e:
            print(f"Error creating app: {e}")
            traceback.print_exc()
            
    except ImportError as e:
        print(f"Import error: {e}")
        traceback.print_exc()
    except Exception as e:
        print(f"Unexpected error: {e}")
        traceback.print_exc()

def main():
    print_header("College ERP System Diagnostic")
    
    # Get current directory
    print(f"Current directory: {os.getcwd()}")
    check_python_version()
    check_dependencies()
    check_directory_structure()
    check_database()
    run_app_import_test()
    
    print_header("Diagnostic Complete")
    print("If issues were found, please address them before running the full system.")
    print("To initialize the database: python init_db.py")
    print("To start the full system: python run.py")

if __name__ == "__main__":
    main()
    input("\nPress Enter to exit...")