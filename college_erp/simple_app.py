import os
from flask import Flask, render_template, redirect, url_for

def create_app_simple():
    # Create a simple Flask app that redirects to the main ERP system
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'simple_key_for_development'

    @app.route('/')
    def home():
        return redirect('/home')

    @app.route('/home')
    def home_route():
        return render_template('simple_home.html')

    @app.route('/about')
    def about():
        return render_template('about.html')

    # Handle errors
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('simple_home.html'), 404

    return app

if __name__ == '__main__':
    app = create_app_simple()
    app.run(debug=True, port=5001)  # Run on a different port