import os
import sys
from flask import Flask, redirect, url_for

# Add the parent directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))

try:
    # Import the app
    from app import create_app
    
    # Create the app
    app = create_app()
    
    # Print debug information
    print("\n===== APPLICATION DEBUG INFO =====")
    print(f"Blueprint URLs:")
    
    # Print all registered URL rules
    url_rules = []
    for rule in app.url_map.iter_rules():
        url_rules.append(f"Route: {rule.rule}, Endpoint: {rule.endpoint}")
    
    # Sort them for better readability
    url_rules.sort()
    for rule in url_rules:
        print(rule)
    
    print("\n===== END DEBUG INFO =====\n")
    
    # Add a root redirect rule to help with debugging
    @app.route('/debug')
    def debug_route():
        return f"""
        <h1>ERP System Debug</h1>
        <p>The application is running correctly.</p>
        <h2>Registered Routes:</h2>
        <ul>
            {''.join([f'<li>{rule}</li>' for rule in url_rules])}
        </ul>
        <p><a href="/home">Go to Home</a></p>
        <p><a href="/login">Go to Login</a></p>
        <p><a href="/dashboard">Go to Dashboard</a></p>
        """
    
    if __name__ == '__main__':
        app.run(debug=True)
    
except Exception as e:
    print(f"Error: {e}")
    print("Traceback:")
    import traceback
    traceback.print_exc()