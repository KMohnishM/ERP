@echo off
echo ==== College ERP System Starter ====
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

REM Step 2: Run the ERP application
echo.
echo Step 2: Starting the College ERP System...
python run.py
if %ERRORLEVEL% neq 0 (
    echo.
    echo Trying simplified app as fallback...
    python app.py
)

pause