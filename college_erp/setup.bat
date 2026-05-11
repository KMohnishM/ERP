@echo off
echo Reinstalling packages with compatible versions...
pip uninstall -y flask flask-login flask-sqlalchemy flask-migrate flask-wtf werkzeug
pip install -r requirements.txt

echo Creating the database...
python -c "from app import create_app, db; app = create_app(); app.app_context().push(); db.create_all()"

echo Initializing sample data...
python setup_data.py

echo Setup completed successfully!
echo.
echo You can now run the application with: flask run