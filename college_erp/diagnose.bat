@echo off
echo ========================================================
echo            COLLEGE ERP SYSTEM DIAGNOSTICS
echo ========================================================
echo.

REM Step 1: Activate the virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat
if %ERRORLEVEL% neq 0 (
    echo ERROR: Failed to activate virtual environment.
    echo Continuing without virtual environment...
)

REM Step 2: Run the diagnostic script
echo Running diagnostic checks...
echo.
python diagnose_erp.py

echo.
pause