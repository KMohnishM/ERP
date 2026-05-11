@echo off
echo ==== College ERP System Tester ====
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

REM Step 2: Display the options
echo.
echo Choose which app to run:
echo 1. Full ERP System (run.py)
echo 2. Simple App (app.py)
echo.
set /p choice=Enter your choice (1 or 2): 

if "%choice%"=="1" (
    echo.
    echo Starting the full College ERP System...
    python run.py
) else if "%choice%"=="2" (
    echo.
    echo Starting the simple Flask app...
    python app.py
) else (
    echo.
    echo Invalid choice. Please enter 1 or 2.
)

pause