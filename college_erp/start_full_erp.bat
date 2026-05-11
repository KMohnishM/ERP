@echo off
setlocal EnableDelayedExpansion

echo ========================================================
echo             COLLEGE ERP SYSTEM LAUNCHER
echo ========================================================
echo.

REM Step 1: Activate the virtual environment
echo [1/3] Activating virtual environment...
call venv\Scripts\activate.bat
if %ERRORLEVEL% neq 0 (
    echo ERROR: Failed to activate virtual environment.
    echo Make sure you have a virtual environment in the 'venv' folder.
    echo If not, create one with: python -m venv venv
    echo Then install dependencies with: pip install -r requirements.txt
    goto :error
)
echo Virtual environment activated successfully.
echo.

REM Step 2: Check if database exists, initialize if needed
echo [2/3] Checking database...
if not exist "app\college_erp.sqlite" (
    echo Database not found. Initializing database...
    python init_db.py
    if %ERRORLEVEL% neq 0 (
        echo ERROR: Failed to initialize database.
        goto :error
    )
    echo Database initialized successfully.
) else (
    echo Database found.
)
echo.

REM Step 3: Run the full ERP system
echo [3/3] Starting College ERP System...
echo.
echo --------------------------------------------------------
echo Access the system at: http://127.0.0.1:5000/
echo Default login: admin@college.edu / admin123
echo --------------------------------------------------------
echo.
python run.py
if %ERRORLEVEL% neq 0 (
    echo ERROR: Failed to start the College ERP System.
    goto :error
)

goto :end

:error
echo.
echo ========================================================
echo                       ERROR
echo ========================================================
echo The College ERP System could not be started.
echo Please check the error messages above.
echo.
echo Troubleshooting steps:
echo 1. Make sure all dependencies are installed:
echo    pip install flask==2.0.1 werkzeug==2.0.1 sqlalchemy==1.4.23 flask-sqlalchemy==2.5.1 flask-migrate==3.1.0 flask-login==0.5.0 flask-wtf==0.15.1 flask-bcrypt==0.7.1
echo.
echo 2. Check that the database is initialized:
echo    python init_db.py
echo.
echo 3. Verify the application structure is intact.
echo.

:end
pause
endlocal