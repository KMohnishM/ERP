import os

# Simple Flask app for direct usage
from flask import Flask, render_template

# Create app with explicit template folder
template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'templates'))
app = Flask(__name__, template_folder=template_dir)
print(f"Using template directory: {template_dir}")

# Basic routes
@app.route('/')
def index():
    return render_template('simple_home.html')

@app.route('/login')
def login():
    return render_template('simple_home.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

# Simple error handlers
@app.errorhandler(404)
def page_not_found(e):
    return render_template('simple_home.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('simple_home.html'), 500

if __name__ == '__main__':
    print("=" * 50)
    print("Starting simple Flask app...")
    print("Visit http://127.0.0.1:5000/ to view the application")
    print("=" * 50)
    app.run(debug=True)