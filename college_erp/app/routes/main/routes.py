from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
@main_bp.route('/home')
def home():
    if current_user.is_authenticated:
        # If user is logged in, redirect based on role
        if current_user.role in ['admin', 'staff']:
            return redirect(url_for('dashboard.dashboard'))
        else:
            # For students or other roles
            return render_template('main/home.html', title='Home')
    else:
        # If user is not logged in, redirect to login
        return redirect(url_for('auth.login'))

@main_bp.route('/about')
def about():
    return render_template('main/about.html', title='About')

@main_bp.route('/contact')
def contact():
    return render_template('main/contact.html', title='Contact')