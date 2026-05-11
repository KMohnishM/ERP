#!/usr/bin/env python
import os
import sys
import subprocess
import platform

def print_header(message):
    print("\n" + "="*50)
    print(message)
    print("="*50)

def print_step(step_number, message):
    print(f"\nStep {step_number}: {message}")

def run_command(command):
    print(f"> {command}")
    try:
        result = subprocess.run(command, shell=True, check=True, 
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                             universal_newlines=True)
        print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"ERROR: Command failed with exit code {e.returncode}")
        print(e.stderr)
        return False

def main():
    print_header("College ERP System Setup Script")
    
    # Step 1: Install required packages
    print_step(1, "Installing required packages")
    packages = [
        "flask==2.0.1", 
        "werkzeug==2.0.1", 
        "sqlalchemy==1.4.23", 
        "flask-sqlalchemy==2.5.1",
        "flask-migrate==3.1.0", 
        "flask-login==0.5.0", 
        "flask-wtf==0.15.1", 
        "email-validator==1.1.3",
        "python-dotenv==0.19.1", 
        "flask-bcrypt==0.7.1"
    ]
    
    install_cmd = f"pip install {' '.join(packages)}"
    if not run_command(install_cmd):
        print("Failed to install required packages. Aborting setup.")
        return
    
    # Step 2: Initialize the database
    print_step(2, "Initializing database")
    if not run_command("python init_db.py"):
        print("Failed to initialize database. Aborting setup.")
        return
    
    # Step 3: Run the application
    print_step(3, "Starting the College ERP System")
    print("\nThe College ERP System should now be running.")
    print("Access the application at: http://127.0.0.1:5000")
    print("\nDefault Login Credentials:")
    print("Admin: admin@college.edu / admin123")
    print("Staff: staff@college.edu / staff123")
    
    if platform.system() == "Windows":
        run_command("start http://127.0.0.1:5000")
    
    run_command("python run.py")

if __name__ == "__main__":
    main()