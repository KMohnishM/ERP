import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

# Initialize extensions
db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
bcrypt = Bcrypt()

def create_app():
    # Set the correct template and static folders
    template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'templates'))
    static_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'static'))
    
    app = Flask(__name__, 
                template_folder=template_dir,
                static_folder=static_dir)
    
    # Configuration
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'default_secret_key_for_dev')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///college_erp.sqlite'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    print(f"Using template directory: {template_dir}")
    
    # Initialize extensions with app
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    bcrypt.init_app(app)
    
    login_manager.login_view = 'auth.login'
    login_manager.login_message_category = 'info'
    
    # Import and register blueprints
    from app.routes.auth import auth_bp
    from app.routes.main import main_bp
    from app.routes.admission.routes import admission_bp
    from app.routes.fees.routes import fees_bp
    from app.routes.hostel.routes import hostel_bp
    from app.routes.examination.routes import exam_bp
    from app.routes.dashboard.routes import dashboard_bp
    
    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)
    app.register_blueprint(admission_bp)
    app.register_blueprint(fees_bp)
    app.register_blueprint(hostel_bp)
    app.register_blueprint(exam_bp)
    app.register_blueprint(dashboard_bp)
    
    # Create database tables
    with app.app_context():
        db.create_all()
    
    return app