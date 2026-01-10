@echo off
REM ========================================
REM CHECK IF SYSTEM IS FIXED
REM ========================================

TITLE System Health Check
COLOR 0E

echo ========================================
echo    TESTING IF SYSTEM ERROR IS FIXED
echo ========================================
echo.

echo [TEST 1] Checking Python...
python --version
if %errorlevel% EQU 0 (
    echo [PASSED] Python works!
) else (
    echo [FAILED] Python still broken
)
echo.

echo [TEST 2] Checking Node.js...
node --version
if %errorlevel% EQU 0 (
    echo [PASSED] Node.js works!
) else (
    echo [FAILED] Node.js still broken
)
echo.

echo [TEST 3] Checking npm...
npm --version
if %errorlevel% EQU 0 (
    echo [PASSED] npm works!
) else (
    echo [FAILED] npm still broken
)
echo.

echo ========================================
echo If all tests PASSED, you can now run:
echo   start_admin.bat
echo.
echo If tests FAILED, you need to:
echo   1. Run: sfc /scannow (as Admin)
echo   2. Install WSL2: wsl --install (as Admin)
echo ========================================
echo.

pause
