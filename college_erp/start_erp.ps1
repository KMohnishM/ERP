# Start College ERP System
Write-Host "=== College ERP System Starter ===" -ForegroundColor Green

# Step 1: Activate the virtual environment
Write-Host "`nStep 1: Activating virtual environment..." -ForegroundColor Cyan
try {
    & .\venv\Scripts\activate.ps1
    Write-Host "Virtual environment activated successfully." -ForegroundColor Green
} 
catch {
    Write-Host "Error activating virtual environment: $_" -ForegroundColor Red
    Write-Host "Please ensure the virtual environment exists at .\venv\" -ForegroundColor Yellow
    exit
}

# Step 2: Run the ERP application
Write-Host "`nStep 2: Starting the College ERP System..." -ForegroundColor Cyan
try {
    python run.py
}
catch {
    Write-Host "Error starting College ERP: $_" -ForegroundColor Red
    
    Write-Host "`nTrying simplified app as fallback..." -ForegroundColor Yellow
    python app.py
}

# Keep PowerShell window open
Write-Host "`nPress any key to exit..." -ForegroundColor Gray
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")