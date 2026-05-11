@echo off
echo ==== College ERP Database Initializer ====
echo.

REM Step 1: Activate the virtual environment
echo Step 1: Activating virtual environment...
call venv\Scripts\activate.bat
if %ERRORLEVEL% neq 0 (
    echo Error: Failed to activate virtual environment.
    echo Please ensure the virtual environment exists at .\venv\
    pause
    exit /b 1
)
echo Virtual environment activated successfully.

REM Step 2: Initialize the database
echo.
echo Step 2: Initializing the database...
python init_db.py
if %ERRORLEVEL% neq 0 (
    echo Error: Failed to initialize the database.
    echo Please check the error messages above.
    pause
    exit /b 1
)

echo.
echo Database initialization completed successfully.
echo You can now run the application with start_erp.bat

pause